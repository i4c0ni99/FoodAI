
import pandas as pd
import random

targhetMacro = {}
import sys
sys.setrecursionlimit(100000) # Limite ricorsioni

# Cambia il peso dell'alimento in input, aggiornando i macronutrienti (fino a raggiungimento del target)
def alimentGranmature(ret_val,val,var,g):
    
    current_var = ret_val[var].iloc[0] # Ottieni il valore corrente di macro
    
    # La differenza è maggiore di 0.5 grammi quindi aggiorno le grammature
    if abs(targhetMacro[var] - current_var) <= 0.5 :
            ret_val['protein'] = (g/100)  * val['protein'].iloc[0]
            ret_val['fat'] = (g/100) * val['fat'].iloc[0]
            ret_val['carbohydrate'] = (g/100) * val['carbohydrate'].iloc[0]
            kilo_carb= ret_val['carbohydrate'] * 4
            kilo_prot = ret_val['protein'] * 4
            kilo_fat = ret_val['fat'] * 9
            ret_val['kilocalories'] = kilo_carb + kilo_fat + kilo_prot
            return ret_val,g
    # Se il valore corrente della macro è minore del target macro, incremento la grammatura 
    if current_var < targhetMacro[var]:
        ret_val[var] = (g + 0.5 ) / 100 * val[var].iloc[0]
        
        return alimentGranmature( ret_val,val,var,g + 0.5)
    
    # Se il valore corrente della macro è maggiore del target macro, decremento la grammatura 
    if current_var > targhetMacro[var]:
        ret_val[var]= (g - 0.5) / 100 * val[var].iloc[0]
        
        return alimentGranmature(ret_val,val,var,g - 0.5)
    return ret_val,g                                    
    
# E' richiamato dopo isConsistent e diminuisce i valori delle macro di un alimento della differenza in input            
def change_grams_aliment(aliment,difference):
    aliment_change = aliment.copy()
    if(difference < aliment['grams']):
        
        carbs= (aliment['carbohydrate']/aliment['grams']  ) * 100 
        prot = ( aliment['protein']/aliment['grams']  ) * 100 
        fat = ( aliment['fat']/aliment['grams']  ) * 100 
        aliment['grams'] -= difference
        
        aliment['carbohydrate'] = ( aliment['grams'] / 100 ) * carbs
        
        aliment['protein'] =   (aliment['grams'] / 100 ) * prot
        
        aliment['fat']  =   (aliment['grams'] / 100)  * fat
        
        aliment['kilocalories'] =  aliment['carbohydrate'] * 4 + aliment['protein'] * 4 + aliment['fat'] * 9 
        
    else :
        aliment['grams'] = 0
        aliment['carbohydrate'] *= aliment['grams'] / 100 
        aliment['protein'] *=   aliment['grams'] / 100 
        aliment['fat']  *=   aliment['grams'] / 100 
    return aliment

# Funzione chiamata per validare la scelta dell'alimento e i valori delle macro rispetto ai target
def is_consistent(assignment, csp):
    constraint = csp['constraints']['macro'](assignment)
    if  constraint is not None :
          return constraint

    return None,None


# Seleziona una variabile che non è stata ancora inserita in assignment
def select_unassigned_variable(assignment, csp):
    for var in csp['variables']:
        if var not in assignment:
            return var

# Restituisce il dominio del CSP in base alla variabile data in input
def order_domain_values(var, csp):
    return csp['domains'][var]

# Funzione che prende in maniera randomica un alimento per volta, fino al raggiungimento della dimensione di assignment
# Questo metodo viene richiamato fintantoché il 
def backtrack(assignment, csp):

    if len(assignment) == len(csp['variables']):
        constraint = is_consistent(assignment,csp)
        if constraint is not None:
            for item in constraint:
                if constraint[item][0] == False:
                    assignment[item] = change_grams_aliment(assignment[item].copy(),constraint[item][1])
                    constraint =  is_consistent(assignment,csp)
                
                    
        return assignment
    
    var = select_unassigned_variable(assignment, csp)
    
    # Valori massimi per macro
    #max_nutrient_food = 
    
    
    # Filtra i valori presi
    value= order_domain_values(var, csp)
    choice_val =  value.sample(1)                   
    
    ret_val,g = alimentGranmature(ret_val=choice_val.copy(), val=choice_val.copy(),var=var,g=100)
    dict_aliment = ret_val.to_dict(orient="records")
    assignment[var] = {  'category': dict_aliment[0]['category'], 'description' : dict_aliment[0]['description'], 'carbohydrate': dict_aliment[0]['carbohydrate'],'protein':
        dict_aliment[0]['protein'],'fat' :dict_aliment[0]['fat'],'kilocalories':dict_aliment[0]['kilocalories'],'generic_category': dict_aliment[0]['generic_category'], 'grams' : g }
   
    return backtrack(assignment, csp)

   



def backtracking_search(csp,target_g):
    global targhetMacro
    targhetMacro={'carbohydrate':target_g[0],'protein': target_g[1],'fat':target_g[2]}    
    return backtrack({}, csp)

def backtracking_changeAliment(csp,target_g,assignment):
    global targhetMacro
    targhetMacro={'carbohydrate':target_g[0],'protein': target_g[1],'fat':target_g[2]}    
    return backtrack(assignment, csp)
# Esecuzione dell'algoritmo

