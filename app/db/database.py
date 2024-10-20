from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Conexion a PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:123456789@localhost:5432/fastapi-rest-test"

# Crear el motor de base de datos asíncrono
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crear sesión asíncrona para interactuar con la base de datos 
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False )

# Definir la base para los modelos
Base = declarative_base()

# Función para obtener una sesión de la base de datos
async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
