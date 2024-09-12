import sqlite3
import json

conn = sqlite3.connect('meals.db')
c = conn.cursor()

# Creazione delle tabelle per ciascun macronutriente
c.execute('''
    CREATE TABLE IF NOT EXISTS carbohydrate (
        id INTEGER PRIMARY KEY AUTOINCREMENT
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
    CREATE TABLE IF NOT EXISTS meal_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_carbohydrate INTEGER,
        id_protein INTEGER,
        id_fat INTEGER,
        meal TEXT,
        FOREIGN KEY (id_carbohydrate) REFERENCES carbohydrate(id),
        FOREIGN KEY (id_protein) REFERENCES protein(id),
        FOREIGN KEY (id_fat) REFERENCES fat(id)
    )
''')



conn.commit()
conn.close()

print("Database creato e dati inseriti correttamente")