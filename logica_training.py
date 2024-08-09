import pandas as pd
import random



total = []

def matchConstraint(domain):
    global total
    total_protein = domain['protein'].sum()
    total_fat = domain['fat'].sum()
    total_carbohydrate = domain['carbohydrate'].sum()    
    return {'domain': domain,
            'proteins':total_protein,
            'carbs':total_carbohydrate,
            'fats':total_fat}

                
        
        
def calculate_difference(combination, target_protein, target_fat, target_carbohydrate,i,df):
   
    selected_data = df.iloc[combination]
    global total
    # Calcola la somma delle proprietà selezionate
    total_macro= matchConstraint(selected_data)
    total_protein=total_macro[1]
    total_fat=total_macro[3]
    total_carbohydrate = total_macro[2]
    # Calcola la differenza rispetto ai target
    diff_protein = abs(total_protein - target_protein)
    diff_fat = abs(total_fat - target_fat)
    diff_carbohydrate = abs(total_carbohydrate - target_carbohydrate)

    # La differenza totale è la somma delle differenze individuali
    total_diff = diff_protein + diff_fat + diff_carbohydrate
    return total_diff, total_protein, total_fat, total_carbohydrate, selected_data['description'].tolist()

def find_best_combination(target_protein, target_fat, target_carbohydrate, num_combinations, comb_size,df,var):
    
    global total
    total.append(var)
    min_diff = float('inf')
    best_combination = None
    best_total_protein = 0
    best_total_fat = 0
    best_total_carbohydrate = 0
    best_description = []

    all_indices = list(range(len(df)))
    i = 0
    size_total = len(total) 
    
    counter=0
    while counter <= num_combinations  and i == len(total):
        
        combination = random.sample(all_indices, comb_size)
        if counter == num_combinations :
            counter = 0
            i+=1
            
            
            

        try:
            diff, total_protein, total_fat, total_carbohydrate, descriptions = calculate_difference(
                combination, target_protein, target_fat, target_carbohydrate, i,df
            )
            if diff < min_diff:
                min_diff = diff
                best_combination = combination
                best_total_protein = total_protein
                best_total_fat = total_fat
                best_total_carbohydrate = total_carbohydrate
                best_description = descriptions
        except IndexError:
            continue
        counter+=1 
    return best_combination, best_total_protein, best_total_fat, best_total_carbohydrate, best_description,
    

""" def main():
    # Carica il dataset
    

    # Richiedi input da tastiera per i target di macronutrienti
    target_protein = float(input("Inserisci il target per le proteine (in grammi): "))
    target_fat = float(input("Inserisci il target per i grassi (in grammi): "))
    target_carbohydrate = float(input("Inserisci il target per i carboidrati (in grammi): "))
    num_combinations = 25000  # Numero fisso di combinazioni da testare
    comb_size = int(input("Inserisci la dimensione della combinazione (2 o 3): "))

    if comb_size not in [2, 3]:
        print("La dimensione della combinazione deve essere 2 o 3.")
        return

    best_combination, best_total_protein, best_total_fat, best_total_carbohydrate, best_description = find_best_combination(
        target_protein, target_fat, target_carbohydrate, df, num_combinations, comb_size
    )

    if best_combination is not None:
        print("Migliore combinazione di alimenti:")
        for description in best_description:
            print(description)
        print(f"\nTotale proteine: {best_total_protein} grammi")
        print(f"Totale grassi: {best_total_fat} grammi")
        print(f"Totale carboidrati: {best_total_carbohydrate} grammi")
    else:
        print("Nessuna combinazione valida trovata.")

if __name__ == "__main__":
    main() """
