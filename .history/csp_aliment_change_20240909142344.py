import pandas as pd
from backtracking import backtracking_changeAliment
import os 

# Viene chiamato quando è premuto il bottone dislike, sostituisce un alimento dell'assignment
def getCsp_change_aliment(protein_g,carb_g,fat_g,aliments,assignment):
    
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
            is_consistent['carbohydrate'] = (False,difference_protein * 10)
        # Le proteine sono meno presenti negli altri alimenti, quindi la condizione si avvera raramente e la moltiplicazione non è necessaria
        if difference_protein >= 0.5 :
            is_consistent['protein'] = (False,difference_protein)
        if difference_fat >= 0.5 :
            is_consistent['fat'] = (False,difference_protein * 10) 
                   
        return is_consistent    
    
    
    df = pd.read_csv('/Users/lucavisconti/Documents/FoodAI/csv/updated-trained-data.csv')
    
    file_path = '/Users/lucavisconti/Documents/FoodAI/csv/training-for-category.csv'
    for aliment in aliments:
    # Controlla se il file esiste
        if os.path.exists(file_path):
        # Cancella il file
            existing_data = pd.read_csv(file_path)
            filtered_data= df[df['generic_category'] == aliment['category']]
            filtered_data = pd.concat([existing_data, filtered_data])
        else:    
            filtered_data= df[df['generic_category'] == aliment['category']]
        filtered_data.to_csv(file_path, index=False)    
        
    df = pd.read_csv('/Users/lucavisconti/Documents/FoodAI/csv/training-for-category.csv')   
     
    # Vincoli sui macronutrienti
    df = df[df['nutritional_score'] > 40]    
    
    csp = {
    'variables' : ['carbohydrate', 'protein', 'fat'],
    'domains' : {
        'carbohydrate': pd.DataFrame(df[(df['carb_percentage'] >= 50 )  & (df['carbohydrate'] >= 15 ) & (df['generic_category'] != 'vegetables' )] ),
        'protein': pd.DataFrame(df[(df['protein_percentage'] >= 70)  & (df['generic_category'] != 'vegetables' )]),
        'fat': pd.DataFrame(df[(df['fat_percentage'] >= 40)  & (df['generic_category'] != 'vegetables' )]) 
    },
    'constraints': {
      'macro':lambda  assignment : constraint_macro(assignment),
    }
    }
    
    return backtracking_changeAliment(csp,[carb_g,protein_g,fat_g],assignment)