from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, crud, schemas
from database import SessionLocal, engine
from typing import List

# Criação das tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def obter_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota raiz
@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo ao sistema de gerenciamento de tabelas de energia"}
