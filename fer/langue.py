from langue import Langue, Mot
from .transcription import régexiser


class MotFER(Mot):
    def _régexiser(self, valeur: str) -> str:
        return régexiser(valeur)


class FER(Langue):
    nom = "Féringien"
    abréviation = "FER"
    abréviation_parent = "VISL"
    mot = MotFER
