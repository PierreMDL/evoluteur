from transcription import syllabifier as base_syllabifier


def transcrire(entrée: str) -> str:
    entrée = entrée.lower()
    entrée = entrée.translate(str.maketrans("ȧảęẻįǫỏųỷởàẽèĩõòũỳờ", "aaeeioǫuyøáéǽíóǭúýǿ"))
    entrée = entrée.replace("ks", "x").replace("iū", "jū").replace("iō", "jō").replace("ọ", "ǫ́")
    entrée = entrée.translate(str.maketrans("āēīōūȳǣȯėẹ", "áéíóúýǽǫeǽ"))
    entrée = entrée.translate(str.maketrans("ŧđ", "þð"))
    return entrée


def régexiser(conv: str) -> str:
    conv = conv.translate(str.maketrans("þðǫ", "ŧđȯ"))
    return conv


def runiser(entrée: str) -> str:
    corres = {
        "nk": "ᛜ", "ng": "ᛜ", "f": "ᚠ", "u": "ᚢ", "ū": "ᚢ", "þ": "ᚦ", "a": "ᚨ", "ā": "ᚨ", "ą": "ᚨ", "ã": "ᚨ", "r": "ᚱ",
        "k": "ᚲ", "g": "ᚷ", "w": "ᚹ", "h": "ᚺ", "n": "ᚾ", "i": "ᛁ", "j": "ᛃ", "ī": "ᛇ", "p": "ᛈ", "z": "ᛉ", "s": "ᛊ",
        "t": "ᛏ", "b": "ᛒ",  "e": "ᛖ", "ē": "ᛖ", "m": "ᛗ", "l": "ᛚ", "d": "ᛞ", "o": "ᛟ", "ô": "ᛟ", "ō": "ᛟ", "õ": "ᛟ"
    }

    for key, value in corres.items():
        entrée = entrée.replace(key, value)
    return entrée


def syllabifier(valeur: str) -> list[dict]:
    noyaux = list("ȯọȧảeięẻįǫỏųỷởàẽèĩõòũỳờ")

    return base_syllabifier(entrée=valeur, noyaux=noyaux)
