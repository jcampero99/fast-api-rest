from pydantic import BaseModel   # Se importa 'BaseModel' de pydantic, para definirt esquemas que validarán y transformarán los datos de la API. Pydantic permite asegurarse que los datos tengan en formato adecuado. 
from datetime import datetime    # Se importa 'datetime' para manejar campos relacionados con marcas de tiempo en los esquemas de los usuarios. 

# Se define el esquema 'UserCreate', se utiliza para validar los datos de entrada cuando se crea un nuevo usuario
class UserCreate (BaseModel):
    username: str   # Nombre de usuario
    useremail: str  # Correo electrónico
    credit_card_number: str # Número de tarjeta de crédito

# Se define el esquema 'User' parala validación de datos en las respuestas relacionadas con los usuarios. para respuestas de usuarios 
class User(BaseModel):
    id: int # Identificador del usuarios
    username: str # Nombre de usuario
    useremail: str # Correo electrónico
    credit_card_number: str # Número de tarjeta de crédito
    created_timestamp: datetime # Marca de tiempo creación de usuario

    class Config: # Se habilita 'orm_mode' que permite que los esquemas se puedan usar directamente con los modelos de db
        orm_mode = True

    



