from langue import Langue, Mot
from .transcription import transcrire, runiser
from .innovations import évolution


class MotVANGL(Mot):
    évolution = évolution

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)

    def _runiser(self, valeur: str) -> str:
        return runiser(valeur)


class VANGL(Langue):
    nom = "Vieil anglais"
    abréviation = "VANGL"
    abréviation_parent = "POGERM"
    mot = MotVANGL
