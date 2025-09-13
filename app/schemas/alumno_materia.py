from pydantic import BaseModel
from datetime import datetime


class AlumnoMateriaBase(BaseModel):
    user_id: int
    materia_id: int


class AlumnoMateriaCreate(AlumnoMateriaBase):
    pass


class AlumnoMateriaResponse(AlumnoMateriaBase):
    id: int
    fecha_inscripcion: datetime

    class Config:
        orm_mode = True
