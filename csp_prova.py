import pandas as pd
from backtracking import backtracking_search

def getCsp(protein_g,carb_g,fat_g):

    df = pd.read_csv('/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-file.csv')
    # Definizione degli alimenti con i relativi macronutrienti
   

    # Vincoli sui macronutrienti
    target_carbs = carb_g
    target_proteins = protein_g
    target_fats = fat_g
    
    # Variabili
   
 
    # Vincoli
    def constraint_carb(target_carbs,g,val,ret_val):
        print('!!!!!!!!!!!!!!!!!!!!!!!!VAL:',val )
        print('!!!!!!!!!!!!!!!!!!!!!!!!RET_VAL:',ret_val['carbohydrate'].iloc[0])
        if ret_val['carbohydrate'].iloc[0] == target_carbs :
            #print("sono entrato ma non voglio")
            #print(val['carbohydrate'].iloc[0])
            return g,ret_val
        if ret_val['carbohydrate'].iloc[0] < target_carbs:
            print(" sono entrato ")
            #print(val['carbohydrate'].iloc[0])
            g+=0.1
            ret_val['carbohydrate'] = (g/100 ) * val 
            #print( ret_val['carbohydrate'].iloc[0] )
            return constraint_carb(target_carbs,g,val,ret_val)
        if ret_val['carbohydrate'].iloc[0] > target_carbs:
            print(" sono entrato 2")
            #print(val['carbohydrate'].iloc[0])
            g-=0.1
            ret_val['carbohydrate'] = (g/100 ) * val
            #print( ret_val['carbohydrate'].iloc[0] )
            return constraint_carb(target_carbs,g ,val,ret_val)
         
        return constraint_carb(target_carbs,g,val,ret_val)

    def constraint_protein(target_proteins,g,val):
        for food in df['protein']: 
            if food == target_proteins:
                return True
        return False   

    def constraint_fat(target_fats,g,val):
        for food in df['fat']:
            if food == target_fats:
                return True
        return False   

   

    df = pd.read_csv('/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-file.csv')
    csp = {
    'variables': ['carbs','proteins'],
    'domains': {
        'carbs': pd.DataFrame(df[df['carbohydrate'] >= 35]),
        #'proteins': df[df['protein'] >= 45],
        #'fats': df[df['fat'] >= 35]
    },
    'constraints': [
        lambda  val,ret_val : constraint_carb(target_carbs,100,val,ret_val),
        #lambda  val: constraint_protein(target_proteins,100,val),
        #lambda  val: constraint_fat(target_fats,100,val),
    ]}

    return backtracking_search(csp)