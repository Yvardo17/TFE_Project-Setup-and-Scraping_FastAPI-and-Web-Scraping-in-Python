from fastapi import FastAPI
import uvicorn
import services as _services

app= FastAPI()

@app.get("/")
async def root():
    return {"Message": "Bienveniue dans le pipeline de données"}

@app.get("/taille")
async def all_tailles():
    return _services.get_all_data()

@app.get("/intervaleData/{nbre}")
async def get_data_pour_nbre(nbre: int):
    return _services.get_donner_nbre(nbre)