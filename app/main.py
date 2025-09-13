from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database.database import get_db, engine, Base
from app.api.routes import user as user_routes, materia, alumno_materia

# Crear la aplicación FastAPI
app = FastAPI(
    title="Sistema Educativo API",
    description="API para gestionar profesores, alumnos y materias",
    version="1.0.0",
)

# Crear las tablas en la BD si no existen
Base.metadata.create_all(bind=engine)

@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}

# Montar routers
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(materia.router, prefix="/materias", tags=["Materias"])
app.include_router(alumno_materia.router, prefix="/alumno_materia", tags=["AlumnoMateria"])
