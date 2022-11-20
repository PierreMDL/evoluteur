from langue import Langue, Mot
from .transcription import régexiser, transcrire, runiser
from .innovations import évolution


class MotPITAL(Mot):
    évolution = évolution

    def _régexiser(self, valeur: str) -> str:
        return régexiser(valeur)

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)

    def _runiser(self, valeur: str) -> str:
        return runiser(valeur)


class PITAL(Langue):
    nom = "Proto-italique"
    abréviation = "PITAL"
    abréviation_parent = "PIE"
    mot = MotPITAL
