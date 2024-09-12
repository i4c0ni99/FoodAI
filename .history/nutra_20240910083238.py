import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

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








































nalty']







































