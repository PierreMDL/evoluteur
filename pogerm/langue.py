from langue import Langue, Mot
from .transcription import transcrire, régexiser
from .innovations import évolution


class MotPOGERM(Mot):
    évolution = évolution

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)

    def _régexiser(self, valeur: str) -> str:
        return régexiser(valeur)


class POGERM(Langue):
    nom = "Proto-ouest-germanique"
    abréviation = "POGERM"
    abréviation_parent = "PGERM"
    mot = MotPOGERM
