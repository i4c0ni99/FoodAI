import pandas as pd

input_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/new_data.csv'
df = pd.read_csv(input_file)

high_carb_protein_foods = df[(df['carbohydrate'] >= 80) | (df['protein'] >= 80) | (df['fat'] >= 80)]

print(high_carb_protein_foods[['description', 'carbohydrate', 'protein']])

output_file = '/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/maximo.csv'
high_carb_protein_foods.to_csv(output_file, index=False)

print(f"I risultati sono stati salvati in {output_file}")
