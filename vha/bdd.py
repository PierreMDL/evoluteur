from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import VHA, MotVHA

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(VHA)


def obtenir_mot(mot: MotVHA) -> Mot:
    return base_obtenir_mot(mot=mot, langue=VHA)


def obtenir_descendants(mot: MotVHA) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=VHA)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=VHA)
