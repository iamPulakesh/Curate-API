from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models,schemas

router = APIRouter(prefix="/users", tags=["Users"])

# create user
@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name, preferences=user.preferences)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get all users
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
