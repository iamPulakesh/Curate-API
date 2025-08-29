from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/items", tags=["Items"])

# create items
@router.post("/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, owner_id: int, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item, owner_id=owner_id)

# get items
@router.get("/", response_model=list[schemas.ItemResponse])
def list_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

# get items by genre
@router.get("/genre={genre}", response_model=list[schemas.ItemResponse])
def list_items_by_genre(genre: str, db: Session = Depends(get_db)):
    return crud.get_items_by_genre(db, genre)

# delete item
@router.delete("/delete={item_id}", response_model=schemas.ItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# update items
@router.put("/update={item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db, item_id, item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item