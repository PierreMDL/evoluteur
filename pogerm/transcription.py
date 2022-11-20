import re


def régexiser(entrée: str) -> str:
    entrée = re.sub("[aāą]", lambda ant: {'a': 'ȧ', 'ā': 'ạ', 'ą': 'ả', 'ą̄': 'à'}.get(ant.group()), entrée)
    entrée = re.sub("ȧi|ȧu|eu|iu|[ȧeiouạēīōūảįųàĩòũ]", lambda voyelle: voyelle.group().upper(), entrée, count=1)
    entrée = entrée.translate(str.maketrans("bgfþh", "ƀǥꝑŧꝁ"))
    entrée = re.sub("(?=^|m)ƀ|ƀƀ|(?<=n)ǥ|ǥǥ", lambda fricative: {"ƀƀ": "bb", "ƀ": "b", "ǥ": "g", "ǥǥ": "gg"
                                                                 }.get(fricative.group()), entrée)
    return entrée


def transcrire(entrée: str) -> str:
    entrée = entrée.lower()
    entrée = entrée.translate(str.maketrans("ȧạảàŧꝁǥꝑƀ", "aāąãþhgfb"))
    return entrée
