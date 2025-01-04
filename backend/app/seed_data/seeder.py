from sqlalchemy.orm import Session
from .. import models
from .adventures import seed_adventures

def seed_database(db: Session) -> None:
    """Remplit la base de données avec les données initiales."""
    
    # Supprime toutes les aventures existantes
    db.query(models.Adventure).delete()
    
    # Ajoute les nouvelles aventures
    for adventure_data in seed_adventures:
        db_adventure = models.Adventure(**adventure_data.model_dump())
        db.add(db_adventure)
    
    try:
        db.commit()
        print("✅ Base de données mise à jour avec succès!")
    except Exception as e:
        print(f"❌ Erreur lors de la mise à jour de la base de données: {e}")
        db.rollback()
