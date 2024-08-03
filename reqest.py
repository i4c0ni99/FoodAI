import json
import time
from fatsecret import Fatsecret



consumer_key = "ae8ad889881b4aa49998a8d293c99f7c"
consumer_secret = "64d1a26c5afb48c3a2c7bc06be526d33"


# Sostituisci questi con le tue chiavi API di FatSecret


# Crea un'istanza dell'API di FatSecret
fs = Fatsecret(consumer_key, consumer_secret)
category=['Beans & Legumes','Beverages','Breads & Cereals','Cheese',' Milk & Dairy','Eggs','Fish & Seafood','Fruit','Meat','Nuts & Seeds','Pasta', 'Rice & Noodles','Salads', 'Sauces', 'Spices & Spreads','Snacks','Soups','Sweets', 'Candy & Desserts','Vegetables','Other']
      
        
all_foods = []

for food_category in category :
        pagenuber = 0
        print(food_category)
        while pagenuber <=100:
            food_data = fs.foods_search(food_category,page_number=pagenuber,max_results=50,region='IT',language='it')
            
            print(pagenuber)
            if food_data :
                print(food_data[2])
            all_foods.append(food_data)
            time.sleep(0.5)
            pagenuber +=1# Aggiungi un ritardo per evitare di fare troppe richieste in poco tempo
    # Salva tutti i dati raccolti in un file JSON
with open('foods_data.json', 'w') as json_file:
        json.dump(all_foods, json_file, indent=4)
print("Dati degli alimenti salvati in 'foods_data.json'") 
 

    
"""
    
        if food_data:
            all_foods.append(food_data)
            time.sleep(1) # Aggiungi un ritardo per evitare di fare troppe richieste in poco tempo
    # Salva tutti i dati raccolti in un file JSON
    with open('foods_data.json', 'w') as json_file:
        json.dump(all_foods, json_file, indent=4)
    print("Dati degli alimenti salvati in 'foods_data.json'") 
"""
# Funzione per cercare i cibi e paginare i risultati
"""def search_all_foods():
    food_id = 1641
    global all_foods
    
    while food_id <= 1700:
        print('food_id =',food_id)
        try:
                foods = fs.food_get(food_id=food_id)
                
                # Verifica se la risposta contiene cibi
                all_foods.append(foods)
        except KeyError as e:
            print(f"Errore chiave non trovata: {e}")
            food_id += 1 
            
        except Exception as e:
            print(f"Errore durante la richiesta: {e}")
            
        food_id += 1    
# Scarica tutti i cibi
all_foods=search_all_foods()

# Stampa il numero totale di cibi scaricati

# Salva i risultati in un file JSON
print(all_foods)
import json
with open('all_foods.json', 'w') as f:
    json.dump(all_foods, f, indent=4)
"""    



""" 
import requests


response = requests.get("https://api.spoonacular.com/food/search?query=ingredients&number=600000&apiKey=475c377d00914f7f84740521a327a178&includeNutrition=true%22")

if response.status_code == 200:
    data = response.json()  # Ottenere i dati in formato JSON
    import json
    with open('def.json', 'w') as f:
        json.dump(data, f, indent=4)
        print(data)
else:
    print(f'Error: {response.status_code}') """
    