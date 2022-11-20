from langue import Langue, Mot
from .transcription import transcrire


class MotISL(Mot):
    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)


class ISL(Langue):
    nom = "Islandais"
    abréviation = "ISL"
    abréviation_parent = "VISL"
    mot = MotISL
