from langue import Langue, Mot
from .transcription import transcrire, accentuer
from .innovations import évolution


class MotPGERM(Mot):
    évolution = évolution

    def _transcrire(self, valeur: str) -> str:
        return transcrire(valeur)

    def _accentuer(self, valeur: str, majuscule: bool = True) -> str:
        return accentuer(valeur, majuscule)


class PGERM(Langue):
    nom = "Proto-germanique"
    abréviation = "PGERM"
    abréviation_parent = "PIE"
    mot = MotPGERM
    grammaire = {
        "nom": {
            "nombre": ["SINGULIER", "PLURIEL"],
            "cas": ["NOMINATIF", "VOCATIF", "ACCUSATIF", "DATIF", "GÉNITIF", "INSTRUMENTAL"],
        },
        "verbe": {
            "temps": ["PASSÉ", "PRÉSENT"],
            "voix": ["ACTIF", "PASSIF"],
            "aspect": ["INDICATIF", "SUBJONCTIF", "IMPÉRATIF"],
        }
    }
