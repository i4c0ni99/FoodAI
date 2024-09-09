import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

input_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/prepared_dataset.csv'
df = pd.read_csv(input_file)

# Filtra per escludere alimenti con un contenuto di carboidrati, proteine o grassi superiore a 80
df_filtered = df[df['carbohydrate'] < 80]
df_filtered = df_filtered[df_filtered['protein'] < 80]
df_filtered = df_filtered[df_filtered['fat'] < 80]

# Penalizza il contenuto di zucchero semplice
if 'sugar' in df_filtered.columns:
    df_filtered['sugar_penalty'] = df_filtered['sugar'] * 2.5  # Penalità per ogni grammo di zucchero
else:
    df_filtered['sugar_penalty'] = 0  

# Aggiungi un bonus per la presenza di fibre
if 'fiber' in df_filtered.columns:
    df_filtered['fiber_bonus'] = df_filtered['fiber'] * 4  # Peso elevato per ogni grammo di fibra
else:
    df_filtered['fiber_bonus'] = 0  

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

# Divisione dei dati in training (80%) e test set (20%)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Addestramento del modello di regressione lineare
model = LinearRegression()
model.fit(X_train, y_train)

# Calcolo del punteggio nutrizionale per l'interoil dataset
df_filtered['nutritional_score'] = model.predict(X_scaled)

output_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/new_data.csv'
df_filtered.to_csv(output_file, index=False)
print(df_filtered)

# Filtra gli alimenti con un punteggio di nutrizionalità pari o superiore a 70 per verificare i risultati
nutritional_foods = df_filtered[df_filtered['nutritional_score'] >= 70]
print(nutritional_foods[['description', 'carbohydrate', 'protein']])

# Gli alimenti con alto punteggio in un file CSV separato
output_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/maximo.csv'
nutritional_foods.to_csv(output_file, index=False)

print(f"I risultati sono stati salvati in {output_file}")