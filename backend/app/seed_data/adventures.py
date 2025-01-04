# backend/app/seed_data/adventures.py
from typing import List
from ..schemas import AdventureCreate

seed_adventures: List[AdventureCreate] = [
    AdventureCreate(
        slug="traversee-baie-mont-saint-michel",
        title="Randonnée Mont Saint-Michel",
        location="Normandie",
        description="Traversée de la baie à marée basse, pêche à pied, visite de l'abbaye",
        nearest_station="Pontorson",
        station_access_info="Navette régulière entre la gare et le Mont (45min)",
        duration=1.0,
        difficulty=2,
        suitable_months=[5, 6, 7, 8, 9],  # Mai à Septembre
        budget_level=2,
        indicative_price=30,
        budget_notes="Prévoir 17€ pour l'entrée de l'abbaye. Guide obligatoire pour la traversée (~15€)",
        guide_required=True,
        website="https://www.ot-montsaintmichel.com/"
    ),
    AdventureCreate(
        slug="bivouac-calanques",
        title="Bivouac dans les Calanques",
        location="Marseille",
        description="Weekend de randonnée et camping dans les calanques",
        nearest_station="Marseille Saint-Charles",
        station_access_info="Puis bus RTM ligne 21 jusqu'à Luminy",
        duration=2.0,
        difficulty=3,
        suitable_months=[4, 5, 6, 9, 10],  # Avril-Juin, Septembre-Octobre (éviter l'été)
        season_notes="Eviter l'été, chaleur et risque d'incendie",
        budget_level=1,
        indicative_price=10,
        budget_notes="Gratuit, prévoir uniquement le transport et la nourriture",
        guide_required=False,
        website="https://www.calanques-parcnational.fr/"
    ),
    AdventureCreate(
        slug="gr20-premiere-etape",
        title="GR20 : Première étape",
        location="Corse",
        description="Découverte de la première étape du mythique GR20, de Calenzana à Ortu di u Piobbu",
        nearest_station="Calvi",
        station_access_info="Navette ou taxi de Calvi à Calenzana (12km)",
        duration=1.0,
        difficulty=5,
        suitable_months=[6, 7, 8, 9],  # Juin à Septembre
        budget_level=2,
        indicative_price=50,
        budget_notes="Nuit en refuge ~16€, repas ~20€, transport ~15€",
        guide_required=False,
        website="https://www.gr20.fr/"
    ),
]
