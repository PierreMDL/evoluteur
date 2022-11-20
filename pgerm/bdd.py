from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import PGERM, MotPGERM

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(PGERM)


def obtenir_mot(mot: MotPGERM) -> Mot:
    return base_obtenir_mot(mot=mot, langue=PGERM)


def obtenir_descendants(mot: MotPGERM) -> list[dict[str: Mot, str: list]]:
    return base_obtenir_descendants(mot=mot, langue=PGERM)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=PGERM)
