from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/items", tags=["Items"])

#post items
@router.post("/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, owner_id: int, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item, owner_id=owner_id)

#get items
@router.get("/", response_model=list[schemas.ItemResponse])
def list_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

#get items by genre
@router.get("/genre={genre}", response_model=list[schemas.ItemResponse])
def list_items_by_genre(genre: str, db: Session = Depends(get_db)):
    return crud.get_items_by_genre(db, genre)
