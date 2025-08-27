from sqlalchemy.orm import Session
from app import models, schemas

# user CRUD
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, preferences=user.preferences)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# item CRUD
def create_item(db: Session, item: schemas.ItemCreate, owner_id: int = None):
    db_item = models.Item(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session):
    return db.query(models.Item).all()

def get_items_by_genre(db: Session, genre: str):
    return db.query(models.Item).filter(models.Item.genre.ilike(f"%{genre}%")).all()

def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
