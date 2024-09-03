
import pandas as pd
import random

targhetMacro = {}


def alimentGranmature(ret_val,val,var,g):
    
    current_var = ret_val[var].iloc[0] # Ottieni il valore corrente di grassi
    
    if abs(targhetMacro[var] - current_var) <= 0.5 :
        #if var == 'carbohydrate' and g >= 50 and g <= 200 or var == 'protein' and g >= 50 and g <= 300 or var == 'fat' and g >= 0 and g <= 30 :
            ret_val['protein'] = (g/100)  * val['protein'].iloc[0]
            ret_val['fat'] = (g/100) * val['fat'].iloc[0]
            ret_val['carbohydrate'] = (g/100) * val['carbohydrate'].iloc[0]
            kilo_carb= ret_val['carbohydrate'] * 4
            kilo_prot = ret_val['protein'] * 4
            kilo_fat = ret_val['fat'] * 9
            ret_val['kilocalories'] = kilo_carb + kilo_fat + kilo_prot
            print(ret_val.to_dict(orient="records"))
            return ret_val,g
    if current_var < targhetMacro[var]:
        print(var,val[var])
        ret_val[var] = (g + 0.5 ) / 100 * val[var].iloc[0]
        return alimentGranmature( ret_val,val,var,g + 0.5)
    if current_var > targhetMacro[var]:
        ret_val[var]= (g - 0.5) / 100 * val[var].iloc[0]
        return alimentGranmature(ret_val,val,var,g - 0.5)
    return ret_val,g                                    
    
            
def change_grams_aliment(aliment,difference):
    if(difference < aliment['grams']):
        aliment['grams'] -= difference
        aliment['carbohydrate'] *= aliment['grams'] / 100 
        aliment['protein'] *=   aliment['grams'] / 100 
        aliment['fat']  *=   aliment['grams'] / 100 
    else :
        aliment['grams'] = 0
        aliment['carbohydrate'] *= aliment['grams'] / 100 
        aliment['protein'] *=   aliment['grams'] / 100 
        aliment['fat']  *=   aliment['grams'] / 100 
    return aliment
def is_consistent(assignment, csp):
    

    constraint = csp['constraints']['macro'](assignment)
    if  constraint is not None :
          return constraint

    return None,None

def select_unassigned_variable(assignment, csp):
    for var in csp['variables']:
        if var not in assignment:
            print(var)
            return var

def order_domain_values(var, assignment, csp):
    return csp['domains'][var]

def backtrack(assignment, csp):

    if len(assignment) == len(csp['variables']):
        constraint = is_consistent(assignment,csp)
        if constraint is not None:
            for item in constraint:
                print(constraint[item][0])
                if not constraint[item][0]:
                    print('entro 1')
                    assignment[item] = change_grams_aliment(assignment[item],constraint[item][1])#creare ricorsione con programmazione dinamica
                    constraint =  is_consistent(assignment,csp)
                    if constraint[item][0]:
                        print('entro')
                        return backtrack(assignment,csp)
        return assignment
    
    var = select_unassigned_variable(assignment, csp)
    
    # Valori massimi per macro
    #max_nutrient_food = 
    
    
    # Filtra i valori presi
    value= order_domain_values(var, assignment, csp)
    ret_val =  value.sample(1)                   
    
                         
    
    
    
    ret_val,g = alimentGranmature(ret_val=ret_val, val=ret_val.copy(),var=var,g=100)
    dict_aliment = ret_val.to_dict(orient="records")
    print('QUESTO E L ALIMENTO RITORNATO')
    print(dict_aliment)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    """ carbohydrate: {
            original_category: string, category: string, description: string,
            carbohydrate: number, protein: number, fat: number, kilocalories: number, feedback: string, generic_category: string, grams: number
        }, """
    assignment[var] = { 'original_category': dict_aliment[0]['original_category'], 'category': dict_aliment[0]['category'], 'description' : dict_aliment[0]['description'], 'carbohydrate': dict_aliment[0]['carbohydrate'],'protein':
        dict_aliment[0]['protein'],'fat' :dict_aliment[0]['fat'],'kilocalories':dict_aliment[0]['kilocalories'],'feedback':dict_aliment[0]['feedback'],'generic_category': dict_aliment[0]['generic_category'], 'grams' : g }
   
    
    return backtrack(assignment, csp)

   
        
    
    """   counter = 0
    while counter <= 500 :
        combination= random.sample(all_indices,50)
        selected_data = order_domain_values(var, assignment, csp).iloc[combination]
        value=matchConstraint(selected_data)
        if is_consistent(var, value, assignment, csp):
            print(value)
            assignment[var] = value
            result = backtrack(assignment, csp)
            print(result)
            if result is not None:
                    return result
            del assignment[var] 
        counter +=1 """


def backtracking_search(csp,target_g):
    global targhetMacro
    targhetMacro={'carbohydrate':target_g[0],'protein': target_g[1],'fat':[2]}    
    return backtrack({}, csp)

# Esecuzione dell'algoritmo

