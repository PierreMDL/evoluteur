import re
from transcription import phonétiser as base_ph, accentuer as base_ac


def régexiser(entrée: str) -> str:
    entrée = re.sub("ch|[oóeyłńw]", lambda match: {"ch": "ꝁ", "o": "ȯ", "ó": "u", "e": "ė", "y": "ɨ", "ł": "w", "ń": "ɲ", "w": "v"}.get(match.group()), entrée)
    entrée = re.sub("(dz|s|c|z|n)?i(?=[aeouėȯąę])", lambda match: {
        "dzi": "ʥ", "si": "ɕ", "ci": "ʨ", "zi": "ʑ", "ni": "ɲ", "i": "ʲ"}.get(match.group()), entrée)
    entrée = re.sub("[śćź]|(dz|s|c|z|n)(?=i)", lambda match: {
        "ś": "ɕ", "ć": "ʨ", "ź": "ʑ",
        "dz": "ʥ", "s": "ɕ", "c": "ʨ", "z": "ʑ", "n": "ɲ"}.get(match.group()), entrée)
    entrée = re.sub("sz|cz|rz|d?ż|c|dz", lambda match: {"sz": "ʂ", "cz": "ʈ", "rz": "ʐ", "dż": "ɖ", "ż": "ʐ", "c": "ʦ", "dz": "ʣ"}.get(match.group()), entrée)
    entrée = re.sub("[vʐzbdg]$", lambda match: {"v": "f", "ʐ": "ʂ", "z": "s", "b": "p", "d": "t", "g": "k"}.get(match.group()), entrée)
    entrée = re.sub("[vʐzbdg](?=[ɕʂptʈʦʨkꝁs])", lambda match: {"v": "f", "ʐ": "ʂ", "z": "s", "b": "p", "d": "t", "g": "k"}.get(match.group()), entrée)
    entrée = re.sub("(?<=[ptkꝁs])[vʐz]", lambda match: {"v": "f", "ʐ": "ʂ", "z": "s"}.get(match.group()), entrée)
    entrée = re.sub("[ąę][gkdɖʣʑʥtʈʦʨʂ]?", lambda match: {
        "ą": "ỏ", "ąd": "ȯnd", "ąg": "ȯŋg", "ąk": "ȯŋk", "ąʂ": "ỏʂ", "ąʦ": "ȯnʦ",
        "ę": "ė", "ęg": "ėŋg", "ęk": "ėŋk",
        "ęʑ": "ėɲʑ", "ęd": "ėnd", "ęɖ": "ęnɖ", "ęʣ": "ėnʣ", "ęʥ": "ėɲʥ",
        "ęʂ": "ẻʂ", "ęt": "ėnt", "ęʈ": "ęnʈ", "ęʦ": "ėnʦ", "ęʨ": "ėɲʨ",
    }.get(match.group()), entrée)
    entrée = re.sub("n(?=[kg])", "ŋ", entrée)

    return entrée


def transcrire(entrée: str) -> str:
    corres = {
        "ɲ": "ń", "ɕ": "ś", "ʥ": "dź", "ʨ": "ć", "ʑ": "ź",
        "ʦ": "c", "ʃ": "sz", "ʧ": "cz", "ʒ": "ż", "ř": "rz", "ʣ": "dz", "ʤ": "dż",
        "ꝁ": "ch", "v": "w", "w": "ł",
        "ả": "ą", "ẻ": "ę",
    }

    corres_avec_i = {
        "ɲ": "n", "ɕ": "s", "ʥ": "dz", "ʨ": "c", "ʑ": "z",
    }

    corres_sans_i = {
        "ɲ": "ni", "ɕ": "si", "ʥ": "dzi", "ʨ": "ci", "ʑ": "zi",
    }

    entrée = re.sub("[ảẻꝁʃʧʣʦʒřvwʤ]|[ɲʥɕʨʑ](?![aeiouyảẻ])", lambda match: corres.get(match.group()), entrée)
    entrée = re.sub("[ɲʥɕʨʑ](?=i)", lambda match: corres_avec_i.get(match.group()), entrée)
    entrée = re.sub("[ɲʥɕʨʑ](?!i)", lambda match: corres_sans_i.get(match.group()), entrée)
    entrée = re.sub("(?<=[wpbm])j", "i", entrée)

    return entrée


def accentuer(entrée: str, majuscule: bool = True) -> str:
    return base_ac(entrée, noyaux=list("aėẻiɨȯỏu"), place=-2, majuscule=majuscule)


phonétiser = base_ph
