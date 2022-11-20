import re


def régexiser(valeur: str) -> str:
    regex = valeur.strip()
    regex = regex.replace("au", "ȯ").replace("ai", "ė").replace("ei", "ī")
    return regex


def transcrire(entrée: str) -> str:
    entrée = entrée.lower()
    entrée = entrée.replace("ng", "gg").replace("nkw", "gq").replace("kw", "q").replace("nk", "gk")
    entrée = re.sub("[ȧạėẹȯọī]", lambda res: {"ȧ": "a", "ạ": "ā", "ė": "ai", "ẹ": "ai", "ȯ": "au", "ọ": "au",
                                              "ī": "ei"}.get(res.group()), entrée)
    entrée = entrée.translate(str.maketrans("ꝑŧħƀđǥꝁ", "fþhbdgg"))
    return entrée


def runiser(entrée: str) -> str:
    corres = {
        "ai": "𐌰𐌹", "au": "𐌰𐌿", "ei": "𐌴𐌹", "iu": "𐌹𐌿",
        "a": "𐌰", "ā": "𐌰", "e": "𐌴", "ē": "𐌴", "i": "𐌹", "ī": "𐌹", "o": "𐍉", "ō": "𐍉", "u": "𐌿", "ū": "𐌿",
        "hw": "𐍈", "b": "𐌱", "d": "𐌳", "f": "𐍆", "g": "𐌲", "h": "𐌷", "j": "𐌾", "k": "𐌺", "l": "𐌻", "m": "𐌼", "n": "𐌽",
        "p": "𐍀", "q": "𐌵", "r": "𐍂", "s": "𐍃", "t": "𐍄", "þ": "𐌸", "w": "𐍅", "z": "𐌶"
    }

    for key, value in corres.items():
        entrée = entrée.replace(key, value)
    return entrée
