from sqlalchemy import Column, Integer, String, DateTime # Se importan las clases 'Column', 'Integer', 'String' y 'DateTime', que permiten definir las columnas y sus tipos en la db 
from sqlalchemy.sql import func # Se importa 'func', permite acceder a funciones que permiten establecer valores por defecto (now)
from app.db.database import Base # Se importa 'Base' la clase base para los modelos. Los modelos de base de datos deben heredar de esta clase que sean mapeados 

# Se define la clase 'User', representa el modelo de la tabla 'users' en la db.
class User(Base):
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True, autoincrement=True) # se define la columna 'id' como clave primaria
    name = Column(String, index=True) # almacena el nombre de usuario
    useremail = Column(String) # almacena el correo electrónico
    credit_card_number = Column(String) # almacena el número de CD
    created_timestamp = Column(DateTime(timezone=True), server_default=func.now()) # almacena la fecha y hora de creación del usuario
