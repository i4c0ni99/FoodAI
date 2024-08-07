import pandas as pd

# Funzione per stampare le categorie con generic_category 'other'
def print_other_categories(input_csv_path):
    
    df = pd.read_csv(input_csv_path)
 
    df.columns = [col.lower() for col in df.columns]

    # Controlla se le colonne 'category' e 'generic_category' esistono
    if 'category' in df.columns and 'generic_category' in df.columns:
        # Filtra i record con generic_category 'other'
        other_categories = df[df['generic_category'] == 'other']['category']

        # Calcola il numero di record con generic_category 'other'
        num_other_categories = len(other_categories)
        
        # Stampa il numero di record
        print(f"Numero di record con generic_category 'other': {num_other_categories}")
        
        # Stampa le categorie
        for category in other_categories:
            print(category)
    else:
        print("Le colonne 'category' e 'generic_category' non esistono nel dataset")

input_csv_path = '/Users/lucavisconti/Documents/FoodAI/csv/prepared-food-data.csv'

print_other_categories(input_csv_path)
