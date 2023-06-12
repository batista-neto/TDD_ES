from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):
    id: Optional[int]
    nome: Optional[str] 
    valor: Optional[float]