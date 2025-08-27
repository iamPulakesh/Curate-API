from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.services import cache 

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

@router.get("/{user_id}", response_model=schemas.Recommendation)
def get_recommendations(user_id: int, db: Session = Depends(get_db)) -> dict:
    cache_key = f"recommendations:{user_id}"

    # Try cache
    cached_result = cache.get_cache(cache_key)
    if cached_result:
        return cached_result

    # Fetch user
    user = db.query(models.User).filter(models.User.id == user_id ).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not user.preferences:
        result = {"user_id": user_id, "user_name": user.name,"recommendations": []}
        return result

    # Normalize preferences
    user_genres = [g.strip().lower() for g in user.preferences.split(",") if g.strip()]

    # Fetch items
    items = db.query(models.Item).all()
    if not items:
        return {"user_id": user_id, "user_name": user.name,"recommendations": []}

    matched_items = []
    for item in items:
        if not item.genre:
            continue
        item_genres = [g.strip().lower() for g in item.genre.split(",") if g.strip()]
        if any(pref in item_genres for pref in user_genres):
            matched_items.append(item.title)

    result = {"user_id": user_id, "user_name": user.name,"preferences":user_genres,"recommendations": matched_items}

    # Save to cache
    cache.set_cache(cache_key, result, ttl=300)

    return result
