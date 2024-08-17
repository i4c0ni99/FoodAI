
def alimentGranmature(var,max_value,assignment,csp,):
    is_consistent(var,max_value,assignment,csp)
      

def is_consistent(var, value, assignment, csp):
    ret_val=value
    val = value['carbohydrate'].iloc[0]
    
    for constraint in csp['constraints']:
        
        g,ret_val= constraint(val,ret_val)
        
        if  g is not None and ret_val is not None:
            assignment[var] = { 'aliment ': ret_val.to_dict(orient="records"),'grams': g}
            return  g,val
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
        
        return assignment
    
    var = select_unassigned_variable(assignment, csp)
    value = max(order_domain_values(var,assignment,csp)['carbohydrate'])
    
    max_value = order_domain_values(var,assignment,csp)[order_domain_values(var,assignment,csp)['carbohydrate'] == value] 
    alimentGranmature(var,max_value,assignment,csp) 
    return backtrack(assignment,csp)
    

   
        
    
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

