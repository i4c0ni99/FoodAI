import pandas as pd
import os

# Dizionario delle categorie generiche
generic_categories = {
    'dairy': ['BUTTER', 'CHEESE', 'CREAM', 'SOUR CREAM', 'MILK', 'WHEY', 'YOGURT', 'CHEESE FD', 'CHEESE SPRD',
              'CREAM SUBSTITUTE', 'DESSERT TOPPING', 'SOUR CRM', 'MILK SHAKES', 'CHEESE SUB', 'CHEESE SAU',
              'PARMESAN CHS TOPPING', 'CREAM SUB'],

    'eggs': ['EGG', 'Egg', 'EGG SUBSTITUTE', 'EGG MIX'],

    'first dishes': ['COUSCOUS', 'NOODLES', 'MACARONI', 'PASTA', 'RICE', 'SEMOLINA', 'SPAGHETTI', 'TORTELLINI'],

    'oilsFats': ['FAT', 'SALAD DRSNG', 'SHORTENING', 'SHORTENING BREAD', 'SHORTENING FRYING (REG)',
                 'SHORTENING CAKE MIX', 'SHORTENING FRYING (HVY DUTY)', 'SHORTENING CONFECTIONERY',
                 'SHORTENING FRYING HVY DUTY',
                 'SHORTENING INDUSTRIAL', 'MEAT DRIPPINGS (LARD', 'ANIMAL FAT'],

    'poultry': ['CHICKEN', 'DUCK', 'GOOSE', 'GUINEA HEN', 'PHEASANT', 'QUAIL', 'SQUAB', 'TURKEY', 'PATE DE FOIE GRAS',
                'TURKEY AND GRAVY', 'TURKEY PATTIES', 'TURKEY BREAST', 'TURKEY THIGH', 'TURKEY RST', 'TURKEY STKS',
                'POULTRY', 'POULTRY FD PRODUCTS', 'CHICKEN NUGGETS', 'CHICKEN PATTY', 'CHICKEN BREAST TENDERS',
                'USDA CMDTY CHICK', 'USDA CMDTY', 'OSTRICH'],

    'meats': ['BARBECUE LOAF', 'BEEF', 'BF', 'BEERWURST', 'BUFFALO', 'BOLOGNA', 'BRATWURST',
              'BRAUNSCHWEIGER (A LIVER SAUSAGE)',
              'BROTWURST', 'CHEESEFURTER', 'CHORIZO', 'CORNED BEEF LOAF', 'DUTCH BRAND LOAF', 'FRANKFURTER', 'HAM',
              'HEADCHEESE', 'SAUSAGE', 'KIELBASA', 'LAMB', 'LIVER CHEESE', 'LIVER SAUSAGE', 'LUNCHEON MEAT',
              'MORTADELLA',
              'OLIVE LOAF', 'PASTRAMI', 'PATE', 'PEPPERONI', 'PICKLE&PIMIENTO LOAF', 'POLISH SAUSAGE', 'LUXURY LOAF',
              'MOTHER\'S LOAF', 'PICNIC LOAF', 'PORK', 'PORK SAUSAGE', 'PORK&BF SAUSAGE', 'TURKEY SAUSAGE', 'SALAMI',
              'SANDWICH SPREAD', 'SMOKED LINK SAUSAGE', 'THURINGER', 'TURKEY HAM', 'TURKEY ROLL', 'HONEY ROLL SAUSAGE',
              'LUNCHEON SAUSAGE', 'NEW ENGLAND BRAND SAUSAGE', 'OSCAR MAYER', 'LOUIS RICH', 'BUTCHER BOY MEATS',
              'CARL BUDDIG',
              'CARL BUDDIG. CKD SMOKED BF PASTRAMI', 'HORMEL SPAM', 'YACHTWURST', 'SCRAPPLE', 'BEEF SAUSAGE',
              'PORK & TURKEY SAUSAGE', 'VEAL'],

    'cereals': ['CEREALS RTE', 'CEREALS', 'CEREALS READY TO EAT', 'CERLS', 'CEREAL WAFER STRAWS'],

    'fish': ['CRAB', 'CATFISH', 'FISH', 'Fish', 'SALMON', 'STEELHEAD TROUT'],

    'fruits': ['ACEROLA', 'ACEROLA JUICE', 'APPLES', 'APPLE JUC', 'APPLESAUCE', 'APRICOTS', 'APRICOT NECTAR',
               'AVOCADOS', 'BANANAS', 'BLACKBERRIES', 'BLACKBERRY JUC', 'BLUEBERRIES', 'BOYSENBERRIES', 'BREADFRUIT',
               'CARAMBOLA', 'CARISSA', 'CHERIMOYA', 'CHERRIES', 'CRABAPPLES', 'CRANBERRIES', 'CRANBERRY SAU',
               'CRANBERRY-ORANGE RELISH', 'CURRANTS', 'CUSTARD-APPLE', 'DATES', 'ELDERBERRIES', 'FIGS', 'FRUIT SALAD',
               'GOOSEBERRIES', 'GRAPEFRUIT', 'GRAPEFRUIT JUC', 'GRAPE JUC', 'GRAPES', 'GROUNDCHERRIES', 'GUAVAS',
               'GUAVA SAUCE', 'JACKFRUIT', 'JAVA-PLUM', 'JUJUBE', 'KIWI FRUIT', 'KUMQUATS', 'LEMONS', 'LEMON JUICE',
               'LEMON JUC', 'LEMON PEEL', 'LIMES', 'LIME JUICE', 'LIME JUC', 'LITCHIS', 'LOGANBERRIES', 'LONGANS',
               'LOQUATS', 'MAMMY-APPLE', 'MANGOS', 'MANGOSTEEN', 'MELON', 'MELONS', 'MELON BALLS', 'FRUIT',
               'MULBERRIES',
               'NECTARINES', 'OHELOBERRIES', 'OLIVES', 'ORANGES', 'ORANGE JUICE', 'ORANGE JUC', 'ORANGE PEEL',
               'ORANGE-GRAPEFRUIT JUC', 'TANGERINES', 'TANGERINE JUICE', 'TANGERINE JUC', 'PAPAYAS', 'PAPAYA NECTAR',
               'PASSION-FRUIT', 'PASSION-FRUIT JUC', 'PEACHES', 'PEACH NECTAR', 'PEARS', 'PEAR NECTAR', 'PERSIMMONS',
               'PINEAPPLE', 'PINEAPPLE JUC', 'PITANGA', 'PLANTAINS', 'PLUMS', 'POMEGRANATES', 'PRICKLY PEARS',
               'PRUNES', 'PRUNE JUICE', 'PUMMELO', 'QUINCES', 'RAISINS', 'RAMBUTAN', 'RASPBERRIES', 'RHUBARB',
               'ROSELLE',
               'ROSE-APPLES', 'SAPODILLA', 'SAPOTES', 'SOURSOP', 'STRAWBERRIES', 'SUGAR-APPLES', 'TAMARINDS',
               'WATERMELON', 'MARASCHINO CHERRIES', 'FRUIT'],

    'legumes': ['BLACK BEANS', 'BROADBEANS', 'CHICKPEAS', 'GARBANZO', 'LENTILS', 'NAVY BEANS', 'PEAS', 'SPLIT PEAS',
                'PIGEON PEAS', 'PINK BEANS', 'PINTO BEANS', 'SOYBEANS', 'MUNG BEANS', 'RED BEANS', 'KIDNEY BEANS',
                'LIMA BEANS', 'LUPINS', 'MUNG'],

    'vegetables': ['ALFALFA SEEDS', 'BEANS', 'BEAN SPROUTS', 'BROCCOLI', 'BROCCOLI RABE', 'BRUSSELS SPROUTS',
                   'CABBAGE', 'CACTUS', 'CANTALOUPE', 'CARROTS', 'CAULIFLOWER', 'CELERIAC', 'CELERY', 'CHAYOTE',
                   'CHINESE CABBAGE', 'CHINESE PEAS', 'COLLARDS', 'CUCUMBERS', 'EGGPLANT', 'ENDIVE', 'GARLIC', 'KALE',
                   'KOHLRABI', 'LETTUCE', 'MUSHROOMS', 'ONIONS', 'PARSNIPS', 'PEPPERS', 'POTATOES', 'PUMPKIN',
                   'RADISHES', 'RUTABAGAS', 'SHALLOTS', 'SPINACH', 'SQUASH', 'SWEET CORN', 'SWEET POTATOES', 'TOFU',
                   'TOMATOES', 'TURNIPS', 'WATER CHESTNUTS', 'YAMS', 'CORN', 'VEGETABLES'],

    'sweets': ['CANDIES', 'CANDY', 'CHOCOLATE', 'DANISH PASTRY', 'DESSERTS', 'DONUTS', 'DOUGHNUTS', 'FROSTINGS',
               'ICE CREAM', 'FROZEN NOVELTIES', 'FRUIT LEATHER', 'FRUIT ICE', 'FRUIT LEATHERS', 'FRUIT LEATHER',
               'FRUIT ROLL-UPS', 'FRUIT STRIPS', 'FUDGE', 'GLAZE', 'ICE CREAM BARS', 'JELLIES', 'MARSHMALLOW',
               'MERINGUE',
               'MINTS', 'PIES', 'PIE FILLINGS', 'PUDDINGS', 'SHERBET', 'SORBET', 'SUGAR'],

    'nutsAndSeeds': ['ACORNS', 'ALMONDS', 'BEECHNUTS', 'BRAZILNUTS', 'BREADNUT TREE SEEDS', 'BREADFRUIT SEEDS',
                     'CANDLENUTS',
                     'CASHEWNUTS', 'CHESTNUTS', 'CHINQUAPIN NUTS', 'CHINESE CHESTNUTS', 'COCONUT MEAT', 'COCONUTS',
                     'GINKGO NUTS', 'HAZELNUTS', 'HICKORYNUTS', 'JAPANESE CHESTNUTS', 'LOTUS SEEDS', 'MACADAMIA NUTS',
                     'OAK ACORNS', 'OAK NUTS', 'PEANUTS', 'PECANS', 'PISTACHIONUTS', 'PUMPKIN SEEDS', 'SOY NUTS',
                     'SQUASH SEEDS',
                     'WALNUTS'],

    'bakedGoods': ['BAGELS', 'BREAD', 'BREADSTICKS', 'CORN MEAL', 'CROISSANTS', 'CUPCAKES', 'ENGLISH MUFFINS',
                   'FRENCH TOAST', 'MALTED BREAD', 'MELBA TOAST', 'MUFFINS', 'PANCAKES', 'PANCAKE', 'PIZZA',
                   'RICE CAKES',
                   'ROLLS', 'TOAST', 'WAFFLES'],

}


# Funzione per ottenere la categoria generica
def get_generic_category(category):
    for key, values in generic_categories.items():
        if category in values:
            return key
    return None  # Restituisce None se la categoria non appartiene a quelle generiche


def filter_and_prepare_csv(input_csv_path, output_csv_path, min_instances=5000):
    df = pd.read_csv(input_csv_path)

    df.columns = [col.lower() for col in df.columns]

    # Elenco delle colonne richieste
    required_columns = [
        'nutrient data bank number', 'category', 'description', 'data.carbohydrate',
        'data.kilocalories', 'data.protein', 'data.fat.total lipid', 'data.fiber', 'data.sugar total'
    ]

    # Seleziona e crea una copia
    filtered_df = df[[col for col in required_columns if col.lower() in df.columns]].copy()

    # Rinomina le colonne
    column_renames = {
        'nutrient data bank number': 'id',
        'data.carbohydrate': 'carbohydrate',
        'data.kilocalories': 'kilocalories',
        'data.protein': 'protein',
        'data.fat.total lipid': 'fat',
        'data.fiber': 'fiber',
        'data.sugar total': 'sugar'
    }
    filtered_df = filtered_df.rename(columns=column_renames)

    # Verifica l'esistenza della colonna 'fat'
    if 'fat' not in filtered_df.columns:
        print("La colonna 'fat' non esiste nel DataFrame.")
        return filtered_df  # oppure gestisci in altro modo l'assenza della colonna

    # Lista dei valori da rimuovere
    categories_to_remove = ['No Category', 'SPICE', 'SQUIRREL', 'TURTLE', 'OIL', 'CATTAIL', 'BEAR', 'WHALE', 'whale',
                            'WALRUS', 'SEAL', 'seal', 'Seal', 'MOUSE NUTS', 'GUM', 'CHEWING GUM']
    words_to_remove = ['SPICE', 'OIL', 'COCKTAIL', 'BABYFOOD', 'ALCOHOLIC', 'MARGARINE', 'SEA LION', 'TURTLE']

    # Record da mantenere
    mask = ~filtered_df['category'].isin(categories_to_remove)
    for word in words_to_remove:
        mask &= ~filtered_df['description'].str.contains(word, case=False)

    # Applica la maschera al DataFrame
    filtered_df = filtered_df[mask]

    # Arrotonda le colonne 'carbohydrate', 'protein' e 'fat' a una cifra decimale
    columns_to_round = ['carbohydrate', 'protein', 'fat']
    for col in columns_to_round:
        if col in filtered_df.columns:
            filtered_df[col] = filtered_df[col].apply(lambda x: round(x, 1))

    # Calcola le calorie totali dai macronutrienti
    filtered_df['calories_from_macros'] = (filtered_df['carbohydrate'] * 4 +
                                           filtered_df['protein'] * 4 +
                                           filtered_df['fat'] * 9)

    # Calcola le percentuali di macronutrienti
    filtered_df['carb_percentage'] = (filtered_df['carbohydrate'] * 4 / filtered_df['calories_from_macros']) * 100
    filtered_df['protein_percentage'] = (filtered_df['protein'] * 4 / filtered_df['calories_from_macros']) * 100
    filtered_df['fat_percentage'] = (filtered_df['fat'] * 9 / filtered_df['calories_from_macros']) * 100

    # Rimuovi la colonna temporanea
    filtered_df = filtered_df.drop(columns=['calories_from_macros'])

    # Pulizia dati
    filtered_df = filtered_df.dropna()
    filtered_df.drop_duplicates(subset=['fat', 'protein', 'carbohydrate', 'category'], inplace=True)

    # Colonna delle categorie generiche
    filtered_df['generic_category'] = filtered_df['category'].apply(get_generic_category)

    # Filtra gli alimenti che non rientrano nelle categorie generiche
    filtered_df = filtered_df.dropna(subset=['generic_category'])

    filtered_df.to_csv(output_csv_path, index=False)

    return filtered_df


input_csv_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/food-data.csv'
output_csv_path = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/prepared_food_data.csv'
filter_and_prepare_csv(input_csv_path, output_csv_path)
