from logica_training import matchConstraint
import random


def alimentGranmature(var,max_value,assignment,csp,):
  
    g,val = is_consistent(var,max_value,assignment,csp)
    if val.any and g:
        return g,val
    return None,None   

def is_consistent(var, value, assignment, csp):
    ret_val=value
    val = value['carbohydrate'].iloc[0]
    for constraint in csp['constraints']:
        g,ret_val= constraint(val,ret_val)
        if  g and val.any:
            assignment[var] = val
            return  g,val
    return None,None

def select_unassigned_variable(assignment, csp):
    for var in csp['variables']:
        if var not in assignment:
            return var

def order_domain_values(var, assignment, csp):
    return csp['domains'][var]

def backtrack(assignment, csp):
    if len(assignment) == len(csp['variables']):
        #print(assignment)
        return assignment
    
    var = select_unassigned_variable(assignment, csp)
    value = max(order_domain_values(var,assignment,csp)['carbohydrate'])
    
    max_value = order_domain_values(var,assignment,csp)[order_domain_values(var,assignment,csp)['carbohydrate'] == value] 
    g,aliment = alimentGranmature(var,max_value,assignment,csp) 
    #print(g,aliment)
    #return backtrack({},csp[csp['domains'][var]['carbohydrate'] < value])

   
        
    
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


def backtracking_search(csp):
    return backtrack({}, csp)

# Esecuzione dell'algoritmo

