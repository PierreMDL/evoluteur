from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import LATIN, MotLATIN

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(LATIN)


def obtenir_mot(mot: MotLATIN) -> Mot:
    return base_obtenir_mot(mot=mot, langue=LATIN)


def obtenir_descendants(mot: MotLATIN) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=LATIN)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=LATIN)
