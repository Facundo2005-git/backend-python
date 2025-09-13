from pydantic import BaseModel


class User(BaseModel):
    name: str
    id: int
    # atributos


class LoginSchema(BaseModel):
    email: str
    password: str


class UserUpdate(User):
    password: str


class UserCreate(BaseModel):
    email: str
    password: str
    name: str
    role: str = "alumno"
