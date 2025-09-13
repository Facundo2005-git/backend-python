from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint, func
from sqlalchemy.orm import relationship
from app.database.database import Base


class AlumnoMateria(Base):
    __tablename__ = "alumno_materia"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    materia_id = Column(Integer, ForeignKey("materias.id"), nullable=False, index=True)
    fecha_inscripcion = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (UniqueConstraint('user_id', 'materia_id', name='uix_user_materia'),)

    # Relaciones
    alumno = relationship("User", back_populates="materias")
    materia = relationship("Materia", back_populates="alumnos")
