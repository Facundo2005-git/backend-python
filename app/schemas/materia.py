from pydantic import BaseModel
from typing import Optional


class MateriaBase(BaseModel):
    nombre: str
    codigo: str
    profesor: Optional[str] = None


class MateriaCreate(MateriaBase):
    pass


class Materia(MateriaBase):
    id: int

    class Config:
        orm_mode = True
