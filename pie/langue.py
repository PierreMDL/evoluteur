from langue import Langue, Mot
from pie.transcription import régexiser, transcrire, syllabifier


class MotPIE(Mot):
    def _régexiser(self, valeur: str) -> str:
        return régexiser(valeur)

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)

    def _syllabifier(self, valeur: str) -> list[dict]:
        return syllabifier(valeur)


class PIE(Langue):
    nom = "Proto-indo-européen"
    abréviation = "PIE"
    abréviation_parent = None
    mot = MotPIE
