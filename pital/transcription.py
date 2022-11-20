def régexiser(entrée: str) -> str:
    entrée = entrée.translate(str.maketrans("fhβðɣ", "ꝑꝁƀđǥ"))
    # ^ normalement plus de θ en PITAL (controversé), convention ƀđǥ : βðɣ, il faut prendre ça en compte aussi

    # entrée = re.sub("[aeoāēō]i|[ao]u|[aeiouāēīōūə]", lambda voyelle: voyelle.group().upper(), entrée, count=1)  # FIXME accentuer()
    return entrée


def transcrire(entrée: str) -> str:
    entrée = entrée.lower()
    entrée = entrée.translate(str.maketrans("ꝑꝁđƀǥj", "fhðβɣi"))
    return entrée


def runiser(conv: str) -> str:
    corres = {
        "a": "𐌀", "b": "𐌁", "c": "𐌂", "d": "𐌃", "e": "𐌄", "v": "𐌅", "z": "𐌆", "h": "𐌇", "ŧ": "𐌈", "i": "𐌉",
        "k": "𐌊", "l": "𐌋", "m": "𐌌", "n": "𐌍", "ʃ": "𐌎", "o": "𐌏", "p": "𐌐", "ś": "𐌑", "q": "𐌒", "r": "𐌓",
        "s": "𐌔", "t": "𐌕", "u": "𐌖", "x": "𐌗", "ꝑ": "𐌘", "ꝁ": "𐌙", "f": "𐌚",
    }

    for key, value in corres.items():
        conv = conv.replace(key, value)
    return conv
