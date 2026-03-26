from fastapi import FastAPI, HTTPException
import dbm
import json

app = FastAPI(title="Taller BD NoSQL - ClaveValor", description="CRUD usando la BD DBM (Key-Value)")

# DBM creará automáticamente un archivo local para guardar los datos persistentes
DB_NAME = "mi_base_clave_valor"

# CREATE
@app.post("/items/{key}")
def crear_item(key: str, data: dict):
    with dbm.open(DB_NAME, 'c') as db:
        if key.encode('utf-8') in db:
            raise HTTPException(status_code=400, detail="La clave ya existe")
            
        db[key] = json.dumps(data)
    return {"mensaje": "Creado exitosamente", "clave": key, "valor": data}

# READ
@app.get("/items/{key}")
def leer_item(key: str):
    with dbm.open(DB_NAME, 'c') as db:
        resultado = db.get(key.encode('utf-8'))
        if not resultado:
            raise HTTPException(status_code=404, detail="Clave no encontrada")
        
        return {"clave": key, "valor": json.loads(resultado.decode('utf-8'))}

# UPDATE
@app.put("/items/{key}")
def actualizar_item(key: str, data: dict):
    with dbm.open(DB_NAME, 'c') as db:
        if key.encode('utf-8') not in db:
            raise HTTPException(status_code=404, detail="Clave no encontrada para actualizar")
        
        db[key] = json.dumps(data)
    return {"mensaje": "Actualizado exitosamente", "clave": key, "valor": data}

# DELETE
@app.delete("/items/{key}")
def eliminar_item(key: str):
    with dbm.open(DB_NAME, 'c') as db:
        if key.encode('utf-8') not in db:
            raise HTTPException(status_code=404, detail="Clave no encontrada")
        
        del db[key]
    return {"mensaje": "Eliminado correctamente", "clave": key}
