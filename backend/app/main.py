# backend/app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db, init_db

# Initialiser la BDD au démarrage
init_db()

app = FastAPI(title="Adventure Planner")

@app.get("/adventures/", response_model=List[schemas.Adventure])
def read_adventures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    adventures = db.query(models.Adventure).offset(skip).limit(limit).all()
    return adventures

@app.get("/adventures/{slug}", response_model=schemas.Adventure)
def read_adventure(slug: str, db: Session = Depends(get_db)):
    adventure = db.query(models.Adventure).filter(models.Adventure.slug == slug).first()
    if adventure is None:
        raise HTTPException(status_code=404, detail="Aventure non trouvée")
    return adventure
