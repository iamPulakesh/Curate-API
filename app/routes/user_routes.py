from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models,schemas,crud

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

# delete user
@router.delete("/delete={user_id}", response_model=schemas.UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# get users by name
@router.get("/name={name}", response_model=list[schemas.UserResponse])
def get_users_by_name(name: str, db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.name.ilike(f"%{name}%")).all()
    return users

# update user
@router.put("/update={user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
