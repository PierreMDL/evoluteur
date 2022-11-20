import re


def régexiser(entrée: str) -> str:
    entrée = re.sub("ě̀|ę̄|[aàěęuùyioǫĭьŭъ]", lambda match: {
        "ě̀": "ē",
        # "o": "a",  # pas clair
        "o": "o",
        "a": "ā", "à": "ā", "ě": "ē", "ę": "ẻ", "ę̄": "ẽ", "ǫ": "ỏ",
        "i": "ī", "u": "ū", "y": "ȳ", "ù": "ū",
        "ь": "i", "ĭ": "i", "ъ": "u", "ŭ": "u"}.get(match.group()), entrée)
    entrée = re.sub("d[zž]|[cčšžx]", lambda match: {
        "dz": "ʣ", "dž": "ʤ", "c": "ʦ", "č": "ʧ", "š": "ʃ", "ž": "ʒ", "x": "ꝁ"
    }.get(match.group()), entrée)

    return entrée


def transcrire(entrée: str, à_la_slaviste: bool = False) -> str:
    corres = {
        "ʦ": "c", "ʧ": "č", "ʃ": "š", "ꝁ": "x", "ʒ": "ž", "ʣ": "dz", "ʤ": "dž",
    }

    if à_la_slaviste:
        corres.update({
            "ā": "a", "ē": "ě", "ẻ": "ę", "ẽ": "ę̄", "a": "o", "ỏ": "ǫ",
            "ī": "i", "ū": "u", "ȳ": "y",
            "i": "ь", "u": "ъ",
        })

    entrée = re.sub("[" + "".join(corres.keys()) + "]", lambda match: corres.get(match.group()), entrée)

    return entrée
