import pandas as pd
from backtracking import backtracking_search

def getCsp(protein_g,carb_g,fat_g):

    df = pd.read_csv('/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/prepared-food-data-for-category.csv')
    # Definizione degli alimenti con i relativi macronutrienti
   

    # Vincoli sui macronutrienti
    target_carbs = carb_g
    target_proteins = protein_g
    target_fats = fat_g

    # Variabili
   

    # Vincoli
    def constraint_carb(target_carbs):
        total_food = 0
        for food in df['carbohydrate']:
            total_food += food
            print(total_food)
            if food == target_carbs:
                
                return True
        return False      

    def constraint_protein(target_proteins):
        for food in df['protein']: 
            if food == target_proteins:
                return True
        return False   

    def constraint_fat(target_fats):
        for food in df['fat']:
            if food == target_fats:
                return True
        return False   

   

    df = pd.read_csv('/Users/i4c0ni99/UNIVAQ/develop/FoodAI/csv/prepared-food-data-for-category.csv')
    csp = {
    'variables': ['carbs','proteins','fats'],
    'domains': {
        'carbs': df[df['carbohydrate'] >= 35],
        'proteins': df[df['protein'] >= 45],
        'fats': df[df['fat'] >= 35]
    },
    'constraints': [
        lambda  val: constraint_carb(  target_carbs),
        lambda  val: constraint_protein(  target_proteins),
        lambda  val: constraint_fat(  target_fats),
    ]}

    return backtracking_search(csp)