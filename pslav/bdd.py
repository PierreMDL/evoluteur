from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import PSLAV, MotPSLAV

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(PSLAV)


def obtenir_mot(mot: MotPSLAV) -> Mot:
    return base_obtenir_mot(mot=mot, langue=PSLAV)


def obtenir_descendants(mot: MotPSLAV) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=PSLAV)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=PSLAV)
