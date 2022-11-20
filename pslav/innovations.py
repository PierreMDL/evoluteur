import re
from innovations import ChangementPhonétique, DéplacementAccent


class Satemisation(ChangementPhonétique):
    motif = re.compile("[ḱǵ]ʰ?")
    règle_remplacement = {"ḱ": "s", "ǵ": "z", "ǵʰ": "z"}
    notes = "This sound change was incomplete, in that all Baltic and Slavic languages have instances where PIE" \
            " palatovelars appear as *k and *g, often in doublets (i.e. etymologically related words, where one" \
            " has a sound descended from *k or *g and the other has a sound descended from *ś or *ź)"


class Delabialisation(ChangementPhonétique):
    motif = re.compile("ʷ(?=[ouOUōūŌŪ])")


class RUKI(ChangementPhonétique):
    motif = re.compile("(?<=[ruUkiI])s")
    règle_remplacement = "ʃ"


class PerteDentalesFinales(ChangementPhonétique):
    motif = re.compile("[td]$")


class PerteAspiration(ChangementPhonétique):
    motif = re.compile("ʰ")


class FermetureDevantSonorantes(ChangementPhonétique):
    motif = re.compile("[ēōĒŌ](?=[lmnrwj])")
    règle_remplacement = {"ē": "ī", "Ē": "Ī", "ō": "ū", "Ō": "Ū"}


class DisparitionSonorantesAprèsLongues(ChangementPhonétique):
    motif = re.compile("(?<=[āēīōūĀĒĪŌŪ])[lmnrwj]")


class Rétractation_o(ChangementPhonétique):
    motif = re.compile("[oōOŌ]")
    règle_remplacement = {"o": "a", "ō": "ā", "O": "A", "Ō": "Ā"}

