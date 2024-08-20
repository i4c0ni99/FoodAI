from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from trainingML import trainerPranzo

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
            

@app.post("/goals/")
async def create_item(requestFE: ReqeustFE):
    if requestFE.pranzo:
        
        return [{'pranzo':trainerPranzo(requestFE.pranzo,requestFE.aliments)}]
        
    return "non ci sono risposte dal server"
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
