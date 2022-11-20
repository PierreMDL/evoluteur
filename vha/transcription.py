import re


def transcrire(entrée: str) -> str:
    entrée = entrée.lower()
    entrée = entrée.replace("tȥ", "z")
    entrée = re.sub("ʃ(?=[aeiou])", "sk", entrée)
    entrée = entrée.translate(str.maketrans("ꝁŧxʃȥ", "hþhsz"))  # attention graphie ꝁ et x => h
    return entrée
