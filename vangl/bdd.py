from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import VANGL, MotVANGL

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(VANGL)


def obtenir_mot(mot: MotVANGL) -> Mot:
    return base_obtenir_mot(mot=mot, langue=VANGL)


def obtenir_descendants(mot: MotVANGL) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=VANGL)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=VANGL)
