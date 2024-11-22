from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  


class TipoFonte(Base):
    __tablename__ = "TIPO_FONTES"

    id = Column('ID_TIPO_FONTE', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(50), nullable=False)

    emissoes = relationship("EmissaoCarbono", back_populates="tipo_fonte")
    projetos = relationship("ProjetoSustentavel", back_populates="tipo_fonte")


class RegiaoSustentavel(Base):
    __tablename__ = "REGIOES_SUSTENTAVEIS"
   

    id = Column('ID_REGIAO', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(50), nullable=False)

    projetos = relationship("ProjetoSustentavel", back_populates="regiao")


class ProjetoSustentavel(Base):
    __tablename__ = "PROJETOS_SUSTENTAVEIS"
    

    id = Column('ID_PROJETO', Integer, primary_key=True, autoincrement=True)
    descricao = Column('DESCRICAO', String(255), nullable=False)
    custo = Column('CUSTO', Float, nullable=False)
    status = Column('STATUS', String(50), nullable=False)
    tipo_fonte_id = Column('ID_TIPO_FONTE', Integer, ForeignKey('TIPO_FONTES.ID_TIPO_FONTE'), nullable=False)
    regioes_sustentaveis_id = Column('ID_REGIAO', Integer, ForeignKey('REGIOES_SUSTENTAVEIS.ID_REGIAO'), nullable=False)

    tipo_fonte = relationship("TipoFonte", back_populates="projetos")
    regiao = relationship("RegiaoSustentavel", back_populates="projetos")


class EmissaoCarbono(Base):
    __tablename__ = "EMISSOES_CARBONO"

    id = Column('ID_EMISSAO', Integer, primary_key=True, autoincrement=True)
    tipo_fonte_id = Column('ID_TIPO_FONTE', Integer, ForeignKey('TIPO_FONTES.ID_TIPO_FONTE'))
    emissao = Column('EMISSAO', Float, nullable=False)

    tipo_fonte = relationship("TipoFonte", back_populates="emissoes")
