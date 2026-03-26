# Taller 1 BD NoSQL - Clave Valor

Proyecto CRUD usando una base de datos NoSQL tipo clave-valor.

## Tecnologías usadas
- Python
- FastAPI
- dbm

## Ejecución del proyecto

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```
2. Ejecutar el servidor:
```bash
uvicorn main:app --reload
```
3. Abrir en el navegador:
```bash
http://127.0.0.1:8000/docs
```
## Endpoints
- POST /items/{key} Crear item
- GET /items/{key} Leer item
- PUT /items/{key} Actualizar item
- DELETE /items/{key} Eliminar item

## Descripción

Este proyecto implementa un CRUD usando una base de datos NoSQL de tipo clave-valor.
Se utilizó dbm para almacenar pares clave-valor y FastAPI para exponer los endpoints.
