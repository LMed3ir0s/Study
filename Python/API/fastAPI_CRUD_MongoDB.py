import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient
from bson import ObjectId

cliente = MongoClient("mongodb://127.0.0.1:27017/")
db = cliente["db_APICRUD"]
colecao = db["usuarios"]

app = FastAPI()

def str_id(objeto):
    if isinstance(objeto, ObjectId): 
        return str(objeto)
    return objeto

class Usuario(BaseModel):
    id: str
    nome: str
    email: str
    senha: str

class Usuario_Resposta(BaseModel):
    id: str
    nome: str
    email: str

    class Config:
        from_attributes = True



@app.post("/criar_usuarios/", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    novo_usuario = usuario.dict()
    resultado = colecao.insert_one(novo_usuario)
    novo_usuario["id"] = str(resultado.inserted_id)
    return novo_usuario

# def criar_multiusuario(usuario: Usuario):


@app.get("/adm/usuarios", response_model=List[Usuario])
def get_adm():
    usuarios_cursor = colecao.find()
    usuarios = list(usuarios_cursor)
    if not usuarios:
         raise HTTPException(status_code=404, detail="Banco de Dados vázio.")
    return [
         
         Usuario(
              id=str(usuario["_id"]),
              nome=usuario["nome"],
              email=usuario["email"],
              senha=usuario["senha"]
         ) 

         for usuario in usuarios
    ]

@app.get("/buscar_usuario/{usuario_id}", response_model=Usuario_Resposta)
def get_usuario(usuario_id: str):
    usuario = colecao.find_one({"_id": ObjectId(usuario_id)})
    if usuario:
            return Usuario_Resposta(id=str_id(usuario["_id"]), nome=usuario["nome"], email=usuario["email"])
    raise HTTPException(status_code=404, detail="Usuario não encontrado.")

@app.put("/atualizar_usuario/{usuario_id}", response_model=Usuario)
def atualizar_usuario(usuario_id: str, atualizar_usuario: Usuario):
    usuario = colecao.find_one({"_id": ObjectId(usuario_id)})
    if usuario:
        colecao.update_one(
            {"_id": ObjectId(usuario_id)},
            {"$set": atualizar_usuario.dict()}
        )
        return atualizar_usuario
    raise HTTPException(status_code=404, detail="Usuario não encontrado.")

@app.delete("/deletar_usuario/{usuario_id}")
def deletar_usuario(usuario_id: str):
    resultado = colecao.delete_one({"_id": ObjectId(usuario_id)})
    if resultado.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Usuario não encontrado.")
    return {"Usuario deletado com sucesso!"}
    

if __name__ == "__main__":
    print("Iniciando o FastAPI...")
    uvicorn.run(app, port=8000)
