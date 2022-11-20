def régexiser(entrée: str) -> str:
    return entrée.translate(str.maketrans("ɸxy", "ꝑꝁj"))


def transcrire(entrée: str) -> str:
    entrée = entrée.lower()
    entrée = entrée.translate(str.maketrans("ꝑꝁj", "ɸxy"))
    return entrée
