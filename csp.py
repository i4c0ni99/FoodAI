import pandas as pd
from logica_training import find_best_combination

def backtracking_search(csp):
    return backtrack({}, csp)

def backtrack(assignment, csp):
    # Se tutte le variabili sono assegnate, abbiamo trovato una soluzione
    if len(assignment) == len(csp['variables']):
        return assignment
    
    
    # Scegliere una variabile non assegnata
    var = select_unassigned_variable(assignment, csp)
    
    
    # Provare ogni valore nel dominio della variabile scelta
    for value in order_domain_values(var,csp):
        # Se il valore è consistente con l'assegnazione attuale
        if is_consistent(var, value, assignment, csp):
            # Aggiungere {var: value} all'assegnazione
            assignment[var] = value
            
            # Procedere con l'assegnazione successiva
            result = backtrack(assignment, csp)
            if result:
                return result
            
            # Se non porta a una soluzione, rimuovere l'assegnazione (backtrack)
            del assignment[var]
    
    return None  # Trigger backtracking

def select_unassigned_variable(assignment, csp):
    
    for var in csp['variables']:
        if var not in assignment:
            print('entro nel select unasigned')
            return var
                
                

def order_domain_values(var, csp):
    print('entro order_domani')
    print(csp['domains'][var])
    return csp['domains'][var]

def is_consistent(var, value, assignment, csp):
    
    for constraint in csp['constraints']:

        if not constraint(var, value, assignment):
            return False
    return True



    

       
        
    return csp

