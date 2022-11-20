from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import VFRA, MotVFRA

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(VFRA)


def obtenir_mot(mot: MotVFRA) -> Mot:
    return base_obtenir_mot(mot=mot, langue=VFRA)


def obtenir_descendants(mot: MotVFRA) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=VFRA)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=VFRA)
