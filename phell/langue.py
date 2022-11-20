from langue import Langue, Mot
from .innovations import évolution


class MotPHELL(Mot):
    évolution = évolution


class PHELL(Langue):
    nom = "Proto-hellénique"
    abréviation = "PHELL"
    abréviation_parent = "PIE"
    mot = MotPHELL
