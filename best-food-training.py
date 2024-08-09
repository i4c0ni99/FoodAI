import pandas as pd
import numpy as np
import os

# Definisci il dataset di categorie generiche
generic_categories = {

    'dairy': ['BUTTER', 'CHEESE', 'CREAM', 'SOUR CREAM', 'MILK', 'WHEY', 'YOGURT', 'CHEESE FD', 'CHEESE SPRD',
              'CREAM SUBSTITUTE', 'DESSERT TOPPING', 'SOUR CRM', 'MILK SHAKES', 'CHEESE SUB', 'CHEESE SAU',
              'PARMESAN CHS TOPPING', 'CREAM SUB'],

    'eggs': ['EGG', 'Egg', 'EGG SUBSTITUTE', 'EGG MIX'],

    'first dishes': ['COUSCOUS', 'NOODLES', 'MACARONI', 'PASTA', 'RICE', 'SEMOLINA', 'SPAGHETTI', 'TORTELLINI'],

    'herbsSpices': ['CHERVIL', 'CINNAMON', 'CLOVES', 'CORIANDER LEAF', 'DILL WEED', 'GINGER', 'MACE', 'MARJORAM',
                    'MUSTARD SEED', 'NUTMEG', 'PARSLEY', 'PEPPER', 'ROSEMARY', 'SAGE', 'SAVORY', 'TURMERIC', 'BASIL',
                    'MUSTARD', 'THYME', 'VANILLA EXTRACT', 'CAPERS', 'HORSERADISH', 'PEPPERMINT', 'SPEARMINT'],

    'soupsSauces': ['CAMPBELL SOUP CO', 'CAMPBELL', 'CAMPBELL SOUP', 'CAMPBELL SOUP COMPANY', 'CAMPBELL COMPANY',
                    'CAMPBELL\'S RED & WHITE', 'SOUP', 'SAUCE', 'GRAVY', 'SPLIT PEA SOUP', 'SPLIT PEA W/ HAM SOUP',
                    'CAMPBELL\'S RED&WHITE', 'CAMPBEL COMPANY', 'CAMPBELL\'S CHUNKY MICROWAVABLE BWLS',
                    'CAMPBELL SOUP COMP',
                    'COMPANY', 'SOUP COMPANY', 'CAMPBELL\'S CHUNKY SOUPS', 'CAMPBELL\'S CHNKY SOUPS',
                    'CAMPBELL\'S RED & WHITE - MCRWVEABLE BOWLS', 'CAMPBELL\'S RED & WHITE - MICROWAVEABLE BOWLS',
                    'CAMPBELL\'S SEL GOLD LABEL SOUPS', 'CAMPBELL\'S SEL MCRWVABLE BOWLS',
                    'CAMPBELL\'S SEL MCRWVABLE BWLS',
                    'CAMPBELL\'S SEL MICROWAVEABLE BOWLS', 'CAMPBELL\'S SEL SOUP', 'CAMPBELL\'S SOUP AT HAND',
                    'POTATO SOUP'],

    'oilsFats': ['FAT', 'SALAD DRSNG', 'SHORTENING', 'SHORTENING BREAD', 'SHORTENING FRYING (REG)',
                 'SHORTENING CAKE MIX',
                 'SHORTENING FRYING (HVY DUTY)', 'SHORTENING CONFECTIONERY', 'SHORTENING FRYING HVY DUTY',
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
               'AVOCADOS',
               'BANANAS', 'BLACKBERRIES', 'BLACKBERRY JUC', 'BLUEBERRIES', 'BOYSENBERRIES', 'BREADFRUIT', 'CARAMBOLA',
               'CARISSA', 'CHERIMOYA', 'CHERRIES', 'CRABAPPLES', 'CRANBERRIES', 'CRANBERRY SAU',
               'CRANBERRY-ORANGE RELISH',
               'CURRANTS', 'CUSTARD-APPLE', 'DATES', 'ELDERBERRIES', 'FIGS', 'FRUIT SALAD', 'GOOSEBERRIES',
               'GRAPEFRUIT',
               'GRAPEFRUIT JUC', 'GRAPE JUC', 'GRAPES', 'GROUNDCHERRIES', 'GUAVAS', 'GUAVA SAUCE', 'JACKFRUIT',
               'JAVA-PLUM',
               'JUJUBE', 'KIWI FRUIT', 'KUMQUATS', 'LEMONS', 'LEMON JUICE', 'LEMON JUC', 'LEMON PEEL', 'LIMES',
               'LIME JUICE',
               'LIME JUC', 'LITCHIS', 'LOGANBERRIES', 'LONGANS', 'LOQUATS', 'MAMMY-APPLE', 'MANGOS', 'MANGOSTEEN',
               'MELON', 'MELONS',
               'MELON BALLS', 'FRUIT', 'MULBERRIES', 'NECTARINES', 'OHELOBERRIES', 'OLIVES', 'ORANGES', 'ORANGE JUICE',
               'ORANGE JUC', 'ORANGE PEEL', 'ORANGE-GRAPEFRUIT JUC', 'TANGERINES', 'TANGERINE JUICE', 'TANGERINE JUC',
               'PAPAYAS', 'PAPAYA NECTAR', 'PASSION-FRUIT', 'PASSION-FRUIT JUC', 'PEACHES', 'PEACH NECTAR', 'PEARS',
               'PEAR NECTAR', 'PERSIMMONS', 'PINEAPPLE', 'PINEAPPLE JUC', 'PITANGA', 'PLANTAINS', 'PLUMS',
               'POMEGRANATES',
               'PRICKLY PEARS', 'PRUNES', 'PRUNE JUICE', 'PUMMELO', 'QUINCES', 'RAISINS', 'RAMBUTAN', 'RASPBERRIES',
               'RHUBARB',
               'ROSELLE', 'ROSE-APPLES', 'SAPODILLA', 'SAPOTES', 'SOURSOP', 'STRAWBERRIES', 'SUGAR-APPLES', 'TAMARINDS',
               'WATERMELON', 'MARASCHINO CHERRIES'],

    'legumes': ['BLACK BEANS', 'BROADBEANS', 'CHICKPEAS', 'GARBANZO', 'LENTILS', 'NAVY BEANS', 'PEAS', 'SPLIT PEAS',
                'PIGEON PEAS', 'PINK BEANS', 'PINTO BEANS', 'SOYBEANS', 'MUNG BEANS', 'RED BEANS', 'KIDNEY BEANS',
                'LIMA BEANS', 'LUPINS', 'MUNG'],

    'nutsSeeds': ['ACORN FLOUR', 'ALMONDS', 'APRICOT SEED', 'BEECHNUTS', 'BREADNUT TREE SEED', 'BUTTERNUTS', 'CASHEW',
                  'CHINESE CHESTNUT', 'COTTONSEED', 'ENGLISH WALNUT', 'FILBERTS', 'GINKGO NUTS', 'HAZELNUTS',
                  'HICKORY NUTS',
                  'LITCHI NUTS', 'LOTUS SEEDS', 'MACADAMIA NUTS', 'PECANS', 'PILI NUTS', 'PINE NUTS', 'PUMPKIN SEEDS',
                  'SESAME SEEDS', 'SUNFLOWER SEEDS', 'WALNUTS', 'WATERMELON SEEDS', 'WINGED BEAN SEED'],

    'vegetables': ['ALFALFA SEEDS', 'BEANS', 'BEAN SPROUTS', 'BROCCOLI', 'BROCCOLI RABE', 'BRUSSELS SPROUTS', 'CABBAGE',
                   'CACTUS', 'CANTALOUPE', 'CARROTS', 'CAULIFLOWER', 'CELERIAC', 'CELERY', 'CHAYOTE', 'CHINESE CABBAGE',
                   'CHINESE PEAS', 'COLLARDS', 'CUCUMBERS', 'EGGPLANT', 'ENDIVE', 'GARLIC', 'KALE', 'KOHLRABI',
                   'LETTUCE',
                   'MUSHROOMS', 'ONIONS', 'PARSNIPS', 'PEPPERS', 'POTATOES', 'PUMPKIN', 'RADISHES', 'RUTABAGAS',
                   'SHALLOTS',
                   'SPINACH', 'SQUASH', 'SWEET CORN', 'SWEET POTATOES', 'TOFU', 'TOMATOES', 'TURNIPS',
                   'WATER CHESTNUTS', 'YAMS',
                   'CORN', 'VEGETABLES'],

    'drinks': ['SOFT DRINK', 'BEVERAGE', 'COFFEE', 'JUICE', 'WATER', 'ALCOHOL', 'ALCOHOLIC BEVERAGE', 'COCOA', 'TEA'],

    'sweets': ['CANDIES', 'CANDY', 'CHOCOLATE', 'DANISH PASTRY', 'DESSERTS', 'GELATIN DSSRT', 'GUM', 'CHEWING GUM',
               'DESSERT',
               'FROSTING', 'ICE CREAM', 'ICE CREAMS', 'ICE CRM CONES', 'LIGHT ICE CRM', 'ENGLISH MUFFINS', 'MUFFINS',
               'PANCAKES',
               'PIE', 'PUDDING', 'PUDDINGS', 'TREAT', 'WAFFLES'],

    'baked goods': ['CAKE', 'COOKIES', 'BAKERY PRODUCT', 'BREAD', 'PASTRY', 'CRACKERS', 'PIE CRUST', 'ROLLS',
                    'SNACK BAR',
                    'SWEET ROLLS', 'WAFER'],

    'meals': ['FROZEN MEALS', 'SANDWICH', 'LASAGNA', 'MEAL', 'MEATBALLS', 'FLAN', 'STEW'],

    'condiments': ['MAYONNAISE', 'MIX', 'FILLING', 'FROSTING', 'SAUCE', 'SPREAD', 'PRESERVE'],

    'seasonings': ['CONDIMENT', 'SEASONING', 'SPICE', 'BAKING POWDER', 'SUGAR', 'SWEETENER', 'SYRUP'],

    'ingredients': ['INGREDIENT', 'FLOUR', 'YEAST', 'TAPIOCA', 'WHEAT'],

    'miscellaneous': ['FOOD', 'SNACKS', 'CUSTARD', 'PICKLES', 'FRUIT', 'GELATIN', 'WATER'],

    'fast food': ['BURGER KING', 'Burger king', "DOMINO'S", 'FT FDS', 'FAST FDS', 'FAST FD', 'FAST FOODS', 'FST FD',
                  'LITTLE CAESARS', "MCDONALD'S", "McDONALD'S", 'PAPA', 'PIZZA', 'PIZZA HUT', 'POPEYES', 'TACO BELL',]

}


# Funzione per caricare il dataset
def load_dataset(input_file):
    """Carica il dataset dal file CSV."""
    return pd.read_csv(input_file)


# Funzione per trovare il miglior alimento in base ai criteri
def find_best_food(df, category, food_list):
    """Trova il miglior alimento per una specifica categoria."""
    # Filtra per la categoria e per gli alimenti nella food_list
    category_df = df[(df['category'].isin(food_list))]

    if category_df.empty:
        return None

    print(f"Alimenti disponibili per la categoria '{category}':")
    print(category_df)

    # Filtra gli alimenti considerati nutrizionali
    category_df = category_df[(category_df['carbohydrate'] >= 30) & (category_df['protein'] >= 20)]
    #alogritmo da implementare è un max quando viene trovato il max viene eliminato dal DataFrame     
    if category_df.empty:
        print(f"Nessun alimento con carboidrati >= 30 e proteine >= 20 per '{category}'.")
        return None

    # Filtra gli alimenti con basso contenuto di grassi
    fat_threshold = category_df['fat'].quantile(0.25)
    category_df = category_df[category_df['fat'] <= fat_threshold]

    if category_df.empty:
        print(f"Nessun alimento con grassi <= {fat_threshold} per '{category}'.")
        return None

    # Calcola il punteggio
    category_df['score'] = category_df['protein'] + category_df['carbohydrate']

    best_food = category_df.loc[category_df['score'].idxmax()]

    return best_food


# Funzione per richiedere feedback e gestire l'alternativa
def request_feedback(category, initial_food, df, food_list, evaluated_food_ids):
    """Richiede feedback sull'alimento proposto e gestisce le alternative."""
    print(f"\nCategoria: {category}")
    print(f"Alimento proposto: {initial_food['category']}")
    print(f"Descrizione: {initial_food['description']}")
    print(f"Carboidrati: {initial_food['carbohydrate']}")
    print(f"Proteine: {initial_food['protein']}")
    print(f"Grassi: {initial_food['fat']}")
    print(f"Kilocalorie: {initial_food['kilocalories']}")

    feedback = input("Questo alimento è adatto? (sì/no) oppure digitare 'stop' per fermare: ").strip().lower()

    if feedback == 'stop':
        return None, 'interrotto'

    if feedback == 'sì':
        return initial_food, 'approvato'
    else:
        # Trova un'altra alternativa
        alternative_df = df[
            (df['id'] != initial_food['id']) & (df['category'].isin(food_list)) & (~df['id'].isin(evaluated_food_ids))]

        if not alternative_df.empty:
            alternative_food = find_best_food(df, category, food_list)
            if alternative_food is not None:
                print("\nProposta alternativa:")
                return request_feedback(category, alternative_food, df, food_list, evaluated_food_ids)
            else:
                print("Non ci sono altre alternative disponibili.")
        return None, 'rifiutato'


# Funzione principale
def main(input_file, output_file, categories_file):
    """Esegue il processo di selezione e salvataggio dei migliori alimenti."""
    # Carica il dataset
    df = load_dataset(input_file)

    # Carica le categorie
    if os.path.exists(categories_file):
        categories_df = pd.read_csv(categories_file)
    else:
        # Crea un DataFrame per le categorie specifiche
        all_foods = [food for sublist in generic_categories.values() for food in sublist]
        categories_df = pd.DataFrame({
            'category': all_foods,
            'accettati': 0,
            'rifiutati': 0,
            'stato': 'da verificare'
        })

    # Carica gli alimenti già valutati, se esiste un file di output
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        evaluated_df = pd.read_csv(output_file)
        # Assicurati che la colonna 'id' sia presente
        if 'id' in evaluated_df.columns:
            evaluated_food_ids = evaluated_df['id'].tolist()
        else:
            print("La colonna 'id' non è presente nel file di output. Verifica il file.")
            evaluated_food_ids = []
    else:
        evaluated_food_ids = []

    results = []
    processed_categories = set()

    while True:
        # Seleziona una categoria specifica random tra quelle non ancora processate
        remaining_categories = set(
            categories_df[categories_df['stato'] == 'da verificare']['category']) - processed_categories
        if not remaining_categories:
            print("Non ci sono più categorie valide da processare.")
            break

        category = np.random.choice(list(remaining_categories))

        # Trova il miglior alimento per questa categoria
        food_list = generic_categories.get(category, [])
        best_food = find_best_food(df, category, food_list)

        if best_food is not None:
            # Richiedi feedback sull'alimento proposto
            final_food, feedback = request_feedback(category, best_food, df, food_list, evaluated_food_ids)

            if feedback == 'approvato':
                results.append({
                    'original_category': category,
                    'category': final_food['category'],
                    'description': final_food['description'],
                    'carbohydrate': final_food['carbohydrate'],
                    'protein': final_food['protein'],
                    'fat': final_food['fat'],
                    'kilocalories': final_food['kilocalories'],
                    'feedback': feedback
                })
                evaluated_food_ids.append(final_food['id'])

                # Se abbiamo trovato 5 alimenti approvati per questa categoria, la consideriamo completata
                if len([res for res in results if
                        res['original_category'] == category and res['feedback'] == 'approvato']) >= 5:
                    categories_df.loc[categories_df['category'] == category, 'stato'] = 'completata'
                    processed_categories.add(category)
            else:
                results.append({
                    'original_category': category,
                    'category': best_food['category'],
                    'description': best_food['description'],
                    'carbohydrate': best_food['carbohydrate'],
                    'protein': best_food['protein'],
                    'fat': best_food['fat'],
                    'kilocalories': best_food['kilocalories'],
                    'feedback': feedback
                })
                evaluated_food_ids.append(best_food['id'])
        else:
            print(f"Nessun alimento nutriente trovato per '{category}'. Ignorando questa categoria.")
            categories_df.loc[categories_df['category'] == category, 'stato'] = 'ignora'
            processed_categories.add(category)

    # Crea un DataFrame con i risultati
    results_df = pd.DataFrame(results)

    # Aggiungi i risultati già valutati, se presenti
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        existing_results_df = pd.read_csv(output_file)
        results_df = pd.concat([existing_results_df, results_df], ignore_index=True)

    # Salva il DataFrame in un file CSV
    results_df.to_csv(output_file, index=False)
    categories_df.to_csv(categories_file, index=False)

    print(f"I risultati finali sono stati salvati in '{output_file}'")
    print(f"Lo stato delle categorie è stato aggiornato in '{categories_file}'")


# Esegui la funzione principale
input_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/new_data.csv'  # Sostituisci con il percorso del tuo file CSV
training_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/training-file.csv'  # Sostituisci con il percorso del file CSV di output
categories_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/categories-file.csv'  # Nuovo file CSV delle categorie

main(input_file, training_file, categories_file)
