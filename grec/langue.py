from langue import Langue, Mot
from .transcription import régexiser


class MotGREC(Mot):
    def _régexiser(self, valeur: str) -> str:
        return régexiser(valeur)


class GREC(Langue):
    nom = "Grec"
    abréviation = "GREC"
    abréviation_parent = "PHELL"
    mot = MotGREC
