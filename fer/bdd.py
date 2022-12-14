from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import FER, MotFER

# Chaque fois que le module est initialis√©, garantir que la langue est √† jour
garantir(FER)


def obtenir_mot(mot: MotFER) -> Mot:
    return base_obtenir_mot(mot=mot, langue=FER)


def obtenir_descendants(mot: MotFER) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=FER)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=FER)
