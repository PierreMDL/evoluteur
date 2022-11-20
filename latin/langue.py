from langue import Langue, Mot
from .innovations import évolution
from .transcription import transcrire


class MotLATIN(Mot):
    évolution = évolution

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)


class LATIN(Langue):
    nom = "Latin"
    abréviation = "LATIN"
    abréviation_parent = "PITAL"
    mot = MotLATIN
