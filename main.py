from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, crud, schemas
from database import SessionLocal, engine
from typing import List

# Criação do banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def obter_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"mensagem": "API para Gerenciamento de Projetos Sustentáveis"}

# --- Rotas para TipoFonte ---
@app.post("/tipos-fonte/", response_model=schemas.tipoFonte)
def criar_tipo_fonte(tipo_fonte: schemas.tipoFonteCriar, db: Session = Depends(obter_db)):
    return crud.criar_tipo_fonte(db, tipo_fonte)

@app.get("/tipos-fonte/", response_model=List[schemas.tipoFonte])
def listar_tipos_fontes(pular: int = 0, limite: int = 10, db: Session = Depends(obter_db)):
    return crud.listar_tipos_fontes(db, pular=pular, limite=limite)

@app.put("/tipos-fonte/{tipo_fonte_id}", response_model=schemas.tipoFonte)
def atualizar_tipo_fonte(tipo_fonte_id: int, tipo_fonte: schemas.tipoFonteAtualizar, db: Session = Depends(obter_db)):
    return crud.atualizar_tipo_fonte(db, tipo_fonte_id, tipo_fonte)

@app.delete("/tipos-fonte/{tipo_fonte_id}")
def deletar_tipo_fonte(tipo_fonte_id: int, db: Session = Depends(obter_db)):
    return crud.deletar_tipo_fonte(db, tipo_fonte_id)

# --- Rotas para Regioes Sustentáveis ---
@app.post("/regioes-sustentaveis/", response_model=schemas.regioesSustentaveis)
def criar_regiao_sustentavel(regiao: schemas.regioesSustentaveisCriar, db: Session = Depends(obter_db)):
    return crud.criar_regiao_sustentavel(db, regiao)

@app.get("/regioes-sustentaveis/", response_model=List[schemas.regioesSustentaveis])
def listar_regioes_sustentaveis(pular: int = 0, limite: int = 10, db: Session = Depends(obter_db)):
    return crud.listar_regioes_sustentaveis(db, pular=pular, limite=limite)

@app.put("/regioes-sustentaveis/{regiao_id}", response_model=schemas.regioesSustentaveis)
def atualizar_regiao_sustentavel(regiao_id: int, regiao: schemas.regioesSustentaveisAtualizar, db: Session = Depends(obter_db)):
    return crud.atualizar_regiao_sustentavel(db, regiao_id, regiao)

@app.delete("/regioes-sustentaveis/{regiao_id}")
def deletar_regiao_sustentavel(regiao_id: int, db: Session = Depends(obter_db)):
    return crud.deletar_regiao_sustentavel(db, regiao_id)

# --- Rotas para Projetos Sustentáveis ---
@app.post("/projetos-sustentaveis/", response_model=schemas.projetosSustentaveis)
def criar_projeto_sustentavel(projeto: schemas.projetosSustentaveisCriar, db: Session = Depends(obter_db)):
    return crud.criar_projeto_sustentavel(db, projeto)

@app.get("/projetos-sustentaveis/", response_model=List[schemas.projetosSustentaveis])
def listar_projetos_sustentaveis(pular: int = 0, limite: int = 10, db: Session = Depends(obter_db)):
    return crud.listar_projetos_sustentaveis(db, pular=pular, limite=limite)

@app.put("/projetos-sustentaveis/{projeto_id}", response_model=schemas.projetosSustentaveis)
def atualizar_projeto_sustentavel(projeto_id: int, projeto: schemas.projetosSustentaveisAtualizar, db: Session = Depends(obter_db)):
    return crud.atualizar_projeto_sustentavel(db, projeto_id, projeto)

@app.delete("/projetos-sustentaveis/{projeto_id}")
def deletar_projeto_sustentavel(projeto_id: int, db: Session = Depends(obter_db)):
    return crud.deletar_projeto_sustentavel(db, projeto_id)

# --- Rotas para Emissões de Carbono ---
@app.post("/emissoes-carbono/", response_model=schemas.emissoesCarbono)
def criar_emissao_carbono(emissao: schemas.emissoesCarbonoCriar, db: Session = Depends(obter_db)):
    return crud.criar_emissao_carbono(db, emissao)

@app.get("/emissoes-carbono/", response_model=List[schemas.emissoesCarbono])
def listar_emissoes_carbono(pular: int = 0, limite: int = 10, db: Session = Depends(obter_db)):
    return crud.listar_emissoes_carbono(db, pular=pular, limite=limite)

@app.put("/emissoes-carbono/{emissao_id}", response_model=schemas.emissoesCarbono)
def atualizar_emissao_carbono(emissao_id: int, emissao: schemas.emissoesCarbonoAtualizar, db: Session = Depends(obter_db)):
    return crud.atualizar_emissao_carbono(db, emissao_id, emissao)

@app.delete("/emissoes-carbono/{emissao_id}")
def deletar_emissao_carbono(emissao_id: int, db: Session = Depends(obter_db)):
    return crud.deletar_emissao_carbono(db, emissao_id)
