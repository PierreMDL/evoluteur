from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import PBRIT, MotPBRIT

# Chaque fois que le module est initialis√©, garantir que la langue est √† jour
garantir(PBRIT)


def obtenir_mot(mot: MotPBRIT) -> Mot:
    return base_obtenir_mot(mot=mot, langue=PBRIT)


def obtenir_descendants(mot: MotPBRIT) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=PBRIT)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=PBRIT)
