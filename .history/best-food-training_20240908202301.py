import pandas as pd
import numpy as np
import os

# Vecchia implementazione (eseguito dopo nutra.py)
def load_dataset(input_file):
    """Carica il dataset dal file CSV."""
    return pd.read_csv(input_file)


# Funzione per estrarre le righe con il massimo punteggio nutrizionale
def get_row(max_score, df):
    return df[df['nutritional_score'] == max_score], df[df['nutritional_score'] < max_score]


# Funzione per trovare il miglior alimento in base ai criteri
def find_best_food(df, category, food_list, remaining_categories, categories_df):
    """Trova il miglior alimento per una specifica categoria."""
    if food_list is None:
        categories_df.loc[categories_df['category'] == category, 'stato'] = 'completata'
        category = np.random.choice(list(remaining_categories))
        food_list = df[df['category'] == category]

    if food_list is not None and len(food_list['nutritional_score']) > 0:
        best_food, food_list = get_row(max(food_list['nutritional_score']), food_list)
        return best_food, food_list, category
    return None, None, None


# Funzione per richiedere feedback e gestire l'alternativa
def request_feedback(category, initial_food, df, food_list, evaluated_food_ids, remaining_categories, categories_df):
    """Richiede feedback sull'alimento proposto e gestisce le alternative."""
    print(f"\nCategoria: {category}")
    print(f"Alimento proposto: {initial_food['category']}")
    print(f"Descrizione: {initial_food['description']}")
    print(f"Carboidrati: {initial_food['carbohydrate']}")
    print(f"Proteine: {initial_food['protein']}")
    print(f"Grassi: {initial_food['fat']}")
    print(f"Kilocalorie: {initial_food['kilocalories']}")

    feedback = input("Questo alimento è adatto? (s/n) oppure digitare 'stop' per fermare: ").strip().lower()

    if feedback == 'stop':
        return None, 'interrotto', category

    if feedback == 's':
        return initial_food, 'approvato', category
    else:
        return initial_food, 'rifiutato', category


# Funzione principale
def main(input_file, output_file, categories_file):
    """Esegue il processo di selezione e salvataggio dei migliori alimenti."""
    df = load_dataset(input_file)

    # Carica le categorie o crea il file delle categorie
    if os.path.exists(categories_file):
        categories_df = pd.read_csv(categories_file)
    else:
        unique_categories = df['category'].unique()
        categories_df = pd.DataFrame({
            'category': unique_categories,
            'accettati': 0,
            'rifiutati': 0,
            'stato': 'da verificare'
        })

    # Carica gli alimenti già valutati
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        evaluated_df = pd.read_csv(output_file)
        if 'id' in evaluated_df.columns:
            evaluated_food_ids = evaluated_df['id'].tolist()
        else:
            print("La colonna 'id' non è presente nel file di output. Verifica il file.")
            evaluated_food_ids = []
    else:
        evaluated_food_ids = []

    results = pd.DataFrame(columns=[
        'category',
                        'description',
                        'carbohydrate',
                        'protein',
                        'fat',
                        'kilocalories',
                        'feedback',
                        'generic_category',
                        'carb_percentage',
                        'fat_percentage',
                        'protein_percentage',
                        'nutritional_score'
    ])

    processed_categories = set()
    feedback = 'in esecuzione'

    while feedback != 'interrotto':
        # Seleziona una categoria specifica random tra quelle non ancora processate
        remaining_categories = set(
            categories_df[categories_df['stato'] == 'da verificare']['category']) - processed_categories

        if not remaining_categories:
            print("Non ci sono più categorie valide da processare.")
            break

        category = np.random.choice(list(remaining_categories))
        food_list = df[df['category'] == category]

        condition = categories_df[categories_df['category'] == category]['stato'] == 'da verificare'

        while condition.any() and feedback != 'interrotto':
            best_food, food_list, category = find_best_food(df, category, food_list, remaining_categories,
                                                            categories_df)

            if best_food is not None:
                final_food, feedback, category = request_feedback(category, best_food, df, food_list,
                                                                  evaluated_food_ids, remaining_categories,
                                                                  categories_df)

                if feedback == 'approvato' and final_food is not None:
                    new_rows = pd.DataFrame({
                        'original_category': category,
                        'category': final_food['category'],
                        'description': final_food['description'],
                        'carbohydrate': final_food['carbohydrate'],
                        'protein': final_food['protein'],
                        'fat': final_food['fat'],
                        'kilocalories': final_food['kilocalories'],
                        'feedback': feedback,
                        'generic_category' : final_food['generic_category'],
                        'carb_percentage': final_food['carb_percentage'],
                        'fat_percentage': final_food['fat_percentage'],
                        'protein_percentage': final_food['protein_percentage'],
                        'nutritional_score': final_food['nutritional_score']
                    })
                    results = pd.concat([results, new_rows], ignore_index=True)
                    categories_df.loc[categories_df['category'] == category, 'accettati'] += 1
                    evaluated_food_ids.append(final_food['id'])

                    if len(results[(results['category'] == category) & (results['feedback'] == 'approvato')]) == 5:
                        categories_df.loc[categories_df['category'] == category, 'stato'] = 'completata'
                        processed_categories.add(category)
                        break

                if feedback == 'rifiutato' and final_food is not None:
                    new_rows = pd.DataFrame({
                        'original_category': category,
                        'category': final_food['category'],
                        'description': final_food['description'],
                        'carbohydrate': final_food['carbohydrate'],
                        'protein': final_food['protein'],
                        'fat': final_food['fat'],
                        'kilocalories': final_food['kilocalories'],
                        'feedback': feedback,
                        'generic_category' : final_food['generic_category'],
                        'carb_percentage': final_food['carb_percentage'],
                        'fat_percentage': final_food['fat_percentage'],
                        'protein_percentage': final_food['protein_percentage'],
                        'nutritional_score': final_food['nutritional_score']
                    })
                    results = pd.concat([results, new_rows], ignore_index=True)
                    evaluated_food_ids.append(final_food['id'])
                    categories_df.loc[categories_df['category'] == category, 'rifiutati'] += 1
                    print(results)
        else:
            print(f"Training interrotto.")

    # Salva i risultati
    results_df = results
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        existing_results_df = pd.read_csv(output_file)
        results_df = pd.concat([existing_results_df, results_df], ignore_index=True)

    results_df.to_csv(output_file, index=False)
    categories_df.to_csv(categories_file, index=False)

    print(f"I risultati finali sono stati salvati in '{output_file}'")
    print(f"Lo stato delle categorie è stato aggiornato in '{categories_file}'")


# Esegui la funzione principale
input_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/linear_regression_data.csv'
training_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-file.csv'
categories_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/categories-file.csv'

main(input_file, training_file, categories_file)
