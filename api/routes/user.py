from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from db.db import get_db
from models.models import User
from datetime import datetime
from schemas.user import UserCreate, UserOut

router = APIRouter(prefix="/user")

@router.post("/user")

def postuser(user_data: UserCreate, db : Session = Depends(get_db)):

    try:
        user = User(
            name=user_data.name,
            company=user_data.company,
            email=user_data.email,
            username=user_data.username,
            timestamp=datetime.utcnow()
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/user", response_model=list[UserOut])
def getuser(db : Session = Depends(get_db)): 
    
    users = db.query(User).all()
    return users

