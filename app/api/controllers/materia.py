from sqlalchemy.orm import Session
from app.models.materia import Materia
from app.schemas.materia import MateriaCreate


def create_materia(db: Session, materia: MateriaCreate):
    db_materia = Materia(nombre=materia.nombre, codigo=materia.codigo, profesor=materia.profesor)
    db.add(db_materia)
    db.commit()
    db.refresh(db_materia)
    return db_materia


def get_materias(db: Session):
    return db.query(Materia).all()


def get_materia_by_id(db: Session, materia_id: int):
    return db.query(Materia).filter(Materia.id == materia_id).first()
