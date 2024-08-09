from logica_training import matchConstraint
import random

def is_consistent(var, value, assignment, csp):
    assignment[var] = value[var]
    for constraint in csp['constraints']:
        if not constraint(value[var]):
            del assignment[var]
            return False
    del assignment[var]
    return True

def select_unassigned_variable(assignment, csp):
    for var in csp['variables']:
        if var not in assignment:
            return var

def order_domain_values(var, assignment, csp):
    return csp['domains'][var]

def backtrack(assignment, csp):
    if len(assignment) == len(csp['variables']):
        return assignment
    
    var = select_unassigned_variable(assignment, csp)
    all_indices = list(range(len(order_domain_values(var,assignment,csp))))
    
   
    counter = 0
    while counter <= 500 :
        combination= random.sample(all_indices,50)
        selected_data = order_domain_values(var, assignment, csp).iloc[combination]
        value=matchConstraint(selected_data)
        if is_consistent(var, value, assignment, csp) :
            print(value)
            assignment[var] = value
            result = backtrack(assignment, csp)
            print(result)
            if result is not None:
                    return result
            del assignment[var] 
        counter +=1


def backtracking_search(csp):
    return backtrack({}, csp)

# Esecuzione dell'algoritmo

