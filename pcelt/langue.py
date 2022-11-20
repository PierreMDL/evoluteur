from langue import Langue, Mot
from .transcription import transcrire, régexiser
from .innovations import évolution


class MotPCELT(Mot):
    évolution = évolution

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)

    def _régexiser(self, valeur: str) -> str:
        return régexiser(valeur)


class PCELT(Langue):
    nom = "Proto-celtique"
    abréviation = "PCELT"
    abréviation_parent = "PIE"
    mot = MotPCELT
