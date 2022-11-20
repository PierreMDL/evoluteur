from bdd import (
    garantir,
    obtenir_mot as base_obtenir_mot,
    obtenir_descendants as base_obtenir_descendants,
    obtenir_lexique as base_obtenir_lexique,
    Mot,
)

from .langue import PCELT, MotPCELT

# Chaque fois que le module est initialisé, garantir que la langue est à jour
garantir(PCELT)


def obtenir_mot(mot: MotPCELT) -> Mot:
    return base_obtenir_mot(mot=mot, langue=PCELT)


def obtenir_descendants(mot: MotPCELT) -> list[dict]:
    return base_obtenir_descendants(mot=mot, langue=PCELT)


def obtenir_lexique() -> list[Mot]:
    return base_obtenir_lexique(langue=PCELT)
