from langue import Langue, Mot
from .transcription import régexiser


class MotSAN(Mot):
    def _régexiser(self, valeur: str) -> str:
        return régexiser(valeur)


class SAN(Langue):
    nom = "Sanscrit"
    abréviation = "SAN"
    abréviation_parent = "PIE"
    mot = MotSAN
