# backend/app/seed_data/adventures.py
from typing import List
from ..schemas import AdventureCreate

seed_adventures: List[AdventureCreate] = [
    AdventureCreate(
        slug="bivouac-calanques",
        title="Bivouac dans les Calanques",
        location="Marseille",
        description="Weekend de randonnée et camping dans les calanques",
        nearest_station="Marseille Saint-Charles",
        station_access_info="Puis bus RTM ligne 21 jusqu'à Luminy",
        country="France",
        zip_code="13000",
        duration=2.0,
        distance=20.0,
        difficulty=3,
        suitable_months=[4, 5, 6, 9, 10],  # Avril-Juin, Septembre-Octobre (éviter l'été)
        season_notes="Eviter l'été, chaleur et risque d'incendie",
        budget_level=1,
        indicative_price=10,
        budget_notes="Gratuit, prévoir uniquement le transport et la nourriture",
        guide_required=False,
        website="https://www.calanques-parcnational.fr/"
    ),
]


"""
manger un munster à Munster
boire du cognac à Cognac
manger un burger à Hamburg
nager à Nages
danser à Danse
du jambon à Parme
du roquefort à Roquefort
du champagne en Champagne
des pruneaux à Agen
du camembert à Camembert
des calissons à Aix
de la moutarde à Dijon
une tropézienne à St Tropez
de la fourme à Ambert
du beaufort à Beaufort
du reblochon à Reblochon
du saint-nectaire à Saint-Nectaire
du maroilles à Maroilles
se balader à Balade
du comté en franche-comté
du bleu à Gex
du brie à Brie
du cantal dans le Cantal
de la tomme à Tomme
du mont d'or au mont d'or
du cheddar à Cheddar
boire un verre à Verre

"""