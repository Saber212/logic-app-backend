from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    name : str
    company : str
    email : str
    username : str
    timestamp : datetime

class UserOut(BaseModel):
    id: int
    name: str
    company : str
    email: str
    username : str
    timestamp: datetime

    class Config:
        orm_mode = True
        
class UserResponse(UserCreate):
    id: int
    timestamp: datetime
    class Config:
        model_config = True