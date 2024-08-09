import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Step 1: Caricamento del dataset
input_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/prepared-food-data.csv'
df = pd.read_csv(input_file)

# Step 2: Preparazione dei dati
# Seleziona le colonne che rappresentano le caratteristiche nutrizionali

# Filtro per escludere alimenti con un contenuto di carboidrati o proteine superiore a 85
df_filtered = df[( df['carbohydrate'] < 80)]

df_filtered = df_filtered[df_filtered['protein']< 80]
df_filtered = df_filtered[df_filtered['fat']< 80]


#Definisci X (caratteristiche) e y (target sintetico basato sulle caratteristiche selezionate)
X = df_filtered[['carbohydrate','fat','protein','kilocalories']]

# Per scopi dimostrativi, il target è una somma ponderata di alcune caratteristiche.
# Qui consideriamo proteine e carboidrati come nutrienti positivi, mentre grassi e calorie come nutrienti negativi.
y = abs(df_filtered['carbohydrate'] + df_filtered['protein'] - (df_filtered['fat'] + df_filtered['kilocalories'] * 0.01))

# Step 3: Normalizzazione dei dati
# È una buona pratica normalizzare le caratteristiche prima di applicare la regressione lineare
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Divisione dei dati in training e test set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 5: Addestramento del modello di regressione lineare
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Calcolo del punteggio di nutrizionalità per tutto il dataset
# Utilizza il modello per predire il punteggio di nutrizionalità su tutto il dataset
df_filtered['nutritional_score'] = model.predict(X_scaled)

# Aggiungi la colonna del punteggio al dataset originale
df = df.merge(df_filtered[['nutritional_score']], left_index=True, right_index=True, how='left')

# Step 7: Salvataggio del dataset con il nuovo punteggio
output_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/new_data.csv'
df.to_csv(output_file, index=False) 
print(df_filtered)
df = pd.read_csv(output_file)

high_carb_protein_foods = df[(df['carbohydrate'] >= 80) | (df['protein'] >= 80) | (df['fat'] >= 80)]

print(high_carb_protein_foods[['description', 'carbohydrate', 'protein']])

output_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/maximo.csv'
high_carb_protein_foods.to_csv(output_file, index=False)

print(f"I risultati sono stati salvati in {output_file}")
print(f"Il dataset con il punteggio di nutrizionalità è stato salvato in {output_file}")
