from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import ISL, MotISL

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(ISL)


def obtenir_mot(mot: MotISL) -> Mot:
    return base_obtenir_mot(mot=mot, langue=ISL)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=ISL)
