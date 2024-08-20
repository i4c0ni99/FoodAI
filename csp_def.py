
import pandas as pd 
import os
import itertools
# 1. Definisci i valori nutrizionali per ciascun alimento (in grammi e calorie)

def search_food(protein_g,carb_g,fat_g,aliments,kal):
    df = pd.read_csv('/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-file.csv')
        
    file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
    for aliment in aliments:
        print(aliment['category'])
    # Controlla se il file esiste
        if os.path.exists(file_path):
        # Cancella il file
            existing_data = pd.read_csv(file_path)
            filtered_data= df[df['generic_category'] == aliment['category']]
            filtered_data = pd.concat([existing_data, filtered_data])
        else:    
            filtered_data= df[df['generic_category'] == aliment['category']]
        filtered_data.to_csv(file_path, index=False)    
        
    nutritional_values_df = pd.read_csv('/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv')
    nutritional_values_df = nutritional_values_df[nutritional_values_df['feedback'] == 'approvato']
    nutritional_values_df = nutritional_values_df[nutritional_values_df['nutritional_score'] >= 15]
    nutritional_values= {}
    for index, row in nutritional_values_df.iterrows():
         nutritional_values[row['description']] = {'proteins': row['protein'],'fats': row['fat'],'carbs': row['carbohydrate'],'kal': row['kilocalories'] } 
         
    print(nutritional_values)    
    # Vincoli sui macronutrienti
    target_carbs = carb_g
    target_proteins = protein_g
    target_fats = fat_g
        
    # 2. Definisci un problema CSP
    print(nutritional_values)
    
    def generate_combinations():
        quantities = list(range(0, 300, 50 ))  # Quantità da 0 a 300 grammi con passo di 100g
        return itertools.product(quantities, repeat=len(nutritional_values))

    # Verifica se una combinazione soddisfa i vincoli nutrizionali
    def satisfies_constraints(combination):
        total_protein = 0
        total_carbs = 0
        total_fat = 0
        total_calories = 0

        
        quantity = combination[i]
        total_protein += quantity * nutritional_values[food]["proteins"] / 100
        total_carbs += quantity * nutritional_values[food]["carbs"] / 100
        total_fat += quantity * nutritional_values[food]["fats"] / 100
        total_calories += quantity * nutritional_values[food]["kal"] / 100
        print([total_calories,total_carbs,total_fat,total_protein,food])

        if total_protein >= target_proteins and total_carbs >= target_carbs and total_fat >= target_fats and total_calories >= kal:
            return combination
    # Trova una combinazione valida
    def find_valid_combination():
        i=0
        for combination in generate_combinations():
            """
            print(combination)
            i+=1
            if i == 10000:
                break """
            if satisfies_constraints(combination):
                return combination
        return None

    # Ottieni una soluzione valida
    solution = find_valid_combination()

    # Stampa la soluzione
    if solution:
        print("Combinazione di alimenti e quantità per un singolo pasto:")
        for i, food in enumerate(nutritional_values):
            quantity = solution[i]
            if quantity > 0:
                print(f"{food}: {quantity}g")
    else:
        print("Nessuna soluzione trovata che rispetti i vincoli nutrizionali.")