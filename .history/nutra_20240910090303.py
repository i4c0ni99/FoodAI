import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
   mean_squared_error, mean_absolute_error, r2_score,
    median_absolute_error, mean_absolute_percentage_error,
    explained_variance_score, max_error, mean_squared_log_error
)

# Dizionario di mapping delle categorie "duplicate"
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

# Funzione per sostituire le categorie
def replace_category(category, mapping_dict):
    for key, values in mapping_dict.items():
        if category in values:
            return key
    return category

# Funzione per aggiornare le categorie nel CSV
def update_categories_in_csv(input_file, output_file, category_col='category'):
    df = pd.read_csv(input_file)

    # Sostituisci le categorie utilizzando il dizionario
    df[category_col] = df[category_col].apply(lambda x: replace_category(x, mapping))

    # Salva il file aggiornato
    df.to_csv(output_file, index=False)
    print(f"File aggiornato salvato in: {output_file}")

# Definizione dei file di input e output per l'aggiornamento delle categorie
input_file = '/Users/lucavisconti/Documents/FoodAI/csv/prepared_food_data.csv'  
output_file = '/Users/lucavisconti/Documents/FoodAI/csv/prepared_dataset.csv' 

# Esegui l'aggiornamento delle categorie
update_categories_in_csv(input_file, output_file)

# Continua con l'elaborazione dei dati e il modello di regressione
input_file = '/Users/lucavisconti/Documents/FoodAI/csv/prepared_dataset.csv'
df = pd.read_csv(input_file)

# Filtra per escludere alimenti con un contenuto di carboidrati, proteine o grassi superiore a 80
df_filtered = df[df['carbohydrate'] < 80]
df_filtered = df_filtered[df_filtered['protein'] < 80]
df_filtered = df_filtered[df_filtered['fat'] < 80]

# Penalizza il contenuto di zucchero semplice e aggiungi un bonus per la presenza di fibre
df_filtered['sugar_penalty'] = df_filtered['sugar'] * 2.5 if 'sugar' in df_filtered.columns else 0  
df_filtered['fiber_bonus'] = df_filtered['fiber'] * 4 if 'fiber' in df_filtered.columns else 0  

# Definisci X (caratteristiche) e y (target sintetico, basato sulle caratteristiche selezionate)
X = df_filtered[['carbohydrate', 'fat', 'protein', 'kilocalories', 'sugar_penalty', 'fiber_bonus']]

# Calcola il punteggio nutrizionale sintetico:
# - Proteine (+) sono considerate positive.
# - Fibre (+) hanno un grande peso positivo per migliorare il punteggio.
# - Zuccheri (-) sono penalizzati.
# - Kilocalorie (-) sono penalizzate, ma con un peso moderato.
# - Grassi (-) sono penalizzati, ma non in modo eccessivo.
y = (df_filtered['protein'] * 3) + df_filtered['fiber_bonus'] - (df_filtered['fat'] * 1.5) - (df_filtered['kilocalories'] * 0.5) - df_filtered['sugar_penalty']

# Normalizza il punteggio per avere valori compresi tra 0 e 100
y = (y - y.min()) / (y.max() - y.min()) * 100

# Normalizzazione dei dati
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Divisione dei dati di training e test set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Addestramento del modello di regressione lineare
model = LinearRegression()
model.fit(X_train, y_train)

# Calcolo del punteggio nutrizionale per l'intero dataset
df_filtered['nutritional_score'] = model.predict(X_scaled)

# Previsione sui dati di test
y_pred = model.predict(X_test)

# Calcolo delle metriche
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mse)
medae = median_absolute_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)
explained_var = explained_variance_score(y_test, y_pred)
max_err = max_error(y_test, y_pred)
msle = mean_squared_log_error(y_test, y_pred)

# Stampa delle metriche
print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"Median Absolute Error (MedAE): {medae}")
print(f"Mean Absolute Percentage Error (MAPE): {mape}")
print(f"R-squared (R2): {r2}")
print(f"Explained Variance: {explained_var}")
print(f"Max Error: {max_err}")
print(f"Mean Squared Log Error (MSLE): {msle}")

# Salvataggio delle metriche in un file di testo
with open('model_metrics.txt', 'w') as f:
    f.write(f"Mean Squared Error (MSE): {mse}\n")
    f.write(f"Mean Absolute Error (MAE): {mae}\n")
    f.write(f"Root Mean Squared Error (RMSE): {rmse}\n")
    f.write(f"Median Absolute Error (MedAE): {medae}\n")
    f.write(f"Mean Absolute Percentage Error (MAPE): {mape}\n")
    f.write(f"R-squared (R2): {r2}\n")
    f.write(f"Explained Variance: {explained_var}\n")
    f.write(f"Max Error: {max_err}\n")
    f.write(f"Mean Squared Log Error (MSLE): {msle}\n")

# Grafico valori reali e predetti
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Valori Reali')
plt.ylabel('Valori Predetti')
plt.title('Confronto tra Valori Reali e Predetti')
plt.grid(True)
plt.savefig('/Users/lucavisconti/Documents/FoodAI/stats/confronto_reali_predetti.png')
plt.show()

# Grafico errori residui
residuals = y_test - y_pred
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, residuals, alpha=0.6)
plt.hlines(y=0, xmin=y_pred.min(), xmax=y_pred.max(), color='red', linestyle='--')
plt.xlabel('Valori Predetti')
plt.ylabel('Residui')
plt.title('Grafico dei Residui')
plt.grid(True)
plt.savefig('/Users/lucavisconti/Documents/FoodAI/stats/residui.png')
plt.show()

# Istogramma errori
plt.figure(figsize=(8, 6))
plt.hist(residuals, bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribuzione degli Errori')
plt.xlabel('Errore Residuo')
plt.ylabel('Frequenza')
plt.grid(True)
plt.savefig('/Users/lucavisconti/Documents/FoodAI/stats/distribuzione_errori.png')
plt.show()

# Dispersione feature rispetto nutritional score
features = ['carbohydrate', 'fat', 'protein', 'kilocalories', 'sugar_penalty', 'fiber_bonus']
for feature in features:
    plt.figure(figsize=(8, 6))
    plt.scatter(df_filtered[feature], df_filtered['nutritional_score'], alpha=0.5)
    plt.title(f'Impatto di {feature} sul punteggio nutrizionale')
    plt.xlabel(feature)
    plt.ylabel('Punteggio nutrizionale')
    plt.grid(True)
    plt.savefig(f'{feature}_vs_nutritional_score.png')
    plt.show()
