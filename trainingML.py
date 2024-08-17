from logica_training import find_best_combination
from dataset_maker import filter_csv_by_category
from csp_prova import getCsp
import os
import json 
def trainerPranzo(tdee_pranzo,aliments):
    
    protein_kal = tdee_pranzo * 0.3
    carb_kal=tdee_pranzo * 0.5
    fat_kal=tdee_pranzo *0.2 
    
    protein_g = protein_kal / 4
    carb_g = carb_kal / 4
    fat_g= fat_kal / 9
    result =  getCsp(protein_g,carb_g,fat_g)
    print(result)
 
    return result
    """  print('carbs',carb_g)
    #filter_csv_by_category(aliments)
    
    print('soluzione trovata')
    print(result[1])
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print('Grammi totali',result[0]) """
    # Specifica il percorso del file da cancellare
    """ file_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/prepared-food-data-for-category.csv'

    # Controlla se il file esiste
    if os.path.exists(file_path):
        # Cancella il file
        os.remove(file_path)
        print(f"File '{file_path}' cancellato con successo.")
    else:
        print(f"Il file '{file_path}' non esiste.")
    return result
     """