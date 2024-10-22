from app.db import models   # Se importan los modelos de la base de datos desde 'app.db.models', definen la estructura de las tablas en las base de datos utilizando 'Sqlalchemy'.
from fastapi import APIRouter, Depends   # Se importa 'APIRouter' para crear rutas agrupadas y 'Depends' para la inyección de dependencias, esto permite gestionar el acceso a la base de datos a través de funciones compartidas. 
from sqlalchemy.ext.asyncio import AsyncSession   # Se importa 'AsyncSession' para manejar las operaciones asíncronas con las db  utilizando 'Sqlalchemy'.
from sqlalchemy.future import select   # Se importa 'select' para construir consultas SQL de forma declarativa 
from app import schemas   # Se importan los esquemas de validación de datos'schemas',  definen la estructura de los datos de entrada y salida de la API.
from app.db.database import get_db   # Se importa la función 'get_db', proporciona unasesión asíncrona para interactuar con la db.   
                                     # Se usa como una dependencia en los endpoints para obtener y manejar la sesión de la db.

router = APIRouter(   # Se crea instancia de APIRouter
    prefix="/api/v1",   # Prefijo que tendrán todos los endopint definidos en este router, lo cual permite versionar la API
    tags=["users"]      # Tag que ayuda a organizar y agrupar todos los endpóints relacionados 
)

# Endpoints

# Endpoint para crear un usuario.
# Se recibe un esquema 'UserCreate', se guarda en la base de datos y se devuelve el usario creado.
# La conexión a la db es gestionada por 'get_db', que proporciona una sesión, en este caso asíncrona
@router.post("/post-users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)): 
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user   # Objeto 'User' con los datos del usuario creado. 



# Endpoint para obtener todos los usuarios
# Devuelve una lista de todos los usuarios almacenados en la db
# La conexión a la db es gestionada por 'get_db', que proporciona una sesión, en este caso asíncrona
@router.get("/get-users/", response_model=list[schemas.User])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User))
    users = result.scalars().all()
    return users # Lista de objetos 'User' que representa a todos los usuarios creados.

