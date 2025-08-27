from pydantic import BaseModel
from typing import Optional

# user Schemas
class UserBase(BaseModel):
    name: str
    preferences: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True

class UserUpdate(UserBase):
    name: Optional[str]=None
    preferences: Optional[str]=None

# item Schemas
class ItemBase(BaseModel):
    title: str
    genre: str
    type: str

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    owner_id: int | None = None
    class Config:
        from_attributes = True

# recommendation Schemas
class Recommendation(BaseModel):
    user_id: int
    user_name: str
    preferences: list[str]
    recommendations: list[str] 
