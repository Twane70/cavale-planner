# schemas.py
from typing import List, Optional
from typing_extensions import Annotated
from pydantic import BaseModel, Field, HttpUrl

class AdventureBase(BaseModel):
    title: str
    description: str
    location: str
    nearest_station: Optional[str] = None
    station_access_info: Optional[str] = None
    duration: float
    difficulty: Annotated[int, Field(ge=1, le=5)]
    suitable_months: List[Annotated[int, Field(ge=1, le=12)]]
    season_notes: Optional[str] = None
    budget_level: Annotated[int, Field(ge=1, le=5)]
    indicative_price: Optional[int] = None
    budget_notes: Optional[str] = None
    guide_required: bool = False
    website: Optional[str] = None

class AdventureCreate(AdventureBase):
    slug: str

class Adventure(AdventureBase):
    slug: str

    class Config:
        from_attributes = True

