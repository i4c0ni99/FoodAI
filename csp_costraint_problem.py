""" from constraint import Problem
import pandas as pd
import os

def search_food_problem(protein_g,carb_g,fat_g,aliments,kal):
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
# Definisci i valori nutrizionali per ciascun alimento (in grammi e calorie)
   

    # Vincoli nutrizionali per il pasto (esempio: 40g di proteine, 50g di carboidrati, 30g di grassi e 700 calorie)
    target_proteine = protein_g
    target_carboidrati = carb_g
    target_grassi = fat_g
    target_calorie = kal

    # Definisci un problema CSP
    problem = Problem()

    # Aggiungi una variabile per ciascun alimento con la sua quantità in grammi (da 0 a 300g per esempio)
    for food in nutritional_values.keys():
        problem.addVariable(food, range(0, 301))

    # Definisci il vincolo sui macronutrienti e calorie
    def nutritional_constraints(**quantities):
        total_protein = sum(quantities[food] * nutritional_values[food]["proteins"] / 100 for food in quantities)
        total_carbs = sum(quantities[food] * nutritional_values[food]["carbs"] / 100 for food in quantities)
        total_fat = sum(quantities[food] * nutritional_values[food]["fats"] / 100 for food in quantities)
        total_calories = sum(quantities[food] * nutritional_values[food]["kal"] / 100 for food in quantities)
        
        # Verifica se i nutrienti rientrano nei target
        return (
            total_protein >= target_proteine and
            total_carbs >= target_carboidrati and
            total_fat >= target_grassi and
            total_calories >= target_calorie
        )

    # Applica il vincolo al problema
    problem.addConstraint(nutritional_constraints)

    # Risolvi il problema
    solution = problem.getSolution()

    # Stampa la soluzione generata
    if solution:
        print("Combinazione di alimenti per un singolo pasto:")
        for food, quantity in solution.items():
            if quantity > 0:  # Mostra solo gli alimenti utilizzati
                print(f"{food}: {quantity}g")
    else:
        print("Nessuna soluzione trovata che rispetti i vincoli nutrizionali.") """


import pandas as pd
import os
from scipy.optimize import minimize
def search_food_problem(protein_g,carb_g,fat_g,aliments,kal):
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
         
    # Obiettivi nutrizionali per un pasto
    target_protein = 40
    target_carbs = 50
    target_fat = 30
    target_calories = 700

    # Numero desiderato di alimenti
    num_selected_foods = 3

    # Numero di alimenti disponibili


         
    print(nutritional_values)    
    # Vincoli sui macronutrienti
    target_carbs = carb_g
    target_proteins = protein_g
    target_fats = fat_g
        
    # 2. Definisci un problema CSP
    print(nutritional_values)
# Definisci i valori nutrizionali per ciascun alimento (in grammi e calorie)
   

    # Vincoli nutrizionali per il pasto (esempio: 40g di proteine, 50g di carboidrati, 30g di grassi e 700 calorie)
    target_proteine = protein_g
    target_carboidrati = carb_g
    target_grassi = fat_g
    target_calorie = kal
    max_food_items = 10
    # Definisci un problema CSP
    # Obiettivi nutrizionali per un pasto


    # Funzione che verifica i vincoli nutrizionali
    def nutritional_constraints(x):
        total_protein = sum([x[i] * nutritional_values[food]["proteins"] for i, food in enumerate(nutritional_values)]) / 100
        total_carbs = sum([x[i] * nutritional_values[food]["carbs"] for i, food in enumerate(nutritional_values)]) / 100
        total_fat = sum([x[i] * nutritional_values[food]["fats"] for i, food in enumerate(nutritional_values)]) / 100
        total_calories = sum([x[i] * nutritional_values[food]["kal"] for i, food in enumerate(nutritional_values)]) / 100
        
        return [
            total_protein - target_proteins,  # Devi raggiungere almeno il target delle proteine
            total_carbs - target_carbs,  # Devi raggiungere almeno il target dei carboidrati
            total_fat - target_fats,  # Devi raggiungere almeno il target dei grassi
            total_calories - kal, # Devi raggiungere almeno il target delle calorie
        ]
        
    # Funzione obiettivo (minimizzare le calorie)
    def objective_function(x):
        return sum([x[i] * nutritional_values[food]["kal"] for i, food in enumerate(nutritional_values)]) / 100

    # Vincoli come funzioni lambda per `scipy.optimize`
    constraints = [
        {'type': 'ineq', 'fun': lambda x: nutritional_constraints(x)[0]},  # Proteine
        {'type': 'ineq', 'fun': lambda x: nutritional_constraints(x)[1]},  # Carboidrati
        {'type': 'ineq', 'fun': lambda x: nutritional_constraints(x)[2]},  # Grassi
        {'type': 'ineq', 'fun': lambda x: nutritional_constraints(x)[3]},  # Calorie
    ]

    # Limiti di quantità per ciascun alimento (0 a 300 grammi)
    bounds = [(0, 300) for _ in nutritional_values]

    # Stima iniziale (ad esempio, 50 grammi per ciascun alimento)
    x0 = [200] * len(nutritional_values)

    # Risolvi il problema di ottimizzazione
    res = minimize(objective_function, x0, method='SLSQP', bounds=bounds, constraints=constraints)

    # Verifica se è stata trovata una soluzione
    if res.success:
        print(res.fun)
        print(kal)
        print("Combinazione di alimenti e quantità per un singolo pasto:")
        for i, food in enumerate(nutritional_values):
            quantity = res.x[i]
            
            if quantity > 0:
                print(f"{food}: {quantity:.2f}g ")
    else:
        print("Nessuna soluzione trovata che rispetti i vincoli nutrizionali.") 