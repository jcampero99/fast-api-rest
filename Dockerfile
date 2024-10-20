# Usamos la imagen base de python 3.12 -slim
FROM python:3.12-slim

# Se establece el directorio de trabajo dentro del contenedor
WORKDIR /app


#Se instalan las dependencias necesarias
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

# Se copia todo el código de la aplicación al contenedor 
COPY . .

#Se expone el puerto en el que corre FastAPi
EXPOSE 8000

#Comando para correr la aplicación cojn uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]