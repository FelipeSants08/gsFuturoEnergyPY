from pydantic import BaseModel
from typing import Optional

class tipoFonteBase(BaseModel):
    nome: str

class tipoFonte(tipoFonteBase):
    id: int
    
    class Config:
        orm_mode = True

class tipoFonteCriar(tipoFonteBase):
    pass

class tipoFonteAtualizar(BaseModel):
    nome: Optional[str] = None
    
    

class regioesSustentaveisBase(BaseModel):
    nome: str

class regioesSustentaveis(regioesSustentaveisBase):
    id: int
    
    class Config:
        orm_mode = True

class regioesSustentaveisCriar(regioesSustentaveisBase):
    pass
       
class regioesSustentaveisAtualizar(BaseModel):
    nome: Optional[str] = None



class projetosSustentaveisBase(BaseModel):
    descricao: str
    custo: float
    status: str
    tipo_fonte_id: int
    regioes_sustentaveis_id: int
 
class projetosSustentaveis(projetosSustentaveisBase):
    id: int 
    class Config:
        orm_mode = True

class projetosSustentaveisCriar(projetosSustentaveisBase):
    pass
   
class projetosSustentaveisAtualizar(BaseModel):
    descricao: Optional[str] = None
    custo: Optional[float] = None
    status: Optional[str] = None
    tipo_fonte_id: Optional[int] = None
    regioes_sustentaveis_id: Optional[int] = None
    
class emissoesCarbonoBase(BaseModel):
    tipo_fonte_id: int
    emissao: str

class emissoesCarbono(emissoesCarbonoBase):
    id: int
    class Config:
        orm_mode = True

class emissoesCarbonoCriar(emissoesCarbono):
    pass

class emissoesCarbonoAtualizar(BaseModel):
    tipo_fonte_id: Optional[int] = None
    emissao: Optional[str] = None
