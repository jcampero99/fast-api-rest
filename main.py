from fastapi import FastAPI # Se importa la clase FastAPI, instancia principal para crear aplicación web con capacidad de manejar peticiones HTTP
import uvicorn # Se importa uvicorn, servidor ASGI (Asynchronous Server Gateway Interface) que permite ejecutar la aplicación de manera asincróna y manejar conexiones simultáneas
from app.db.database import engine, Base   # Se importan 'engine' y 'Base' desde el módulo 'database' / importacion de funciones con base en la ruta app.db.database
from app import users   # Se importa el módulo 'users' que contiene el router de endpoints relacionado a la gestión de usuarios 

app = FastAPI()   # Instancia de la clase 'FastAPI' que inicializa la app, se utiliza para gestionar las rutas y los endpoints de la API

# Fución encarga de crear tablas en la db
def create_tables():
    Base.metadata.create_all(bind=engine)

# Se incluye el router de usuarios 'users' dentro de la app, esto permite que los usuarios acceder a la API
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
