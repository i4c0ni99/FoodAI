import pandas as pd
from backtracking import backtracking_search
import os 

def getCsp(protein_g,carb_g,fat_g,aliments):
    
    # Verifica se la differenza tra il target di una macro e la somma dei valori della macro di tutti gli alimenti è minore o uguale di 0.5 grammi
    # Altrimenti, sulla specifica macro, ritorna "false" e la differenza
    def constraint_macro(assignment):
        
        is_consistent = {'carbohydrate': (True,0),'protein': (True,0),'fat': (True,0)}
        
        protein_carbs = assignment['carbohydrate']['protein']
        carb_carbs = assignment['carbohydrate']['carbohydrate']
        fat_carbs = assignment['carbohydrate']['fat']
        
        protein_protein = assignment['protein']['protein']
        carb_protein = assignment['protein']['carbohydrate']
        fat_protein = assignment['protein']['fat']
        
        protein_fat = assignment['fat']['protein'] 
        carb_fat = assignment['fat']['carbohydrate']
        fat_fat = assignment['fat']['fat']
        
        difference_protein = abs( (protein_protein + protein_carbs + protein_fat) -  protein_g)
        difference_carb = abs( (carb_carbs + carb_protein + carb_fat) -  carb_g)
        difference_fat = abs( (fat_carbs + fat_protein + fat_fat) -  fat_g)

        if difference_carb >= 0.5 :
            is_consistent['carbohydrate'] = (False,difference_carb * 10 )
        if difference_protein >= 0.5 :
            is_consistent['protein'] = (False,difference_protein * 10 )
        if difference_fat >= 0.5 :
            is_consistent['fat'] = (False,difference_fat  * 10 ) 
        
        return is_consistent    
    
    
    df = pd.read_csv('/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/updated-trained-data.csv')
    
    file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
    for aliment in aliments:
        if os.path.exists(file_path):
        # Cancella il file
            existing_data = pd.read_csv(file_path)
            filtered_data= df[df['generic_category'] == aliment['category']]
            filtered_data = pd.concat([existing_data, filtered_data])
        else:    
            filtered_data= df[df['generic_category'] == aliment['category']]
        filtered_data.to_csv(file_path, index=False)    
        
    df = pd.read_csv('/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv')    

    # Minimo score per gli alimenti
    df = df[df['nutritional_score'] > 40]    
    
    csp = {
    'variables' : ['carbohydrate', 'protein', 'fat'],
    'domains' : {
        'carbohydrate': pd.DataFrame(df[(df['carb_percentage'] >= 50 )  & (df['carbohydrate'] >= 15 ) & (df['generic_category'] )] ),
        'protein': pd.DataFrame(df[(df['protein_percentage'] >= 70)  & (df['generic_category'] )]),
        'fat': pd.DataFrame(df[(df['fat_percentage'] >= 40)  & (df['generic_category']  )]) 
    },
    'constraints': {
      'macro':lambda  assignment : constraint_macro(assignment),
    }
    }
    
    return backtracking_search(csp,[carb_g,protein_g,fat_g])