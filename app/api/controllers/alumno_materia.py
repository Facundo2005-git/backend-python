from sqlalchemy.orm import Session
from app.models.alumno_materia import AlumnoMateria
from app.schemas.alumno_materia import AlumnoMateriaCreate


def enroll_student(db: Session, enroll: AlumnoMateriaCreate):
    # evitar duplicados
    existing = db.query(AlumnoMateria).filter(
        AlumnoMateria.user_id == enroll.user_id,
        AlumnoMateria.materia_id == enroll.materia_id,
    ).first()
    if existing:
        return existing

    record = AlumnoMateria(user_id=enroll.user_id, materia_id=enroll.materia_id)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def unenroll_student(db: Session, user_id: int, materia_id: int):
    rec = db.query(AlumnoMateria).filter(
        AlumnoMateria.user_id == user_id,
        AlumnoMateria.materia_id == materia_id,
    ).first()
    if rec:
        db.delete(rec)
        db.commit()
        return True
    return False


def get_materias_by_user(db: Session, user_id: int):
    return db.query(AlumnoMateria).filter(AlumnoMateria.user_id == user_id).all()


def get_alumnos_by_materia(db: Session, materia_id: int):
    return db.query(AlumnoMateria).filter(AlumnoMateria.materia_id == materia_id).all()
