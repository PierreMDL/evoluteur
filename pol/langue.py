from langue import Langue, Mot
from .transcription import transcrire, régexiser
from .innovations import évolution


class MotPOL(Mot):
    évolution = évolution

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)

    def _régexiser(self, valeur: str) -> str:
        return régexiser(valeur)


class POL(Langue):
    nom = "Polonais"
    abréviation = "POL"
    abréviation_parent = "PSLAV"
    mot = MotPOL
