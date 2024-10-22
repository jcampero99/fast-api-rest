Código para crear tablas en PostgreSQL

CREATE TABLE users (
    id SERIAL PRIMARY KEY,                    -- Llave primaria autoincremental
    username VARCHAR(255) NOT NULL,           -- Nombre de usuario como cadena de texto
    useremail VARCHAR(255) NOT NULL UNIQUE,   -- Email del usuario, debe ser único
    credit_card_number VARCHAR(20) NOT NULL,  -- Número de tarjeta de crédito como texto
    created_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Marca de tiempo de creación con valor por defecto de la hora actual
);


//Script PARA INSERTAR USUARIOS

INSERT INTO users (username, useremail, credit_card_number)
VALUES 
('JohnDoe', 'john@example.com', '1234-5678-9101-1121'),
('JaneDoe', 'jane@example.com', '4321-5678-9101-1112'),
('MikeSmith', 'mike@example.com', '5678-1234-9101-2111'),
('AnnaTaylor', 'anna@example.com', '9876-4321-5678-1110'),
('ChrisJohnson', 'chris@example.com', '1111-2222-3333-4444'),
('EmilyBrown', 'emily@example.com', '5555-6666-7777-8888'),
('DavidWhite', 'david@example.com', '9999-8888-7777-6666'),
('SarahGreen', 'sarah@example.com', '1111-2222-9999-8888'),
('DanielLee', 'daniel@example.com', '3333-4444-5555-6666'),
('LauraMartinez', 'laura@example.com', '1234-5555-6666-7777');




/////
Github Push


echo "# fast-api-rest" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/jcampero99/fast-api-rest.git
git push -u origin main