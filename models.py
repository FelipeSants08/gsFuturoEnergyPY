from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  


class TipoFonte(Base):
    __tablename__ = "TIPO_FONTES"
    __table_args__ = {'schema': 'PF0645'}  # Define o esquema

    id = Column('ID_TIPO_FONTE', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(50), nullable=False)

    emissoes = relationship("EmissaoCarbono", back_populates="tipo_fonte")
    projetos = relationship("ProjetoSustentavel", back_populates="tipo_fonte")


class RegiaoSustentavel(Base):
    __tablename__ = "REGIOES_SUSTENTAVEIS"
    __table_args__ = {'schema': 'PF0645'}

    id = Column('ID_REGIAO', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(50), nullable=False)

    projetos = relationship("ProjetoSustentavel", back_populates="regiao")


class ProjetoSustentavel(Base):
    __tablename__ = "PROJETOS_SUSTENTAVEIS"
    __table_args__ = {'schema': 'PF0645'}

    id = Column('ID_PROJETO', Integer, primary_key=True, autoincrement=True)
    descricao = Column('DESCRICAO', String(255), nullable=False)
    custo = Column('CUSTO', Float, nullable=False)
    status = Column('STATUS', String(50), nullable=False)
    tipo_fonte_id = Column('ID_TIPO_FONTE', Integer, ForeignKey('PF0645.TIPO_FONTES.ID_TIPO_FONTE'))
    regiao_id = Column('ID_REGIAO', Integer, ForeignKey('PF0645.REGIOES_SUSTENTAVEIS.ID_REGIAO'))

    tipo_fonte = relationship("TipoFonte", back_populates="projetos")
    regiao = relationship("RegiaoSustentavel", back_populates="projetos")


class EmissaoCarbono(Base):
    __tablename__ = "EMISSOES_CARBONO"
    __table_args__ = {'schema': 'PF0645'}

    id = Column('ID_EMISSAO', Integer, primary_key=True, autoincrement=True)
    tipo_fonte_id = Column('ID_TIPO_FONTE', Integer, ForeignKey('PF0645.TIPO_FONTES.ID_TIPO_FONTE'))
    emissao = Column('EMISSAO', Float, nullable=False)

    tipo_fonte = relationship("TipoFonte", back_populates="emissoes")
