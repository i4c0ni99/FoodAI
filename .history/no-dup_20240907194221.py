import pandas as pd

# Dizionario di mapping delle categorie 
mapping = {
    'ICE CREAM': ['ICE CREAM', 'ICE CREAMS', 'ICE CRM CONES', 'LIGHT ICE CRM'],
    'BROCCOLI': ['BROCCOLI', 'BROCCOLI RAPE', 'BROCCOLI RABE'],
    'EGG': ['EGG', 'Egg', 'EGG SUBSTITUTE', 'EGG MIX'],
    'SHORTENING': ['SHORTENING', 'SHORTENING BREAD', 'SHORTENING FRYING (REG)', 'SHORTENING CAKE MIX',
                   'SHORTENING FRYING (HVY DUTY)', 'SHORTENING CONFECTIONERY', 'SHORTENING FRYING HVY DUTY',
                   'SHORTENING INDUSTRIAL'],
    'TURKEY': ['TURKEY AND GRAVY', 'TURKEY PATTIES', 'TURKEY BREAST', 'TURKEY THIGH', 'TURKEY RST',
               'TURKEY STKS'],
    'CHICKEN': ['CHICKEN NUGGETS', 'CHICKEN PATTY', 'CHICKEN BREAST TENDERS', 'USDA CMDTY CHICK', 'USDA CMDTY'],
    'BEEF': ['BEEF', 'BF'],
    'WURSTEL': ['BRATWURST', 'BRAUNSCHWEIGER (A LIVER SAUSAGE)', 'BROTWURST'],
    'SAUSAGE': ['PORK SAUSAGE', 'PORK&BF SAUSAGE', 'TURKEY SAUSAGE', 'CHORIZO', 'LIVER SAUSAGE', 'SAUSAGE',
                'POLISH SAUSAGE', 'HONEY ROLL SAUSAGE', 'LUNCHEON SAUSAGE', 'NEW ENGLAND BRAND SAUSAGE',
                'SMOKED LINK SAUSAGE', 'BEEF SAUSAGE', 'PORK & TURKEY SAUSAGE'],
    'CEREALS': ['CEREALS RTE', 'CEREALS', 'CEREALS READY TO EAT', 'CERLS', 'CEREAL WAFER STRAWS'],
    'CRANBERRIES': ['CRANBERRIES', 'CRANBERRY SAU', 'CRANBERRY-ORANGE RELISH'],
    'GRAPEFRUIT': ['GRAPEFRUIT', 'GRAPES'],
    'MELON': ['MELON', 'MELONS', 'MELON BALLS'],
    'LIME JUICE': ['LIME JUICE', 'LIME JUC'],
    'LEMON JUICE': ['LEMON JUICE', 'LEMON JUC'],
    'ORANGE JUICE': ['ORANGE JUICE', 'ORANGE JUC'],
    'TANGERINE JUICE': ['TANGERINE JUICE', 'TANGERINE JUC'],
    'PUDDING': ['PUDDING', 'PUDDINGS']
}

def replace_category(category, mapping_dict):
    for key, values in mapping_dict.items():
        if category in values:
            return key
    return category

def update_categories_in_csv(input_file, output_file, category_col='category'):
    # Leggi il file CSV
    df = pd.read_csv(input_file)

    # Sostituisci le categorie utilizzando il dizionario
    df[category_col] = df[category_col].apply(lambda x: replace_category(x, mapping))

    # Salva il file aggiornato
    df.to_csv(output_file, index=False)
    print(f"File aggiornato salvato in: {output_file}")

# Esempio di utilizzo
input_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/prepared_food_data.csv'  # Sostituisci con il nome del tuo file di input
output_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/prepared_dataset.csv'  # Sostituisci con il nome del file di output desiderato

update_categories_in_csv(input_file, output_file)
