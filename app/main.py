from fastapi import FastAPI
from app.api.v1.user import router

# Créer une instance de l'application FastAPI
app = FastAPI()

# Définir une route
@app.get("/")
def read_root():
    return {"message": "Hello, World"}

app.include_router(router)