import pandas as pd
from backtracking import backtracking_search
from dataset_maker import filter_csv_by_category
import os 

def getCsp(protein_g,carb_g,fat_g,aliments):

    
    # Definizione degli alimenti con i relativi macronutrienti
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
        
    df = pd.read_csv('/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv')    
    # Vincoli sui macronutrienti
    df = df[df['nutritional_score'] > 40]
    target_carbs = carb_g
    target_proteins = protein_g
    target_fats = fat_g
    
    # Variabili
   
 
    # Vincoli
    def constraint_carb(g,val,ret_val):
        global target_carbs
        global target_fats
        global target_proteins
        
        current_carbs = ret_val[0]['carbohydrate'].iloc[0]  # Ottieni il valore corrente di carboidrati
        print("carboidrati masselli")
        """   print(f"Peso corrente (g): {g}")
                print(f"Valore attuale dei carboidrati: {current_carbs}")
                print(f"Target carboidrati: {target_carbs}")
        """
        if abs(current_carbs - target_carbs) <= 0.5 :  # Controllo se il valore corrente è abbastanza vicino al target
            #print("Target raggiunto o abbastanza vicino.")
            #print(ret_val)
            """ sum_macro_1 = ret_val[1]['protein'].iloc[0] + ret_val[1]['fat'].iloc[0]
            sum_macro_2 = ret_val[2]['protein'].iloc[0] +ret_val[2]['fat'].iloc[0]
            sum_macro_target= target_proteins + target_fats
            if abs( sum_macro_1 - sum_macro_target) > abs( sum_macro_2 - sum_macro_target) :
                print("MEVDA")
                
                g_prot,ret_val=constraint_prot(100,ret_val[1]['protein'].iloc[0],ret_val[1]['fat'].iloc[0],ret_val)
                ret_val= [ret_val[0],ret_val[1]]
                print([target_carbs,target_fats,target_proteins])
                print('!!!!!!!!!!!!!!!!!!!!!!!!!')
                print(g_prot)
                print(ret_val)
            if abs( sum_macro_1 - sum_macro_target) < abs( sum_macro_2 - sum_macro_target) :
                print("MEVDA2") """
            ret_val['protein']*= (g/100) 
            ret_val['fat']*= (g/100)
            kilo_carb= current_carbs * 4
            kilo_prot = ret_val['protein'] * 4
            kilo_fat = ret_val['fat'] * 9
            ret_val['kilocalories'] = kilo_carb + kilo_fat + kilo_prot
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            print(g)
            print(ret_val)
            return g, ret_val

        if current_carbs < target_carbs:
            #print("Aumentando il peso...")
            new_carbs = (g + 0.5) / 100 * val
            ret_val[0]['carbohydrate'] = new_carbs
            #print(ret_val)
            return constraint_carb( g + 0.5, val, ret_val)

        if current_carbs > target_carbs:
            #print("Diminuisco il peso...")
            new_carbs = (g - 0.5) / 100 * val
            ret_val[0]['carbohydrate'] = new_carbs
            return constraint_carb(g - 0.5, val, ret_val)

        # In caso di errore, ritorno i valori attuali senza modifiche
        print("Errore nella regolazione dei carboidrati.")
        return g, ret_val


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
        
  # Vincoli su protein
    def constraint_prot(g,val_prot,val_fat,ret_val):
        current_protein = ret_val[1]['protein'].iloc[0]+ret_val[0]['protein'].iloc[0]  # Ottieni il valore corrente di carboidrati
        current_fat = ret_val[1]['fat'].iloc[0] + ret_val[0]['fat'].iloc[0]
        print("cicciaaaaaaaa")
        

        if abs((current_protein + current_fat) - (target_proteins + target_fats)) <= 0.5:  # Controllo se il valore corrente è abbastanza vicino al target
            #print("Target raggiunto o abbastanza vicino.")
            #print(ret_val)
            
            return g, ret_val

        if (current_protein + current_fat) < (target_proteins + target_fats):
            #print("Aumentando il peso...")
            ret_val[1]['protein'] = (g + 0.5) / 100 * val_prot
            ret_val[1]['fat'] = (g + 0.5) / 100 * val_fat
            
            #print(ret_val)
            return constraint_prot( g + 0.5, val_prot,val_fat, ret_val)

        if (current_protein + current_fat) > (target_proteins + target_fats):
            #print("Diminuisco il peso...")
            ret_val[1]['protein'] = (g - 0.5) / 100 * val_prot
            ret_val[1]['fat'] = (g - 0.5) / 100 * val_fat
            return constraint_prot(g - 0.5, val_prot,val_fat, ret_val)

        # In caso di errore, ritorno i valori attuali senza modifiche
        print("Errore nella regolazione dei carboidrati.")
        return g, ret_val
        
        """ 
        print("cicciaaaaaaaa")
        current_proteins = ret_val['protein'].iloc[0]  # Ottieni il valore corrente di proteine

        if abs(current_proteins - target_proteins) <= 0.5:
            
            return g, ret_val
        
        if current_proteins < target_proteins:
            
            new_proteins = (g + 0.5 / 100) * val
            ret_val['protein'] = new_proteins
            return constraint_prot(target_proteins, g + 0.5, val, ret_val)
        
        if current_proteins > target_proteins:
            
            new_proteins = (g - 0.5 / 100) * val
            ret_val['protein'] = new_proteins
            return constraint_prot(target_proteins, g - 0.5, val, ret_val)
        
        return g, ret_val
     """
     # Vincoli su fat
    def constraint_fat( g, val, ret_val):
        print("grassi buon")
        current_fats = ret_val['fat'].iloc[0]  # Ottieni il valore corrente di grassi

        if abs(target_fats - current_fats) <= 0.5 :
            return g,ret_val
        if current_fats < target_fats :
            ret_val['fat'] = (g + 0.5  ) / 100 * val
            return constraint_fat(target_fats,g + 0.5,val,ret_val)
        if current_fats > target_fats :
            ret_val['fat']= (g - 0.5) / 100 * val 
            return constraint_fat(target_fats,g - 0.50,val,ret_val)
        return g,ret_val
    
    
    csp = {
    'variables' : ['carbohydrate', 'protein', 'fat'],
    'domains' : {
        'carbohydrate': pd.DataFrame(df[(df['carb_percentage'] >= 50 ) & (df['feedback'] == 'approvato' )]),
        'protein': pd.DataFrame(df[(df['protein_percentage'] >= 70)  & (df['feedback'] == 'approvato' )]),
        'fat': pd.DataFrame(df[(df['fat_percentage'] >= 40) & (df['feedback'] == 'approvato' )]) 
    },
    'constraints': {
      'carbohydrate':lambda  val,ret_val : constraint_carb(100,val,ret_val),
      'protein':  lambda  val_prot,val_fat,ret_val: constraint_prot(100,val_prot,val_fat,ret_val),
        'fat': lambda  val,ret_val: constraint_fat(100,val,ret_val)
    }
    }

    return backtracking_search(csp)