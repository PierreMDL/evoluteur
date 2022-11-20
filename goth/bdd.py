from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import GOTH, MotGOTH

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(GOTH)


def obtenir_mot(mot: MotGOTH) -> Mot:
    return base_obtenir_mot(mot=mot, langue=GOTH)


def obtenir_descendants(mot: MotGOTH) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=GOTH)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=GOTH)
