import random
import csv
from trainingML import trainerColazione, trainerSpuntino_mat, trainerPranzo, trainerSpuntino_pom, trainerCena
import json
import sys

# Funzione per selezionare casualmente almeno 5 categorie di alimenti
sys.setrecursionlimit(10000)
def get_random_categories(mock_data, min_categories=5):
    selected_categories = random.sample(mock_data, k=random.randint(min_categories, len(mock_data)))
    return [item["category"] for item in selected_categories]

def calculate_macronutrients(eta, altezza, peso, obbiettivo, stile_di_vita, numero_di_pasti):
    activity_factors = {
        'sedentario': 1.0,
        'attivo': 1.55,
        'molto attivo': 1.75
    }
    activity_factor = activity_factors.get(stile_di_vita, 1.0)

    bmr = 10 * peso + 6.25 * altezza - 5 * eta + 5
    tdee = bmr * activity_factor

    if obbiettivo == 'dimagrimento':
        tdee -= 500
        if stile_di_vita == 'sedentario':
            carb_percentage, protein_percentage, fat_percentage = 0.3, 0.4, 0.3
        elif stile_di_vita == 'attivo':
            carb_percentage, protein_percentage, fat_percentage = 0.35, 0.4, 0.25
        elif stile_di_vita == 'molto attivo':
            carb_percentage, protein_percentage, fat_percentage = 0.40, 0.35, 0.25
        else:
            raise ValueError("Livello di attività non valido")
    elif obbiettivo == 'mantenimento':
        if stile_di_vita == 'sedentario':
            carb_percentage, protein_percentage, fat_percentage = 0.45, 0.30, 0.20
        elif stile_di_vita == 'attivo':
            carb_percentage, protein_percentage, fat_percentage = 0.50, 0.25, 0.25
        elif stile_di_vita == 'molto attivo':
            carb_percentage, protein_percentage, fat_percentage = 0.50, 0.25, 0.25
        else:
            raise ValueError("Livello di attività non valido")
    elif obbiettivo == 'massa':
        tdee += 500
        if stile_di_vita == 'sedentario':
            carb_percentage, protein_percentage, fat_percentage = 0.5, 0.3, 0.2
        elif stile_di_vita == 'attivo':
            carb_percentage, protein_percentage, fat_percentage = 0.55, 0.30, 0.15
        elif stile_di_vita == 'molto attivo':
            carb_percentage, protein_percentage, fat_percentage = 0.55, 0.30, 0.15
        else:
            raise ValueError("Livello di attività non valido")
    else:
        raise ValueError("Obiettivo non valido")

    protein_g = protein_percentage * tdee / 4
    carb_g = carb_percentage * tdee / 4
    fat_g = fat_percentage * tdee / 9

    pasti = {}
    if numero_di_pasti == 5:
        pasti['colazione'] = tdee * 0.20
        pasti['spuntino_mat'] = tdee * 0.07
        pasti['pranzo'] = tdee * 0.35
        pasti['spuntino_pom'] = tdee * 0.08
        pasti['cena'] = tdee * 0.30
    else:
        raise ValueError("Numero pasti non consentito")

    return tdee, protein_g, carb_g, fat_g, pasti

mock_data = [
    {"name": "Latticini", "category": "dairy"},
    {"name": "Uova", "category": "eggs"},
    {"name": "zuppe e salse", "category": "soupsSauces"},
    {"name": "Oli e grassi", "category": "oilsFats"},
    {"name": "Avicoli", "category": "poultry"},
    {"name": "Carne", "category": "meats"},
    {"name": "Cereali", "category": "cereals"},
    {"name": "Frutta", "category": "fruits"},
    {"name": "Verdura", "category": "vegetables"}
]

num_simulations = 100  # customizzabile

csv_data = []
pasti_formattati = []
for i in range(1, num_simulations + 1):
    eta = random.randint(18, 80)
    altezza = random.randint(150, 200)
    peso = random.randint(50, 120)
    obbiettivo = random.choice(['dimagrimento', 'mantenimento', 'massa'])
    stile_di_vita = random.choice(['sedentario', 'attivo', 'molto attivo'])
    categorie = get_random_categories(mock_data)

    tdee, protein_g, carb_g, fat_g, pasti = calculate_macronutrients(eta, altezza, peso, obbiettivo, stile_di_vita, 5)

    alimenti = [{"category": categoria} for categoria in categorie]

    colazione_result = trainerColazione(pasti['colazione'], alimenti,None)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','block 1')
    spuntino_mattina_result = trainerSpuntino_mat(pasti['spuntino_mat'], alimenti,None)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','block 2')
    pranzo_result = trainerPranzo(pasti['pranzo'], alimenti,None)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','block 3')
    spuntino_pomeriggio_result = trainerSpuntino_pom(pasti['spuntino_pom'], alimenti,None)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','block 4')
    cena_result = trainerCena(pasti['cena'], alimenti,None)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!','block 5')
    
    file_path = '/Users/lucavisconti/Documents/FoodAI/json/output.json'
    
    pasti_formattati.append({'user'+ str(i) :{'kal':tdee,'protein': protein_g,'carb': carb_g, 'fat':fat_g},'meal': {'colazione':colazione_result, 'spuntino_mattina':spuntino_mattina_result,'pranzo': pranzo_result, 'spuntino_pom': spuntino_pomeriggio_result, 'cena':cena_result}})
with open(file_path, 'w') as file:
    json.dump(pasti_formattati, file, indent=4) 
    """ for result in [colazione_result, spuntino_mattina_result, pranzo_result, spuntino_pomeriggio_result, cena_result]:
       
        formatted_result = [f"{alimento['carbohydrat']['description']}:{alimento['carbohydrat']['quantity']}g" for alimento in result]
       
        pasti_formattati.append(formatted_result)

    csv_data.append([i, eta, peso, altezza, obbiettivo, stile_di_vita, tdee, protein_g, carb_g, fat_g] + pasti_formattati)

with open('/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    header = ['id', 'eta', 'peso', 'altezza', 'obbiettivo', 'stile_di_vita', 'tdee', 'protein_g', 'carb_g', 'fat_g',
              'colazione', 'spuntino_mattina', 'pranzo', 'spuntino_pomeriggio', 'cena']
    writer.writerow(header)
    writer.writerows(csv_data) """

print("Simulazione completata. I dati sono stati salvati in 'output.csv'.")