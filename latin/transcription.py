def transcrire(entrée: str) -> str:
    entrée = entrée.lower()
    entrée = entrée.replace("ks", "x").replace("kw", "qu")
    entrée = entrée.translate(str.maketrans("ɦwkɫj", "hvcli"))
    return entrée
