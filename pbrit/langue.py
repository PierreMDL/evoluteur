from langue import Langue, Mot
from .transcription import transcrire
from .innovations import évolution


class MotPBRIT(Mot):
    évolution = évolution

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)


class PBRIT(Langue):
    nom = "Proto-bryittonique"
    abréviation = "PBRIT"
    abréviation_parent = "PCELT"
    mot = MotPBRIT
