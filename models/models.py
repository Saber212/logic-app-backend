from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=True)
    company = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    username = Column(String(100), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
