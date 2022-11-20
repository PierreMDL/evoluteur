from langue import Langue, Mot
from .innovations import évolution
from .transcription import régexiser, transcrire, runiser


class MotGOTH(Mot):
    évolution = évolution

    def _régexiser(self, valeur: str) -> str:
        return régexiser(valeur)

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)

    def _runiser(self, valeur: str) -> str:
        return runiser(valeur)


class GOTH(Langue):
    nom = "Gothique"
    abréviation = "GOTH"
    abréviation_parent = "PGERM"
    mot = MotGOTH
