from langue import Langue, Mot
from .transcription import transcrire
from .innovations import évolution


class MotVHA(Mot):
    évolution = évolution

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)


class VHA(Langue):
    nom = "Vieux haut allemand"
    abréviation = "VHA"
    abréviation_parent = "POGERM"
    mot = MotVHA
