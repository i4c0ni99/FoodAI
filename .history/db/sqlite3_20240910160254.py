import sqlite3
import json

conn = sqlite3.connect('meals.db')
c = conn.cursor()

# Creazione delle tabelle per ciascun macronutriente
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

# Inserimento dei dati
for meal_name, meal_data in data['meal'].items():
    for nutrient, nutrient_data in meal_data.items():
        table_name = nutrient.lower()
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
