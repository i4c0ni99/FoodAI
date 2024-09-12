import sqlite3
import json

conn = sqlite3.connect('meals.db')
c = conn.cursor()

# Creazione delle tabelle per ciascun macronutriente
c.execute('''
    CREATE TABLE IF NOT EXISTS carbohydrate (
        id INT AUTOINCREMENT
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

conn.commit()
conn.close()

print("Database creato e dati inseriti correttamente")
 
 import sqlite3

# Creazione del database
db_path = '/Users/lucavisconti/Documents/FoodAI/db/meal_plan.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Creazione della tabella giornaliera
cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_meal_plan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        colazione_carbohydrate_category TEXT,
        colazione_carbohydrate_description TEXT,
        colazione_carbohydrate_grams REAL,
        colazione_protein_category TEXT,
        colazione_protein_description TEXT,
        colazione_protein_grams REAL,
        colazione_fat_category TEXT,
        colazione_fat_description TEXT,
        colazione_fat_grams REAL,
        spuntino_mattina_carbohydrate_category TEXT,
        spuntino_mattina_carbohydrate_description TEXT,
        spuntino_mattina_carbohydrate_grams REAL,
        spuntino_mattina_protein_category TEXT,
        spuntino_mattina_protein_description TEXT,
        spuntino_mattina_protein_grams REAL,
        spuntino_mattina_fat_category TEXT,
        spuntino_mattina_fat_description TEXT,
        spuntino_mattina_fat_grams REAL,
        pranzo_carbohydrate_category TEXT,
        pranzo_carbohydrate_description TEXT,
        pranzo_carbohydrate_grams REAL,
        pranzo_protein_category TEXT,
        pranzo_protein_description TEXT,
        pranzo_protein_grams REAL,
        pranzo_fat_category TEXT,
        pranzo_fat_description TEXT,
        pranzo_fat_grams REAL,
        spuntino_pom_carbohydrate_category TEXT,
        spuntino_pom_carbohydrate_description TEXT,
        spuntino_pom_carbohydrate_grams REAL,
        spuntino_pom_protein_category TEXT,
        spuntino_pom_protein_description TEXT,
        spuntino_pom_protein_grams REAL,
        spuntino_pom_fat_category TEXT,
        spuntino_pom_fat_description TEXT,
        spuntino_pom_fat_grams REAL,
        cena_carbohydrate_category TEXT,
        cena_carbohydrate_description TEXT,
        cena_carbohydrate_grams REAL,
        cena_protein_category TEXT,
        cena_protein_description TEXT,
        cena_protein_grams REAL,
        cena_fat_category TEXT,
        cena_fat_description TEXT,
        cena_fat_grams REAL
    )
''')

# Inserimento di dati di esempio per una giornata
cursor.execute('''
    INSERT INTO daily_meal_plan (
        colazione_carbohydrate_category, colazione_carbohydrate_description, colazione_carbohydrate_grams,
        colazione_protein_category, colazione_protein_description, colazione_protein_grams,
        colazione_fat_category, colazione_fat_description, colazione_fat_grams,
        spuntino_mattina_carbohydrate_category, spuntino_mattina_carbohydrate_description, spuntino_mattina_carbohydrate_grams,
        spuntino_mattina_protein_category, spuntino_mattina_protein_description, spuntino_mattina_protein_grams,
        spuntino_mattina_fat_category, spuntino_mattina_fat_description, spuntino_mattina_fat_grams,
        pranzo_carbohydrate_category, pranzo_carbohydrate_description, pranzo_carbohydrate_grams,
        pranzo_protein_category, pranzo_protein_description, pranzo_protein_grams,
        pranzo_fat_category, pranzo_fat_description, pranzo_fat_grams,
        spuntino_pom_carbohydrate_category, spuntino_pom_carbohydrate_description, spuntino_pom_carbohydrate_grams,
        spuntino_pom_protein_category, spuntino_pom_protein_description, spuntino_pom_protein_grams,
        spuntino_pom_fat_category, spuntino_pom_fat_description, spuntino_pom_fat_grams,
        cena_carbohydrate_category, cena_carbohydrate_description, cena_carbohydrate_grams,
        cena_protein_category, cena_protein_description, cena_protein_grams,
        cena_fat_category, cena_fat_description, cena_fat_grams
    ) VALUES (
        'TANGERINES', 'TANGERINES,(MANDARIN ORANGES),CND,LT SYRUP PK', 372.0,
        'TURKEY', 'TURKEY,YOUNG TOM,LT MEAT,MEAT ONLY,CKD,RSTD', 100.0,
        'FRANKFURTER', 'FRANKFURTER,PORK', 69.0,
        'BLUEBERRIES', 'BLUEBERRIES,CND,LT SYRUP,DRND', 123.0,
        'BEEF', 'BEEF,RND,TOP RND,LN,1/8" FAT,SEL,RAW', 26.5,
        'BEERWURST', 'BEERWURST,BEER SALAMI,PORK', 25.8,
        'PEARS', 'PEARS,RAW', 581.5,
        'OSTRICH', 'OSTRICH,INSIDE LEG,RAW', 289.1,
        'OSCAR MAYER', 'OSCAR MAYER,SALAMI (FOR BEER)', 151.2,
        'PERSIMMONS', 'PERSIMMONS,JAPANESE,DRIED', 14.6,
        'TURKEY', 'TURKEY,BREAST,SMOKED,LEMON PEPPER FLAVOR', 31.9,
        'QUAIL', 'QUAIL,COOKED,TOTAL EDIBLE', 44.7,
        'PINEAPPLE JUC', 'PINEAPPLE JUC,FRZ CONC,UNSWTND,UNDIL', 159.0,
        'PORK', 'PORK,CURED,HAM W/ NAT JUICES,SLICE,BONE-IN,LN,UNHTD', 231.2,
        'GOOSE', 'GOOSE,DOMESTICATED,MEAT&SKN,RAW', 82.3
    )
''')

# Commit per salvare i cambiamenti
conn.commit()

# Chiudi la connessione al database
conn.close()

print("Database e dati creati con successo!")
 """