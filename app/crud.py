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
