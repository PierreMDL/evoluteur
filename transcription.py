import re


corres_regex_ipa = {
    "ȧ": "ɑ", "ạ": "ɑː",
    "ả": "ɑ̃", "à": "ɑ̃ː",
    "ė": "ɛ", "ẹ": "ɛː", "ệ": "ɛːː",
    "ẻ": "ɛ̃",
    "ȯ": "ɔ", "ọ": "ɔː", "ộ": "ɔːː",
    "ỏ": "ɔ̃", "ò": "ɔ̃ː", "ȍ": "ɔ̃ːː",
    "ō": "oː", "ē": "eː",

    "ƀ": "β", "đ": "ð", "ǥ": "ɣ", "ꝑ": "ɸ", "ŧ": "θ", "ꝁ": "x",
    "ʣ": "d͡z", "ʥ": "d͡ʑ", "ɖ": "d͡ʐ", "ʤ": "d͡ʒ", "ʦ": "t͡s", "ʨ": "t͡ɕ", "ʈ": "t͡ʂ", "ʧ": "t͡ʃ",
    "g": "ɡ",
    "ḷ": "l̥", "ṛ": "r̥", "ṃ": "m̥", "ṇ": "n̥", "ń": "ɲ̊", "ǹ": "ŋ̊",
    "P": "pː", "T": "tː", "K": "kː", "C": "cː", "N": "nː", "R": "rː", "M": "mː", "F": "fː", "S": "sː",

    "ʲ": "j",

    "Ȧ": "Ɑ", "Ạ": "Ɑː",
    "Ả": "Ɑ̃", "À": "Ɑ̃ː",
    "Ė": "Ɛ", "Ẹ": "Ɛː", "Ệ": "Ɛːː",
    "Ẻ": "Ɛ̃",
    "Ȯ": "Ɔ", "Ọ": "Ɔː", "Ộ": "Ɔːː",
    "Ỏ": "Ɔ̃", "Ò": "Ɔ̃ː", "Ȍ": "Ɔ̃ːː",
    "Ō": "Oː", "Ē": "Eː",

}


def phonétiser(regex: str) -> str:
    """Renvoie la représentation IPA d'un mot en représentation REGEX"""
    ipa = regex.strip()

    caractères = "".join(corres_regex_ipa.keys())
    ipa = re.sub("[" + caractères + "]", lambda match: corres_regex_ipa.get(match.group()), regex)

    return ipa


# def syllabifier(entrée: str, noyaux: list) -> list:
#     noyaux.sort(key=lambda noy: len(noy), reverse=True)  # classe les diphtongues en premier
#     mono = "".join(list(filter(lambda voy: len(voy) == 1, noyaux)))
#     noyaux = "|".join(noyaux)
#
#     attaque = f"(?P<att>[^{mono}]*)"
#     noyau = f"(?P<noy>{noyaux})"
#     coda = f"(?P<cod>[^{mono}]*)"
#
#     motif = re.compile(attaque + noyau + coda)
#     syllabes = re.findall(motif, entrée)
#
#     return syllabes
#
#
# def trouver_accent(entrée: str, noyaux: list, place: int, majuscule=True) -> str:
#     """Syllabifie le mot pour trouver la syllabe portant l'accent"""
#
#     syllabes = syllabifier(entrée, noyaux)
#
#     # S'il n'y a aucune voyelle pour porter l'accent, pas d'accent
#     if len(syllabes) == 0:
#         return entrée
#
#     # Calcul de l'index de la syllabe accentuée par rapport au nombre de syllabes
#     if place < 0:
#         index_syllabe_accentuée = 0 - min(abs(place), len(syllabes))
#         inclure_dernière_syllabe = (index_syllabe_accentuée < -1)  # évite l'offshoot ([-1 + 1] = [0])
#     elif place > 0:
#         index_syllabe_accentuée = min(place, len(syllabes)) - 1
#         inclure_dernière_syllabe = True
#     else:
#         return entrée
#
#     découpé = []
#     découpé.extend([x for x in syllabes[:index_syllabe_accentuée]])
#     if majuscule:
#         découpé.extend([syllabes[index_syllabe_accentuée][0],
#                         syllabes[index_syllabe_accentuée][1].upper(),
#                         syllabes[index_syllabe_accentuée][2]])
#     else:
#         découpé.extend(["ˈ"] + [x for x in syllabes[index_syllabe_accentuée]])
#     découpé.extend([x for x in syllabes[index_syllabe_accentuée + 1:]] if inclure_dernière_syllabe else [])
#
#     return "".join([x for y in découpé for x in y])


"""
TODO - rate les consonnes 
"""
def syllabifier(entrée: str, noyaux: list) -> list[dict]:
    """Découpe l'entrée en syllabes selon la liste de noyaux donnée"""

    noyaux.sort(key=lambda noy: len(noy), reverse=True)  # classe les diphtongues en premier

    motif = re.compile("(ʲ?(?:" + "|".join(noyaux) + ")ː?)")
    # ^ ʲ pour capter le j qui, en polonais, n'est pas "consonnantique" en soi si proche d'une consonne

    éléments = list(filter(lambda x: len(x) > 0, re.split(motif, entrée)))
    avec_bornes = [""] + éléments + [""]  # rajout de bornes pour éviter les offshoots

    syllabes = []
    for nb, élément in enumerate(éléments, start=1):
        if (élément[0] in noyaux) or (élément[-1] in noyaux):
            syllabe = {}.fromkeys(["attaque", "noyau", "coda"], "")
            syllabe["attaque"] = avec_bornes[nb-1]
            syllabe["noyau"] = élément
            if len(avec_bornes[nb+1]) > 1:
                syllabe["coda"] = avec_bornes[nb+1][0]
                avec_bornes[nb+1] = avec_bornes[nb+1][1:]
            syllabes.append(syllabe)

            avec_bornes[nb] = ""

    if not syllabes:  # s'il n'y avait pas de noyau (ex. POL "z"), alors une syllabe sans noyau
        syllabe = {}.fromkeys(["attaque", "noyau", "coda"], "")
        syllabe["attaque"] = entrée
        syllabes.append(syllabe)
    else:  # s'il reste des consonnes (ex. VCC$), les rajoute
        syllabes[-1]["coda"] += avec_bornes[-2]

    return syllabes


def accentuer(entrée: str, noyaux: list, place: int, majuscule: bool = True) -> str:
    """Trouve l'accent du mot passé selon la place donnée

    place est la place de l'accent à chercher (index 1, rebours depuis -1)
    majuscule détermine si l'accent doit être indiqué par une majuscule sur la voyelle ou une apostrophe devant la syllabe
    """

    syllabes = syllabifier(entrée, noyaux)

    # S'il n'y a aucune voyelle pour porter l'accent, pas d'accent
    if len(syllabes) == 0:
        return entrée

    # Calcul de l'index de la syllabe accentuée par rapport au nombre de syllabes
    if place < 0:
        index_syllabe_accentuée = 0 - min(abs(place), len(syllabes))
        inclure_dernière_syllabe = (index_syllabe_accentuée < -1)  # évite l'offshoot ([-1 + 1] = [0])
    elif place > 0:
        index_syllabe_accentuée = min(place, len(syllabes)) - 1
        inclure_dernière_syllabe = True
    else:
        return entrée

    découpé = []
    découpé.extend(["".join(x.values()) for x in syllabes[:index_syllabe_accentuée]])
    if majuscule:
        découpé.extend([syllabes[index_syllabe_accentuée]["attaque"],
                        syllabes[index_syllabe_accentuée]["noyau"].upper(),
                        syllabes[index_syllabe_accentuée]["coda"]])
    else:
        découpé.extend(["ˈ"] + ["".join(syllabes[index_syllabe_accentuée].values())])
    découpé.extend(["".join(x.values()) for x in syllabes[index_syllabe_accentuée + 1:]] if inclure_dernière_syllabe else [])

    return "".join([x for x in découpé])


def transcrire(valeur: str) -> str:
    """Renvoie la transcription conventionnelle d'un mot en forme REGEX"""

    return valeur


def régexiser(valeur: str) -> str:
    """Renvoie la représentation REGEX de la forme conventionnelle d'un mot"""

    return valeur


def runiser(valeur: str) -> str:
    """Renvoie la représentation en runes de la forme conventionnelle d'un mot"""

    return valeur
