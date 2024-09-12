import pandas as pd
import numpy as np
import os
import json

input_file_path = '/Users/lucavisconti/Documents/FoodAI/csv/new_data.csv'
df = pd.read_csv(input_file_path)

# Filtra i 20 record con il punteggio "nutritional_score" più alto, per ciascuna categoria
df_top20 = (df
           .groupby('category', group_keys=False)
           .apply(lambda x: x.nlargest(20, 'nutritional_score'))
           .reset_index(drop=True))

df_output = df_top20.drop(columns=['sugar_penalty', 'fiber_bonus'])

output_file_path = '/Users/lucavisconti/Documents/FoodAI/csv/trained-data.csv'
df_output.to_csv(output_file_path, index=False)

print(f"File di output salvato come {output_file_path}")

# Statistiche training
stats_file_path = '/Users/lucavisconti/Documents/FoodAI/csv//ML_results.json'

def load_statistics(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {'approved': 0, 'rejected': 0}


def save_statistics(stats, file_path):
    with open(file_path, 'w') as file:
        json.dump(stats, file, indent=4)


def load_approved_categories(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)['category'].tolist()
    return []


def save_approved_categories(categories, file_path):
    pd.DataFrame({'category': categories}).to_csv(file_path, index=False)


def get_feedback_and_update(df_trained, df_linear, approved_categories_file, stats_file_path):
    # Verifica le categorie già approvate
    approved_categories = load_approved_categories(approved_categories_file)

    # Carica le statistiche esistenti
    stats = load_statistics(stats_file_path)

    # Verifica i nomi delle colonne
    print("Colonne in df_trained:", df_trained.columns)
    print("Colonne in df_linear:", df_linear.columns)


    categories = df_trained['category'].unique()
    # Crea una copia per gli update
    df_updated = df_trained.copy()

    for category in categories:
        # Non considerare le categorie già approvate
        if category in approved_categories:
            continue

        # Scelta random dell'alimento per la categoria corrente
        df_category = df_trained[df_trained['category'] == category]
        if df_category.empty:
            continue

        random_index = np.random.choice(df_category.index)
        random_food = df_category.loc[random_index]

        description_column = 'description'
        carbohydrate_column = 'carbohydrate'
        protein_column = 'protein'
        fat_column = 'fat'

        print(f"\nCategoria: {category}")
        print(f"Alimento: {random_food[description_column]}")
        print(f"Carboidrati (g): {random_food[carbohydrate_column]}")
        print(f"Proteine (g): {random_food[protein_column]}")
        print(f"Grassi (g): {random_food[fat_column]}")

        feedback = input("Se l'alimento è nutriente (sì/no) o digitare 'stop' per interrompere: ").strip().lower()

        if feedback == 'stop':
            # Salva lo stato corrente e interrompe il processo
            save_approved_categories(approved_categories, approved_categories_file)
            save_statistics(stats, stats_file_path)
            print("Feedback interrotto.")
            # Mostra le statistiche finali
            print(f"Alimenti approvati: {stats['approved']}")
            print(f"Alimenti rifiutati: {stats['rejected']}")
            return df_updated

        if feedback == 'sì':
            # Aggiungi la categoria alla lista delle approvate
            approved_categories.append(category)
            stats['approved'] += 1
        elif feedback == 'no':
            # Trova un'alternativa con il punteggio nutrizionale più alto
            df_linear_category = df_linear[df_linear['category'] == category]
            df_linear_category = df_linear_category[
                ~df_linear_category[description_column].isin(df_trained[description_column])]

            if not df_linear_category.empty:
                best_alternative = df_linear_category.nlargest(1, 'nutritional_score').iloc[0]
                # Sostituisci l'alimento selezionato con l'alternativa migliore
                df_updated.loc[random_index] = best_alternative
                print(f"Alimento sostituito con: {best_alternative[description_column]}")
            else:
                # Elimina l'alimento se non ci sono alternative disponibili
                df_updated = df_updated.drop(random_index)
                print("Nessuna alternativa disponibile. Record eliminato.")
                stats['rejected'] += 1

    # Aggiorna le categorie approvate
    save_approved_categories(approved_categories, approved_categories_file)
    # Aggiorna le statistiche
    save_statistics(stats, stats_file_path)

    print(f"Alimenti approvati: {stats['approved']}")
    print(f"Alimenti rifiutati: {stats['rejected']}")

    return df_updated

input_file_path_linear = '/Users/lucavisconti/Documents/FoodAI/csv/new_data.csv'
input_file_path_trained = '/Users/lucavisconti/Documents/FoodAI/csv/trained-data.csv'
output_file_path_updated = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/updated-trained-data.csv'
approved_categories_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/approved_categories.csv'

df_linear = pd.read_csv(input_file_path_linear)
df_trained = pd.read_csv(input_file_path_trained)

# Aggiorna con i nuovi feedback
df_updated = get_feedback_and_update(df_trained, df_linear, approved_categories_file, stats_file_path)
df_updated.to_csv(output_file_path_updated, index=False)

print(f"File aggiornato salvato come {output_file_path_updated}")
