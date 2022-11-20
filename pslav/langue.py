from langue import Langue, Mot
from .transcription import transcrire, régexiser


class MotPSLAV(Mot):
    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)

    def _régexiser(self, valeur: str) -> str:
        return régexiser(valeur)


class PSLAV(Langue):
    nom = "Proto-slavique"
    abréviation = "PSLAV"
    abréviation_parent = "PBALTSLAV"
    mot = MotPSLAV
