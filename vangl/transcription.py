import re


def transcrire(entrée: str) -> str:
    entrée = entrée.lower()
    entrée = entrée.replace("īu", "īo").replace("ǣȧ", "ēȧ").replace("īy", "īe")  # graphie diphtongue, īo > ēo pou tomber sur formes canoniques ! (triwwiz > trēow)
    entrée = entrée.replace("iu", "io").replace("æȧ", "eȧ").replace("iy", "ie")  # faire sauter pour travailler au corps avec formes phono.
    entrée = entrée.replace("dʤ", "ċġ").replace("nʤ", "nġ").replace("tʧ", "ċċ").replace("ʧ", "ċ").replace("ʃ",
                                                                                                                "sċ")
    entrée = entrée.replace("ks", "x")
    entrée = re.sub(re.compile("(?<=[rl])j"), "i", entrée)
    entrée = entrée.translate(str.maketrans("ŧꝁǥʝjk", "þhgġġc"))
    entrée = entrée.replace("ạ", "ā").replace("ȧ", "a")
    return entrée


def runiser(entrée: str) -> str:
    entrée = entrée.translate(str.maketrans("āēīōūǿǣȳ", "aeiouøæy"))
    corres = {  # j aussi ᛡ, s aussi ᚴ, ᛇ utilisé aussi pour i(:) ou h
        "io": "ᛡ", "ea": "ᛠ", "ks": "ᛉ", "ng": "ᛝ",
        "f": "ᚠ", "u": "ᚢ", "þ": "ᚦ", "o": "ᚩ", "r": "ᚱ", "k": "ᚳ", "g": "ᚷ", "w": "ᚹ", "h": "ᚻ", "n": "ᚾ", "i": "ᛁ",
        "j": "ᛄ", "p": "ᛈ", "s": "ᛋ", "t": "ᛏ", "b": "ᛒ", "e": "ᛖ", "m": "ᛗ", "l": "ᛚ", "ø": "ᛟ", "d": "ᛞ", "a": "ᚪ",
        "æ": "ᚫ", "y": "ᚣ"
    }

    for key, value in corres.items():
        entrée = entrée.replace(key, value)
    return entrée
