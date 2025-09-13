from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base


class Materia(Base):
    __tablename__ = "materias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, index=True)
    codigo = Column(String(50), unique=True, nullable=False, index=True)
    profesor = Column(String(100), nullable=True)

    # Relación con la tabla intermedia AlumnoMateria
    alumnos = relationship("AlumnoMateria", back_populates="materia", cascade="all, delete-orphan")
