import pandas as pd
import numpy as np
import os
import json

# Percorsi file
input_file_path = '/Users/lucavisconti/Documents/FoodAI/csv/new_data.csv'
output_file_path = '/Users/lucavisconti/Documents/FoodAI/csv/trained-data.csv'
stats_file_path = '/Users/lucavisconti/Documents/FoodAI/json/ML_results.json'
approved_categories_file = '/Users/lucavisconti/Documents/FoodAI/csv/approved_categories.csv'
json_output_file = '/Users/lucavisconti/Documents/FoodAI/json/output.json'

df = pd.read_csv(input_file_path)

# Filtra i 20 record con il punteggio "nutritional_score" più alto per ciascuna categoria
df_top20 = (df
           .groupby('category', group_keys=False)
           .apply(lambda x: x.nlargest(20, 'nutritional_score'))
           .reset_index(drop=True))

df_output = df_top20.drop(columns=['sugar_penalty', 'fiber_bonus'])
df_output.to_csv(output_file_path, index=False)

print(f"File di output salvato come {output_file_path}")

# Funzione per caricare le statistiche
def load_statistics(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {'approved': 0, 'rejected': 0}

# Funzione per salvare le statistiche
def save_statistics(stats, file_path):
    with open(file_path, 'w') as file:
        json.dump(stats, file, indent=4)

# Funzione per salvare il feedback in formato JSON
def save_feedback_to_json(feedback_list, file_path):
    with open(file_path, 'w') as file:
        json.dump(feedback_list, file, indent=4)

# Funzione per caricare le categorie approvate
def load_approved_categories(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)['category'].tolist()
    return []

# Funzione per salvare le categorie approvate
def save_approved_categories(categories, file_path):
    pd.DataFrame({'category': categories}).to_csv(file_path, index=False)

# Funzione per gestire il feedback
def get_feedback_and_update(df_trained, df_linear, approved_categories_file, stats_file_path, json_output_file):
    approved_categories = load_approved_categories(approved_categories_file)
    stats = load_statistics(stats_file_path)
    feedback_list = []

    categories = df_trained['category'].unique()
    df_updated = df_trained.copy()

    for category in categories:
        if category in approved_categories:
            continue

        df_category = df_trained[df_trained['category'] == category]
        if df_category.empty:
            continue

        random_index = np.random.choice(df_category.index)
        random_food = df_category.loc[random_index]

        description_column = 'description'

        print(f"\nCategoria: {category}")
        print(f"Alimento: {random_food[description_column]}")
        print(f"Carboidrati (g): {random_food['carbohydrate']}")
        print(f"Proteine (g): {random_food['protein']}")
        print(f"Grassi (g): {random_food['fat']}")

        feedback = input("Se l'alimento è nutriente (sì/no) o digitare 'stop' per interrompere: ").strip().lower()

        if feedback == 'stop':
            save_approved_categories(approved_categories, approved_categories_file)
            save_statistics(stats, stats_file_path)
            save_feedback_to_json(feedback_list, json_output_file)
            print("Feedback interrotto.")
            print(f"Alimenti approvati: {stats['approved']}")
            print(f"Alimenti rifiutati: {stats['rejected']}")
            return df_updated

        if feedback == 'sì':
            approved_categories.append(category)
            stats['approved'] += 1
            feedback_entry = {
                'category': category,
                'description': random_food[description_column],
                'feedback': 'approvato'
            }
        elif feedback == 'no':
            df_linear_category = df_linear[df_linear['category'] == category]
            df_linear_category = df_linear_category[
                ~df_linear_category[description_column].isin(df_trained[description_column])]

            if not df_linear_category.empty:
                best_alternative = df_linear_category.nlargest(1, 'nutritional_score').iloc[0]
                df_updated.loc[random_index] = best_alternative
                print(f"Alimento sostituito con: {best_alternative[description_column]}")
                feedback_entry = {
                    'category': category,
                    'description': best_alternative[description_column],
                    'feedback': 'approvato'
                }
            else:
                df_updated = df_updated.drop(random_index)
                print("Nessuna alternativa disponibile. Record eliminato.")
                stats['rejected'] += 1
                feedback_entry = {
                    'category': category,
                    'description': random_food[description_column],
                    'feedback': 'rifiutato'
                }

        feedback_list.append(feedback_entry)

    save_approved_categories(approved_categories, approved_categories_file)
    save_statistics(stats, stats_file_path)
    save_feedback_to_json(feedback_list, json_output_file)

    print(f"Alimenti approvati: {stats['approved']}")
    print(f"Alimenti rifiutati: {stats['rejected']}")

    return df_updated

# Carica i dati
input_file_path_linear = '/Users/lucavisconti/Documents/FoodAI/csv/new_data.csv'
input_file_path_trained = '/Users/lucavisconti/Documents/FoodAI/csv/trained-data.csv'
output_file_path_updated = '/Users/lucavisconti/Documents/FoodAI/csv/updated-trained-data.csv'

df_linear = pd.read_csv(input_file_path_linear)
df_trained = pd.read_csv(input_file_path_trained)

# Aggiorna con i nuovi feedback
df_updated = get_feedback_and_update(df_trained, df_linear, approved_categories_file, stats_file_path, json_output_file)
df_updated.to_csv(output_file_path_updated, index=False)

print(f"File aggiornato salvato come {output_file_path_updated}")
print(f"Feedback salvato in {json_output_file}")