from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import models, schemas


# Função genérica para validar existência
def validar_existencia(db: Session, model, model_id: int, nome_modelo: str):
    db_objeto = db.query(model).filter(model.id == model_id).first()
    if not db_objeto:
        raise HTTPException(status_code=404, detail=f"{nome_modelo} com ID {model_id} não encontrado.")
    return db_objeto


# CRUD para TipoFonte
def criar_tipo_fonte(db: Session, tipo_fonte: schemas.tipoFonteCriar):
    db_tipo_fonte = models.TipoFonte(**tipo_fonte.dict())
    try:
        db.add(db_tipo_fonte)
        db.commit()
        db.refresh(db_tipo_fonte)
        return db_tipo_fonte
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="TipoFonte já cadastrada.")


def listar_tipos_fontes(db: Session, pular: int = 0, limite: int = 10):
    return db.query(models.TipoFonte).offset(pular).limit(limite).all()


def atualizar_tipo_fonte(db: Session, tipo_fonte_id: int, tipo_fonte: schemas.tipoFonteAtualizar):
    db_tipo_fonte = validar_existencia(db, models.TipoFonte, tipo_fonte_id, "TipoFonte")
    for chave, valor in tipo_fonte.dict(exclude_unset=True).items():
        setattr(db_tipo_fonte, chave, valor)
    db.commit()
    db.refresh(db_tipo_fonte)
    return db_tipo_fonte


def deletar_tipo_fonte(db: Session, tipo_fonte_id: int):
    db_tipo_fonte = validar_existencia(db, models.TipoFonte, tipo_fonte_id, "TipoFonte")
    db.delete(db_tipo_fonte)
    db.commit()
    return {"mensagem": "TipoFonte deletada com sucesso."}


# CRUD para RegiaoSustentavel
def criar_regiao_sustentavel(db: Session, regiao: schemas.regioesSustentaveisCriar):
    db_regiao = models.RegiaoSustentavel(**regiao.dict())
    try:
        db.add(db_regiao)
        db.commit()
        db.refresh(db_regiao)
        return db_regiao
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Região Sustentável já cadastrada.")


def listar_regioes_sustentaveis(db: Session, pular: int = 0, limite: int = 10):
    return db.query(models.RegiaoSustentavel).offset(pular).limit(limite).all()


def atualizar_regiao_sustentavel(db: Session, regiao_id: int, regiao: schemas.regioesSustentaveisAtualizar):
    db_regiao = validar_existencia(db, models.RegiaoSustentavel, regiao_id, "Região Sustentável")
    for chave, valor in regiao.dict(exclude_unset=True).items():
        setattr(db_regiao, chave, valor)
    db.commit()
    db.refresh(db_regiao)
    return db_regiao


def deletar_regiao_sustentavel(db: Session, regiao_id: int):
    db_regiao = validar_existencia(db, models.RegiaoSustentavel, regiao_id, "Região Sustentável")
    db.delete(db_regiao)
    db.commit()
    return {"mensagem": "Região Sustentável deletada com sucesso."}


# CRUD para ProjetoSustentavel
def criar_projeto_sustentavel(db: Session, projeto: schemas.projetosSustentaveisCriar):
    db_projeto = models.ProjetoSustentavel(**projeto.dict())
    try:
        db.add(db_projeto)
        db.commit()
        db.refresh(db_projeto)
        return db_projeto
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Projeto Sustentável já cadastrado.")


def listar_projetos_sustentaveis(db: Session, pular: int = 0, limite: int = 10):
    return db.query(models.ProjetoSustentavel).offset(pular).limit(limite).all()


def atualizar_projeto_sustentavel(db: Session, projeto_id: int, projeto: schemas.projetosSustentaveisAtualizar):
    db_projeto = validar_existencia(db, models.ProjetoSustentavel, projeto_id, "Projeto Sustentável")
    for chave, valor in projeto.dict(exclude_unset=True).items():
        setattr(db_projeto, chave, valor)
    db.commit()
    db.refresh(db_projeto)
    return db_projeto


def deletar_projeto_sustentavel(db: Session, projeto_id: int):
    db_projeto = validar_existencia(db, models.ProjetoSustentavel, projeto_id, "Projeto Sustentável")
    db.delete(db_projeto)
    db.commit()
    return {"mensagem": "Projeto Sustentável deletado com sucesso."}


# CRUD para EmissaoCarbono
def criar_emissao_carbono(db: Session, emissao: schemas.emissoesCarbonoCriar):
    db_emissao = models.EmissaoCarbono(**emissao.dict())
    try:
        db.add(db_emissao)
        db.commit()
        db.refresh(db_emissao)
        return db_emissao
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Emissão de Carbono já cadastrada.")


def listar_emissoes_carbono(db: Session, pular: int = 0, limite: int = 10):
    return db.query(models.EmissaoCarbono).offset(pular).limit(limite).all()


def atualizar_emissao_carbono(db: Session, emissao_id: int, emissao: schemas.emissoesCarbonoAtualizar):
    db_emissao = validar_existencia(db, models.EmissaoCarbono, emissao_id, "Emissão de Carbono")
    for chave, valor in emissao.dict(exclude_unset=True).items():
        setattr(db_emissao, chave, valor)
    db.commit()
    db.refresh(db_emissao)
    return db_emissao


def deletar_emissao_carbono(db: Session, emissao_id: int):
    db_emissao = validar_existencia(db, models.EmissaoCarbono, emissao_id, "Emissão de Carbono")
    db.delete(db_emissao)
    db.commit()
    return {"mensagem": "Emissão de Carbono deletada com sucesso."}
