from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import SAN, MotSAN

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(SAN)


def obtenir_mot(mot: MotSAN) -> Mot:
    return base_obtenir_mot(mot=mot, langue=SAN)


def obtenir_descendants(mot: MotSAN) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=SAN)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=SAN)
