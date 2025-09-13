from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.api.controllers import materia as materia_controller
from app.schemas.materia import Materia, MateriaCreate

router = APIRouter(prefix="/materias", tags=["Materias"])


@router.get("/", response_model=List[Materia])
def get_materias(db: Session = Depends(get_db)):
    return materia_controller.get_materias(db)


@router.post("/", response_model=Materia)
def create_materia(materia: MateriaCreate, db: Session = Depends(get_db)):
    # podrías validar codigo único antes de crear si querés
    return materia_controller.create_materia(db, materia)


@router.get("/{materia_id}", response_model=Materia)
def get_materia(materia_id: int, db: Session = Depends(get_db)):
    found = materia_controller.get_materia_by_id(db, materia_id)
    if not found:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return found
