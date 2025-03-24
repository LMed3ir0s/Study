import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

class Usuario_Resposta(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True

banco_dados: List[Usuario] = []

@app.post("/usuarios/", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    banco_dados.append(usuario)
    return usuario

@app.get("/usuarios/adm", response_model=List[Usuario])
def get_adm():
    if not banco_dados:
         raise HTTPException(status_code=404, detail="Usuario não encontrado.")
    return banco_dados

@app.get("/usuarios/{usuario_id}", response_model=Usuario_Resposta)
def get_usuario(usuario_id: int):
    for usuario in banco_dados:
        if usuario.id == usuario_id:
            return Usuario_Resposta(id=usuario.id, nome=usuario.nome, email=usuario.email)
    raise HTTPException(status_code=404, detail="Usuario não encontrado.")

@app.put("/usuarios/{usuario_id}", response_model=Usuario)
def atualizar_usuario(usuario_id: int, atualizar_usuario: Usuario):
    for i, usuario in enumerate(banco_dados):
        if usuario.id == usuario_id:
            banco_dados[i] = Usuario(
                id=usuario.id,
                nome=atualizar_usuario.nome,
                email=atualizar_usuario.email,
                senha=atualizar_usuario.senha
                )
            print(f"Senha atualizada: {banco_dados[i].senha}")
            return banco_dados[i]
    raise HTTPException(status_code=404, detail="Usuario não encontrado.")

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    for i, usuario in enumerate(banco_dados):
        if usuario.id == usuario_id:
            banco_dados.pop(i)
            return {"Usuario deletado com sucesso!"}
    raise HTTPException(status_code=404, detail="Usuario não encontrado.")

if __name__ == "__main__":
    print("Iniciando o FastAPI...")
    uvicorn.run(app, port=8000)