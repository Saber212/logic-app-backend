from sqlalchemy import create_engine, event, text
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.exc import SQLAlchemyError
import os
import logging
from typing import Generator
from models.models import Base, User
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

try:
    engine = create_engine(
        DATABASE_URL,
        echo=True,  # Log all SQL statements
        pool_pre_ping=True,  # Enable connection health checks
        pool_recycle=3600,  # Recycle connections after 1 hour
    )
    
    # Test the connection
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
except SQLAlchemyError as e:
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        raise
    finally:
        db.close()

# Create all tables
def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except SQLAlchemyError as e:
        raise

# Initialize tables when this module is imported
init_db()
