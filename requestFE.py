from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from trainingML import trainerColazione
from trainingML import trainerSpuntino_mat
from trainingML import trainerPranzo
from trainingML import trainerSpuntino_pom
from trainingML import trainerCena

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permetti tutte le origini, puoi specificare una lista di domini
    allow_credentials=True,
    allow_methods=["*"],  # Permetti tutti i metodi HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permetti tutte le intestazioni
)
class ReqeustFE(BaseModel):
    tdee: float
    carb_g: float
    protein_g: float
    fat_g: float
    cena:float
    colazione:float
    pranzo:float
    spuntino_mat:float
    spuntino_pom:float
    aliments:list
            

@app.post("/colazione/")
async def create_item(requestFE: ReqeustFE):
    if requestFE.pranzo:
        print({'meal':trainerColazione(requestFE.colazione,requestFE.aliments)})
        return {'meal':trainerColazione(requestFE.colazione,requestFE.aliments)}
        
    return "non ci sono risposte dal server"    

@app.post("/spuntino_mat/")
async def create_item(requestFE: ReqeustFE):
    if requestFE.pranzo:
        
        return {'meal':trainerSpuntino_mat(requestFE.spuntino_mat,requestFE.aliments)}
        
    return "non ci sono risposte dal server"    


@app.post("/pranzo/")
async def create_item(requestFE: ReqeustFE):
    if requestFE.pranzo:
        
        return {'meal':trainerPranzo(requestFE.pranzo,requestFE.aliments)}
        
    return "non ci sono risposte dal server"

@app.post("/spuntino_pom/")
async def create_item(requestFE: ReqeustFE):
    if requestFE.pranzo:
        
        return {'meal':trainerSpuntino_pom(requestFE.spuntino_pom,requestFE.aliments)}
        
    return "non ci sono risposte dal server"  

@app.post("/cena/")
async def create_item(requestFE: ReqeustFE):
    if requestFE.pranzo:
        
        return {'meal':trainerCena(requestFE.cena,requestFE.aliments)}
        
    return "non ci sono risposte dal server"  


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
