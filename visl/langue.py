from langue import Langue, Mot
from .transcription import transcrire, régexiser, runiser, syllabifier
from .innovations import évolution, évoluer


class MotVISL(Mot):
    évolution = évolution

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)

    def _régexiser(self, valeur: str) -> str:
        return régexiser(valeur)

    def _runiser(self, valeur: str) -> str:
        return runiser(valeur)

    def _syllabifier(self, valeur: str) -> list[dict]:
        return syllabifier(valeur)


class VISL(Langue):
    nom = "Vieil islandais"
    abréviation = "VISL"
    abréviation_parent = "PGERM"
    mot = MotVISL


__all__ = (
    "MotVISL",
    "VISL",
    "transcrire",
    "régexiser",
    "runiser",
    "syllabifier",
    "évolution",
    "évoluer",
)
