from logica_training import find_best_combination
def trainerPranzo(tdee_pranzo):
    protein_kal = tdee_pranzo * 0.3
    carb_kal=tdee_pranzo * 0.5
    fat_kal=tdee_pranzo *0.2 
    
    protein_g = protein_kal / 4
    carb_g = carb_kal / 4
    fat_g= fat_kal / 9
    
    return find_best_combination(protein_g, fat_g, carb_g,5000,3)
    