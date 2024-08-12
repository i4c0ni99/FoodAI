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

def get_row(max_score,df):
    
    return df[df['nutritional_score'] == max_score],df[df['nutritional_score'] < max_score]
# Funzione per caricare il dataset
def load_dataset(input_file):
    """Carica il dataset dal file CSV."""
    return pd.read_csv(input_file)


# Funzione per trovare il miglior alimento in base ai criteri
def find_best_food(df, category, food_list,remaining_categories,categories_df):
    """Trova il miglior alimento per una specifica categoria."""
    # Filtra per la categoria e per gli alimenti nella food_list
    """  category_df = df[(df['category'].isin(food_list))]

    if category_df.empty:
        return None

    print(f"Alimenti disponibili per la categoria '{category}':")
    print(category_df) """
    
    if food_list is  None  :
                categories_df.loc[categories_df['category'] == category, 'stato'] = 'completata'
                category = np.random.choice(list(remaining_categories))
            # Trova il miglior alimento per questa categoria
                food_list = df[df['category'] == category]
    # Calcola il punteggio
    if food_list is not None and len(food_list['nutritional_score']) > 0   :
        best_food,food_list = get_row(max(food_list['nutritional_score']),food_list)
        return best_food,food_list,category   
    return None,None,None


# Funzione per richiedere feedback e gestire l'alternativa
def request_feedback(category, initial_food, df, food_list, evaluated_food_ids,remaining_categories,categories_df):
    """Richiede feedback sull'alimento proposto e gestisce le alternative."""
    print(f"\nCategoria: {category}")
    print(f"Alimento proposto: {initial_food['category']}")
    print(f"Descrizione: {initial_food['description']}")
    print(f"Carboidrati: {initial_food['carbohydrate']}")
    print(f"Proteine: {initial_food['protein']}")
    print(f"Grassi: {initial_food['fat']}")
    print(f"Kilocalorie: {initial_food['kilocalories']}")

    
         
    feedback = input("Questo alimento è adatto? (si/no) oppure digitare 'stop' per fermare: ").strip().lower()

    if feedback == 'stop':
        return None, 'interrotto',category

    if feedback == 'si':
        return initial_food, 'approvato',category
    else:
        return initial_food, 'rifiutato',category
        # Trova un'altra alternativa
        """ if len(food_list) > 0 :
            alternative_food,food_list,category = find_best_food(df, category, food_list,remaining_categories,categories_df)
        print(alternative_food ,'questa e la proposta:')
        if alternative_food is not None:
            print("\nProposta alternativa:")
            return request_feedback(category, alternative_food, df, food_list, evaluated_food_ids,remaining_categories ,categories_df)
        else:
            print("Non ci sono altre alternative disponibili.") """
                
        


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

    results = pd.DataFrame({},columns=[
                        'original_category',
                        'category',
                        'description',
                        'carbohydrate',
                        'protein',
                        'fat',
                        'kilocalories',
                        'feedback'])
    processed_categories = set()
    feedback = 'in esecuzione'
    while  feedback != 'interrotto':
        # Seleziona una categoria specifica random tra quelle non ancora processate
        remaining_categories = set(
            categories_df[categories_df['stato'] == 'da verificare']['category']) - processed_categories
       
        if not remaining_categories:
            print("Non ci sono più categorie valide da processare.")
            break

        category = np.random.choice(list(remaining_categories))
        
        # Trova il miglior alimento per questa categoria
        food_list = df[df['category'] == category]
        #generic_categories.get(category,[])
        condition= categories_df[categories_df['category'] == category]['stato'] == 'da verificare'
        while   condition.any() and feedback != 'interrotto' :
            
            best_food,food_list ,category= find_best_food(df, category,food_list ,remaining_categories,categories_df)
            if best_food is not None:
                # Richiedi feedback sull'alimento proposto
                final_food, feedback,category = request_feedback(category, best_food, df, food_list, evaluated_food_ids,remaining_categories,categories_df)
                if feedback == 'approvato' and final_food is not None:
                    new_rows = pd.DataFrame({
                       'original_category': category,
                        'category': final_food['category'],
                        'description': final_food['description'],
                        'carbohydrate': final_food['carbohydrate'],
                        'protein': final_food['protein'],
                        'fat': final_food['fat'],
                        'kilocalories': final_food['kilocalories'],
                        'feedback': feedback
                    })
                    #Se l'alimento è approvato, aumentiamo il contatore per la categoria , = 1
                    results = pd.concat([results, new_rows], ignore_index=True)
                    categories_df.loc[categories_df['category'] == category,'accettati'] = 1
                    evaluated_food_ids.append(final_food['id'])

                    # Se abbiamo trovato 5 alimenti approvati per questa categoria, la consideriamo completata
                    cond=results[(results['category'] == category) & (results['feedback']== 'approvato')]
                    if len(cond) == 5:
                        categories_df.loc[categories_df['category'] == category, 'stato'] = 'completata'
                        processed_categories.add(category)
                        break
                        
                if feedback == 'rifiutato' and final_food is not None:
                    new_rows = pd.DataFrame({
                        'original_category': category,
                        'category': final_food['category'],
                        'description': final_food['description'],
                        'carbohydrate': final_food['carbohydrate'],
                        'protein': final_food['protein'],
                        'fat': final_food['fat'],
                        'kilocalories': final_food['kilocalories'],
                        'feedback': feedback
                    })
                    # Aggiungi le nuove righe usando concat
                    results = pd.concat([results, new_rows], ignore_index=True)
                    evaluated_food_ids.append(final_food['id'])
                    categories_df.loc[categories_df['category'] == category,'rifiutati'] = 1
                    print(results)
                    
        else:
            print(f"Nessun alimento nutriente trovato per '{category}'. Ignorando questa categoria.")
            categories_df.loc[categories_df['category'] == category, 'stato'] = 'ignora'
            processed_categories.add(category)
    
    # Crea un DataFrame con i risultati
    
    results_df=results

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
