from csp_diet import getCsp
from csp_aliment_change import getCsp_change_aliment
import os
import json 

def trainerColazione(tdee_meal,aliments,assignment):
    
    protein_kal = tdee_meal * 0.25
    carb_kal=tdee_meal * 0.45
    fat_kal=tdee_meal *0.30 
    
    protein_g = protein_kal / 4
    carb_g = carb_kal / 4
    fat_g= fat_kal / 9
    if assignment:
        result =  getCsp_change_aliment(protein_g,carb_g,fat_g,aliments,assignment)
        file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
        
        # Controlla se il file esiste
        if os.path.exists(file_path):
            # Cancella il file
            os.remove(file_path)
            print(f"File '{file_path}' cancellato con successo.")
        else:
            print(f"Il file '{file_path}' non esiste.")
        return result 
    result =  getCsp(protein_g,carb_g,fat_g,aliments)
    file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
    
    # Controlla se il file esiste
    if os.path.exists(file_path):
        # Cancella il file
        os.remove(file_path)
        print(f"File '{file_path}' cancellato con successo.")
    else:
        print(f"Il file '{file_path}' non esiste.")
    return result 

def trainerSpuntino_mat(tdee_meal,aliments,assignment):
    
    protein_kal = tdee_meal * 0.15
    carb_kal=tdee_meal * 0.60
    fat_kal=tdee_meal *0.25
    
    protein_g = protein_kal / 4
    carb_g = carb_kal / 4
    fat_g= fat_kal / 9
    if assignment:
        result =  getCsp_change_aliment(protein_g,carb_g,fat_g,aliments,assignment)
        file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
        
        # Controlla se il file esiste
        if os.path.exists(file_path):
            # Cancella il file
            os.remove(file_path)
            print(f"File '{file_path}' cancellato con successo.")
        else:
            print(f"Il file '{file_path}' non esiste.")
        return result 
    result =  getCsp(protein_g,carb_g,fat_g,aliments)
    file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
    
    # Controlla se il file esiste
    if os.path.exists(file_path):
        # Cancella il file
        os.remove(file_path)
        print(f"File '{file_path}' cancellato con successo.")
    else:
        print(f"Il file '{file_path}' non esiste.")
    return result 

def trainerPranzo(tdee_meal,aliments,assignment):
    
    protein_kal = tdee_meal * 0.3
    carb_kal=tdee_meal * 0.4
    fat_kal=tdee_meal * 0.3
    
    protein_g = protein_kal / 4
    carb_g = carb_kal / 4
    fat_g= fat_kal / 9
    if assignment:
        result =  getCsp_change_aliment(protein_g,carb_g,fat_g,aliments,assignment)
        file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
        
        # Controlla se il file esiste
        if os.path.exists(file_path):
            # Cancella il file
            os.remove(file_path)
            print(f"File '{file_path}' cancellato con successo.")
        else:
            print(f"Il file '{file_path}' non esiste.")
        return result 
    result =  getCsp(protein_g,carb_g,fat_g,aliments)
    file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
    
    # Controlla se il file esiste
    if os.path.exists(file_path):
        # Cancella il file
        os.remove(file_path)
        print(f"File '{file_path}' cancellato con successo.")
    else:
        print(f"Il file '{file_path}' non esiste.")
    return result 

def trainerSpuntino_pom(tdee_meal,aliments,assignment):
    
    protein_kal = tdee_meal * 0.2
    carb_kal=tdee_meal * 0.5
    fat_kal=tdee_meal *0.3 
    
    protein_g = protein_kal / 4
    carb_g = carb_kal / 4
    fat_g= fat_kal / 9
    if assignment:
        result =  getCsp_change_aliment(protein_g,carb_g,fat_g,aliments,assignment)
        file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
        
        # Controlla se il file esiste
        if os.path.exists(file_path):
            # Cancella il file
            os.remove(file_path)
            print(f"File '{file_path}' cancellato con successo.")
        else:
            print(f"Il file '{file_path}' non esiste.")
        return result 
    result =  getCsp(protein_g,carb_g,fat_g,aliments)
    file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
    
    # Controlla se il file esiste
    if os.path.exists(file_path):
        # Cancella il file
        os.remove(file_path)
        print(f"File '{file_path}' cancellato con successo.")
    else:
        print(f"Il file '{file_path}' non esiste.")
    return result 

def trainerCena(tdee_meal,aliments,assignment):
    
    protein_kal = tdee_meal * 0.3
    carb_kal=tdee_meal * 0.35
    fat_kal=tdee_meal *0.35 
    
    protein_g = protein_kal / 4
    carb_g = carb_kal / 4
    fat_g= fat_kal / 9
    if assignment:
        result =  getCsp_change_aliment(protein_g,carb_g,fat_g,aliments,assignment)
        file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
        
        # Controlla se il file esiste
        if os.path.exists(file_path):
            # Cancella il file
            os.remove(file_path)
            print(f"File '{file_path}' cancellato con successo.")
        else:
            print(f"Il file '{file_path}' non esiste.")
        return result 
    result =  getCsp(protein_g,carb_g,fat_g,aliments)
    file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-for-category.csv'
    
    # Controlla se il file esiste
    if os.path.exists(file_path):
        # Cancella il file
        os.remove(file_path)
        print(f"File '{file_path}' cancellato con successo.")
    else:
        print(f"Il file '{file_path}' non esiste.")
    return result 