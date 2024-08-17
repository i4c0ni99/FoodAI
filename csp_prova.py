import pandas as pd
from backtracking import backtracking_search

def getCsp(protein_g,carb_g,fat_g):

    df = pd.read_csv('/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-file.csv')
    # Definizione degli alimenti con i relativi macronutrienti
   
    df.to_numpy
    # Vincoli sui macronutrienti
    target_carbs = carb_g
    target_proteins = protein_g
    target_fats = fat_g
    
    # Variabili
   
 
    # Vincoli
    def constraint_carb(target_carbs,g,val,ret_val):
        
        current_carbs = ret_val['carbohydrate'].iloc[0]  # Ottieni il valore corrente di carboidrati

        print(f"Peso corrente (g): {g}")
        print(f"Valore attuale dei carboidrati: {current_carbs}")
        print(f"Target carboidrati: {target_carbs}")

        if abs(current_carbs - target_carbs) <= 0.5:  # Controllo se il valore corrente è abbastanza vicino al target
            print("Target raggiunto o abbastanza vicino.")
            print(ret_val)
            return g, ret_val

        if current_carbs < target_carbs:
            print("Aumentando il peso...")
            new_carbs = (g + 0.5) / 100 * val
            ret_val['carbohydrate'] = new_carbs
            print(ret_val)
            return constraint_carb(target_carbs, g + 0.5, val, ret_val)

        if current_carbs > target_carbs:
            print("Diminuisco il peso...")
            new_carbs = (g - 0.5) / 100 * val
            ret_val['carbohydrate'] = new_carbs
            return constraint_carb(target_carbs, g - 0.5, val, ret_val)

        # In caso di errore, ritorno i valori attuali senza modifiche
        print("Errore nella regolazione dei carboidrati.")
        return g, ret_val[1]


        """ print('G:',g)
        print('!!!!!!!!!!!!!!!!!!!!!!!!VAL:',val)
        print('!!!!!!!!!!!!!!!!!!!!!!!!RET_VAL:',ret_val['carbohydrate'].iloc[0])
        if ret_val['carbohydrate'].item() - 0.5 == target_carbs or ret_val['carbohydrate'].item() + 0.5 == target_carbs  :
            print("sono entrato ma non voglio")
            print(val)
            return g,ret_val
        if ret_val['carbohydrate'].item() < target_carbs:
            print(" sono entrato ")
            g += 0.5
            ret_val['carbohydrate'] = (g/100 ) * val 
        if ret_val['carbohydrate'].item() > target_carbs:
            print(" sono entrato 2")
            #print(val['carbohydrate'].iloc[0])
            g-=0.5
            ret_val['carbohydrate'] = (g/100 ) * val
            #print( ret_val['carbohydrate'].iloc[0] )
        
        return constraint_carb(target_carbs,g,val,ret_val) """
        

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
    'variables': ['carbs'],
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