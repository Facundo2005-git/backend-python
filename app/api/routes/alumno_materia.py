from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.api.controllers import alumno_materia as am_controller
from app.schemas.alumno_materia import AlumnoMateriaCreate, AlumnoMateriaResponse

router = APIRouter(prefix="/inscripciones", tags=["Inscripciones"])


@router.post("/", response_model=AlumnoMateriaResponse)
def enroll(enroll: AlumnoMateriaCreate, db: Session = Depends(get_db)):
    return am_controller.enroll_student(db, enroll)


@router.delete("/", response_model=dict)
def unenroll(user_id: int = Query(...), materia_id: int = Query(...), db: Session = Depends(get_db)):
    ok = am_controller.unenroll_student(db, user_id, materia_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Inscripción no encontrada")
    return {"detail": "Desinscripción exitosa"}


@router.get("/materias/{user_id}", response_model=List[AlumnoMateriaResponse])
def materias_by_user(user_id: int, db: Session = Depends(get_db)):
    return am_controller.get_materias_by_user(db, user_id)


@router.get("/alumnos/{materia_id}", response_model=List[AlumnoMateriaResponse])
def alumnos_by_materia(materia_id: int, db: Session = Depends(get_db)):
    return am_controller.get_alumnos_by_materia(db, materia_id)
