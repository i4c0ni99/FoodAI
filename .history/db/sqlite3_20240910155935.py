import sqlite3
import json

# Connessione al database SQLite (crea il database se non esiste)
conn = sqlite3.connect('meals.db')
c = conn.cursor()

# Creazione delle tabelle per ciascun macronutriente (carboidrati, proteine, grassi)
c.execute('''
    CREATE TABLE IF NOT EXISTS carbohydrate (
        meal TEXT,
        category TEXT,
        description TEXT,
        carbohydrate REAL,
        protein REAL,
        fat REAL,
        kilocalories REAL,
        generic_category TEXT,
        grams REAL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS protein (
        meal TEXT,
        category TEXT,
        description TEXT,
        carbohydrate REAL,
        protein REAL,
        fat REAL,
        kilocalories REAL,
        generic_category TEXT,
        grams REAL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS fat (
        meal TEXT,
        category TEXT,
        description TEXT,
        carbohydrate REAL,
        protein REAL,
        fat REAL,
        kilocalories REAL,
        generic_category TEXT,
        grams REAL
    )
''')

# Carica il file JSON
data = {
    "meal": {
        "colazione": {
            "carbohydrate": {
                "category": "TANGERINES",
                "description": "TANGERINES,(MANDARIN ORANGES),CND,LT SYRUP PK",
                "carbohydrate": 60.264,
                "protein": 1.86,
                "fat": 0.37200000000000005,
                "kilocalories": 251.84400000000002,
                "generic_category": "fruits",
                "grams": 372.0
            },
            "protein": {
                "category": "TURKEY",
                "description": "TURKEY,YOUNG TOM,LT MEAT,MEAT ONLY,CKD,RSTD",
                "carbohydrate": 0.0,
                "protein": 29.913174687499996,
                "fat": 2.9012778124999996,
                "kilocalories": 145.76419906249998,
                "generic_category": "poultry",
                "grams": 100.0440625
            },
            "fat": {
                "category": "FRANKFURTER",
                "description": "FRANKFURTER,PORK",
                "carbohydrate": 0.20990816343750002,
                "protein": 8.956081640000003,
                "fat": 16.582744911562504,
                "kilocalories": 185.90866341781256,
                "generic_category": "meats",
                "grams": 69.9693878125
            }
        },
        # Aggiungere altri pasti qui...
    }
}

# Inserimento dei dati nel database
for meal_name, meal_data in data['meal'].items():
    for nutrient, nutrient_data in meal_data.items():
        table_name = nutrient.lower()  # Usa il nome del macronutriente come nome tabella
        query = f'''
            INSERT INTO {table_name} 
            (meal, category, description, carbohydrate, protein, fat, kilocalories, generic_category, grams)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        values = (
            meal_name, 
            nutrient_data['category'],
            nutrient_data['description'],
            nutrient_data['carbohydrate'],
            nutrient_data['protein'],
            nutrient_data['fat'],
            nutrient_data['kilocalories'],
            nutrient_data['generic_category'],
            nutrient_data['grams']
        )
        c.execute(query, values)

# Commit delle modifiche e chiusura della connessione
conn.commit()
conn.close()

print("Database creato e dati inseriti con successo!")
