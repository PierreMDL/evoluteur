from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import PHELL, MotPHELL

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(PHELL)


def obtenir_mot(mot: MotPHELL) -> Mot:
    return base_obtenir_mot(mot=mot, langue=PHELL)


def obtenir_descendants(mot: MotPHELL) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=PHELL)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=PHELL)