from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession # Se importan las funciones 'create_async_engine' y 'AsyncSession' para configurar el motor de dc y las sesiones con la db de manera asíncrona 
from sqlalchemy.orm import sessionmaker, declarative_base  # Se importa 'sessionmaker' para crear una fabrica de sesiones de db y 'declarative_base' para difinimr las clases bases de los modelos de la db 

# Conexion a PostgreSQL --- 'asyncpg' se usa para conexiones asíncronas
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:123456789@localhost:5432/fastapi-rest-test"

# Crear el motor de base de datos asíncrono con la url de conexión definida
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Crear sesión asíncrona para interactuar con la base de datos 
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False )

# Definir la clase base para los modelos
Base = declarative_base()

# Función para obtener una sesión de la base de datos
async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
