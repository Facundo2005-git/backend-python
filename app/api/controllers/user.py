# pyton puro
from sqlalchemy.orm import Session
from app.utils.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate
from datetime import timedelta
from sqlalchemy.orm import Session
from app.utils.security import verify_password, create_access_token
from app.models.user import User

def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name, email=user.email, password=hash_password(user.password), role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        return None

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email, "role": user.role},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}