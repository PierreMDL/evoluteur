from langue import Langue, Mot
from .transcription import transcrire
from .innovations_2 import évolution


class MotVFRA(Mot):
    évolution = évolution

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)


class VFRA(Langue):
    nom = "Vieux français"
    abréviation = "VFRA"
    abréviation_parent = "LATIN"
    mot = MotVFRA
