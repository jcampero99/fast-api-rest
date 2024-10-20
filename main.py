from fastapi import FastAPI
import uvicorn
from app.db.database import engine, Base #importacion de funciones con base en la ruta app.db.database
from app import users # importar el router de usuarios 

app = FastAPI()

# Crear tablas 
def create_tables():
    Base.metadata.create_all(bind=engine)

# Incluir el router de usuarios
app.include_router(users.router)

# Endpoint de prueba para testear la app

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI está funcionando!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
