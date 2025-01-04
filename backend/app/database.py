# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:postgres@localhost:5432/adventures"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    from . import models  # Import ici pour éviter les imports circulaires
    
    # Drop toutes les tables existantes
    Base.metadata.drop_all(bind=engine)
    # Recréer toutes les tables
    Base.metadata.create_all(bind=engine)
    
    # Seeding
    from .seed_data.seeder import seed_database
    db = SessionLocal()
    try:
        seed_database(db)
    finally:
        db.close()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
