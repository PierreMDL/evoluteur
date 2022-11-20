from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import PITAL, MotPITAL

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(PITAL)


def obtenir_mot(mot: MotPITAL) -> Mot:
    return base_obtenir_mot(mot=mot, langue=PITAL)


def obtenir_descendants(mot: MotPITAL) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=PITAL)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=PITAL)
