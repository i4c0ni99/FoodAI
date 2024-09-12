
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from static.utils.calculateMacro import calculate_kal_macro
from static.utils.totalKalMacro import kilototal
from static.utils.totalKalMacro import totalCarb
from static.utils.totalKalMacro import totalFat
from static.utils.totalKalMacro import totalProt
from typing import List
import json


# Impostiamo Jinja2 per gestire i template HTML


from trainingML import trainerColazione
from trainingML import trainerSpuntino_mat
from trainingML import trainerPranzo
from trainingML import trainerSpuntino_pom
from trainingML import trainerCena
import sqlite3




conn = sqlite3.connect('/Users/lucavisconti/Documents/FoodAI/db/meal_plan.db')
c = conn.cursor()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Servire file statici (come CSS, immagini)
app.mount("/static", StaticFiles(directory="static"), name="static")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permetti tutte le origini, puoi specificare una lista di domini
    allow_credentials=True,
    allow_methods=["*"],  # Permetti tutti i metodi HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permetti tutte le intestazioni
)
userData= {}
colazione = None
spuntino_mat = None
pranzo = None
spuntino_pom = None
cena = None
user = {}
selected_categories= []
food_categories = [
          {
                "name": "Latticini",
                "category": "dairy",
                "img": "https://www.fondazioneveronesi.it/uploads/thumbs/2020/01/16/latte-latticini-dieta_thumb_720_480.jpg",
            }
            ,
            {
                "name": "Uova",
                "category": "eggs",
                "img": "https://www.curarsiconilcibo.com/wp-content/uploads/2021/03/UOVA.jpg",
            },
            {
                "name": "Oli e grassi",
                "category": "oilsFats",
                "img": "https://www.my-personaltrainer.it/2023/07/21/colesterolo-oli-e-grassi-orig.jpeg",
            },
            {
                "name": "Avicoli",
                "category": "poultry",
                "img": "https://www.chiappinellicarni.it/it/wp-content/uploads/2019/02/Le-vendite-della-carne-di-pollo-sorpassano-quelle-del-bovino-1-1.jpg",
            },
            {
                "name": "Carne",
                "category": "meats",
                "img": "https://www.my-personaltrainer.it/2023/10/31/carne-orig.jpeg",
            },
            {
                "name": "Cereali",
                "category": "cereals",
                "img": "https://lebarbarighe.it/wp-content/uploads/2017/11/cereali.jpg",
            },
            {
                "name": "Frutta",
                "category": "fruits",
                "img": "https://www.donnamoderna.com/content/uploads/2023/05/come-preparare-una-macedonia-di-frutta_800_resize.jpg",
            },
            {
                "name": "Verdura",
                "category": "vegetables",
                "img": "https://iberiana.es/wp-content/uploads/2024/01/shutterstock_2285898265-scaled.jpg",
                
            },
            {
                "name": "Legumi",
                "category": "legumes",
                "img": "https://ilfattoalimentare.it/wp-content/uploads/2014/10/legumi-iStock_000020447381_Small.jpg",
                
            },
            {
                "name": "Pesce",
                "category": "fish",
                "img": "https://www.my-personaltrainer.it/2021/03/23/proteine-del-pesce-orig.jpeg",
                
            },
            {
                "name": "Primi piatti",
                "category": "first dishes",
                "img": "https://media-assets.lacucinaitaliana.it/photos/6426da66217d19c609f6f4f8/3:2/w_2121,h_1414,c_limit/GettyImages-522387318.jpg",
                
            },
            {
                "name": "Frutta secca",
                "category": "nutsAndSeeds",
                "img": "https://aws.imagelinenetwork.com/agronotizie/materiali/ArticoliImg/frutta-in-guscio-frutta-secca-mista-by-luigi-giordano-adobe-stock-1200x800.jpeg",
                
                
            }
    # Aggiungi altre categorie qui
]

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    c.execute('SELECT * FROM daily_meal_plan ORDER BY id DESC')
    rows = c.fetchall()
    return templates.TemplateResponse("calculateMacro.html", {"request": request,"cronos":rows})

@app.post("/categories_list", response_class=HTMLResponse)
async def post_categories_list(request: Request,eta: int = Form(...), peso: float = Form(...), altezza: float = Form(...), goal: str = Form(...),stile_di_vita: str = Form(...)):
    global user
    user = {"eta":eta,"altezza":altezza,"peso":peso,"obbiettivo":goal,"stile_di_vita":stile_di_vita, "numero_di_pasti": 5}
    return templates.TemplateResponse("category_selection.html", {"request": request, "categories": food_categories})

@app.get("/crono_day", response_class=HTMLResponse)
async def get_crono(request: Request):
    c.execute('SELECT * FROM daily_meal_plan where id ='request.hea)
    return templates.TemplateResponse("meal_plan.html",
            {   
        "colazione":colazione,
        "spuntino_mat":spuntino_mat,
        "pranzo":pranzo,
        "spuntino_pom": spuntino_pom,
        "cena": cena,
        "kal_target": userData["tdee"],
        "totalKal": totalKal,
        "totalCarb": totalCarb(colazione,spuntino_mat,pranzo,spuntino_pom,cena),
        "totalFat":  totalFat(colazione,spuntino_mat,pranzo,spuntino_pom,cena),
        "totalProt": totalProt(colazione,spuntino_mat,pranzo,spuntino_pom,cena),
        "carb_g": userData['carb_g'],
        "protein_g":userData['protein_g'], 
        "fat_g":userData['fat_g'],
        })  
   
    

@app.get("/daily_diet", response_class=HTMLResponse)
async def post_categories(request: Request):
    global colazione
    global spuntino_mat
    global pranzo
    global spuntino_pom
    global cena
    global userData
    # Qui potremmo elaborare i dati e mostrarli all'utente o passare alla pagina successiva
    tdee = calculate_kal_macro(user)
    userData= {"tdee" : tdee['tdee'],
    "carb_g": tdee['carb_g'],
    "protein_g":tdee['protein_g'], 
    "fat_g":tdee['fat_g'], 
    "cena":tdee['pasti']['cena'],
    "colazione":tdee['pasti']['colazione'],
    "pranzo":tdee['pasti']['pranzo'],
    "spuntino_mat":tdee['pasti']['spuntino_mat'],
    "spuntino_pom":tdee['pasti']['spuntino_pom'],
    "aliments": selected_categories,
    "meal" : " ",
    "assignment" : {} }
    
    
    while  True :
        colazione=trainerColazione(userData['colazione'],userData['aliments'],None)
        spuntino_mat=trainerSpuntino_mat(userData['spuntino_mat'],userData['aliments'],None)
        pranzo=trainerPranzo(userData['pranzo'],userData['aliments'],None)
        spuntino_pom= trainerSpuntino_pom(userData['spuntino_pom'],userData['aliments'],None)
        cena= trainerSpuntino_pom(userData['cena'],userData['aliments'],None)
        totalKal= kilototal(colazione,spuntino_mat,pranzo,spuntino_pom,cena)
        if totalKal and totalKal  - userData['tdee'] <=  totalKal * 0.025: 
            print ({totalKal,"entrato",userData["tdee"]})
            return templates.TemplateResponse("meal_plan.html",
                        {
                    "request":request,   
                    "colazione":colazione,
                    "spuntino_mat":spuntino_mat,
                    "pranzo":pranzo,
                    "spuntino_pom": spuntino_pom,
                    "cena": cena,
                    "kal_target": userData["tdee"],
                    "totalKal": totalKal,
                    "totalCarb": totalCarb(colazione,spuntino_mat,pranzo,spuntino_pom,cena),
                    "totalFat":  totalFat(colazione,spuntino_mat,pranzo,spuntino_pom,cena),
                    "totalProt": totalProt(colazione,spuntino_mat,pranzo,spuntino_pom,cena),
                    "carb_g": userData['carb_g'],
                    "protein_g":userData['protein_g'], 
                    "fat_g":userData['fat_g'],
                    })  
  
  
@app.post("/submit", response_class=HTMLResponse)
async def post_loading(request: Request,categories: List[str] = Form(...)):
    global selected_categories
    print(categories)
    selected_categories = [json.loads(item.replace("'", '"')) for item in categories]
    print(selected_categories)
    return templates.TemplateResponse("loading.html", {"request": request})  

@app.get("/daily_diet_changed")
async def get_diet(request:Request):
    return templates.TemplateResponse("meal_plan.html",
                        {
                    "request":request,   
                    "colazione":colazione,
                    "spuntino_mat":spuntino_mat,
                    "pranzo":pranzo,
                    "spuntino_pom": spuntino_pom,
                    "cena": cena,
                    "kal_target": userData["tdee"],
                    "totalKal": kilototal(colazione,spuntino_mat,pranzo,spuntino_pom,cena),
                    "totalCarb": totalCarb(colazione,spuntino_mat,pranzo,spuntino_pom,cena),
                    "totalFat":  totalFat(colazione,spuntino_mat,pranzo,spuntino_pom,cena),
                    "totalProt": totalProt(colazione,spuntino_mat,pranzo,spuntino_pom,cena),
                    "carb_g": userData['carb_g'],
                    "protein_g":userData['protein_g'], 
                    "fat_g":userData['fat_g'],
                    })  
   
class RequestFE(BaseModel):
    
    meal : str
    assignment : dict
    
    

@app.post("/changeAliment/")
async def create_item(requestFE: RequestFE,request:Request):
    global colazione
    global spuntino_mat
    global spuntino_pom
    global pranzo
    global cena
    print(requestFE.assignment,requestFE.meal)
    if requestFE.meal == 'colazione' and colazione :
        colazione = trainerColazione(userData['colazione'],selected_categories,requestFE.assignment)
    if requestFE.meal == 'spuntino_mat' and spuntino_mat : 
        spuntino_mat=trainerSpuntino_mat(userData['spuntino_mat'],selected_categories,requestFE.assignment)   
    if requestFE.meal == 'pranzo' and pranzo : 
        pranzo=trainerSpuntino_mat(userData['pranzo'],selected_categories,requestFE.assignment)
    if requestFE.meal == 'spuntino_pom' and spuntino_pom : 
        spuntino_pom=trainerSpuntino_mat(userData['spuntino_pom'],selected_categories,requestFE.assignment)
    if requestFE.meal == 'cena' and cena : 
        cena=trainerSpuntino_mat(userData['cena'],selected_categories,requestFE.assignment)    
    return templates.TemplateResponse("meal_plan.html",
                        {
                    "request":request,   
                    "colazione":colazione,
                    "spuntino_mat":spuntino_mat,
                    "pranzo":pranzo,
                    "spuntino_pom": spuntino_pom,
                    "cena": cena,
                    "kal_target": userData["tdee"],
                    "totalKal": kilototal(),
                    "totalCarb": totalCarb(),
                    "totalFat":  totalFat(),
                    "totalProt": totalProt(),
                    "carb_g": userData['carb_g'],
                    "protein_g":userData['protein_g'], 
                    "fat_g":userData['fat_g'],
                    })    

 

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
