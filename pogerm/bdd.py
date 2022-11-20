from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import POGERM, MotPOGERM

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(POGERM)


def obtenir_mot(mot: MotPOGERM) -> Mot:
    return base_obtenir_mot(mot=mot, langue=POGERM)


def obtenir_descendants(mot: MotPOGERM) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=POGERM)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=POGERM)
