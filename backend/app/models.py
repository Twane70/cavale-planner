# models.py
from sqlalchemy import Column, Integer, String, Float, Text, ARRAY, Boolean
from .database import Base

class Adventure(Base):
    __tablename__ = "adventures"

    slug = Column(String, primary_key=True, index=True)  # ex: "gr20-corse"
    title = Column(String, index=True)
    description = Column(Text)
    
    # Localisation
    location = Column(String)
    nearest_station = Column(String, nullable=True)
    station_access_info = Column(Text, nullable=True)
    
    # Caractéristiques
    duration = Column(Float)  # en jours
    difficulty = Column(Integer)  # 1-5
    suitable_months = Column(ARRAY(Integer))  # [1,2,3,4] pour Jan-Avril
    season_notes = Column(Text, nullable=True)
    
    # Budget
    budget_level = Column(Integer)  # 1-5
    indicative_price = Column(Integer, nullable=True)  # en euros
    budget_notes = Column(Text, nullable=True)
    
    # Informations pratiques
    guide_required = Column(Boolean, default=False)
    website = Column(String, nullable=True)

