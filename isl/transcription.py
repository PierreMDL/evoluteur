import re
from transcription import phonétiser as base_ph, accentuer as base_ac


def resolve_initial(match) -> str:
    corres = {
        "p": "pʰ", "t": "tʰ", "k": "kʰ",
        "sp": "sp", "st": "st", "sk": "sk",
        "b": "p", "d": "t", "g": "k",
        "hl": "ḷ", "hr": "ṛ", "hn": "ṇ", "hj": "ç", "hv": "kʰv",
        "sl": "stl",
    }

    if match.groups()[1]:
        corres.update({
            "k": "cʰ", "sk": "sc",
            "g": "c",
        })

    return corres.get(match.groups()[0], match.groups()[0]) + \
           ("" if match.groups()[1] == "j" and match.groups()[0][-1] in ["g", "k"] else match.groups()[1])


def resolve_single(match) -> str:
    corres = {
        "b": "p", "d": "t", "g": "k", "f": "v",
    }

    if match.groups()[0]:
        corres.update({
            "g": "ɣ",
        })

    if match.groups()[2]:
        corres.update({
            "g": "j",
        })

    return (match.groups()[0] or "") + \
           corres.get(match.groups()[1])


def resolve_clusters(match) -> str:
    corres = {
        "pp": "hp", "tt": "ht", "kk": "hk",
        "bb": "P", "dd": "T", "gg": "K",
        "ll": "tl",  # ne tient pas compte des mots d'emprunts bollur > /bolːʏr/
        "nn": "N", "rr": "R", "mm": "M", "ff": "F", "ss": "S",
        "lp": "ḷp", "lt": "ḷt", "lk": "ḷk",
        "rp": "ṛp", "rt": "ṛt", "rk": "ṛk",
        "np": "ṇp", "nt": "ṇt", "nk": "ǹk",
        "mp": "ṃp", "mt": "ṃt", "mk": "ṃk",
        "lb": "lp", "ld": "lt", "lg": "lk",
        "rb": "rp", "rd": "rt", "rg": "rk",
        "nb": "np", "nd": "nt", "ng": "ŋk",
        "mb": "mp", "md": "mt", "mg": "mk",
        "tl": "htl", "kl": "hkl", "pl": "hpl",
        "gl": "kl", "gr": "ɣr", "gn": "kn", "gt": "ꝁt",
        "pt": "ft", "kt": "ꝁt", "ks": "ꝁs",
        "fl": "pl", "fn": "pn", "fnd": "mt", "fnt": "ṃt",
        "sl": "stl", "lf": "lv", "rf": "rv", "rsl": "ṛstl",
        "vg": "vk",
    }

    if match.groups()[0]:
        corres.update({
            "nn": "tn",
        })

    if match.groups()[2]:
        corres.update({
            "lk": "ḷc", "rk": "ṛc", "nk": "ńc", "mk": "ṃc",
            "lg": "lc", "rg": "rc", "ng": "ɲc", "mg": "mc",
            "kk": "ʰc", "gg": "C",
        })

    return (match.groups()[0]) + \
           corres.get(match.groups()[1], match.groups()[1]) + \
           ("" if match.groups()[2] == "j" and match.groups()[1][-1] in ["g", "k"] else match.groups()[2])


def resolve_vowels(match) -> str:
    corres = {
        "e": "ė", "i": "ɪ", "o": "ȯ", "u": "ʏ", "y": "ɪ",
        "á": "au", "é": "je", "í": "i", "ó": "ou", "ú": "u", "ý": "i",
        "au": "œy", "ey": "ei", "ö": "œ", "æ": "ai",
    }

    if match.groups()[1] in ["ɲ", "ń", "ŋ", "ǹ"]:
        corres.update({
            "a": "au", "e": "ei", "i": "i", "u": "u", "y": "i",
            "é": "ei", "ö": "œy",
        })

    return corres.get(match.groups()[0].lower(), match.groups()[0].lower()) + \
           ("ː" if not match.groups()[1] and match.groups()[0].isupper() else "") + \
           (match.groups()[1] or "")


def régexiser(entrée: str) -> str:

    # Ortho
    entrée = re.sub("[þðx]", lambda match: {"þ": "ŧ", "ð": "đ", "x": "ꝁs"}.get(match.group()), entrée)

    # Accentuation
    entrée = re.sub("(au|ei|ey|[aeiouyöáéíóúýæ])", lambda match: match.group().upper(), entrée, count=1)

    # Consonnes
    entrée = re.sub(
        "(au|ei|ey|[áéíóúýæ]?)(pp|tt|kk|bb|dd|gg|ll|rr|mm|ff|ss|nn|[lmnr][ptkbdgf]|g[lnrt]|vg|f[nl][dt]?|(?<!^)[ptk][lmnt]|(?<!^)r?sl)([jiyeíýæ]?)",
        resolve_clusters, entrée, flags=re.IGNORECASE)
    entrée = re.sub("((?i:[aeiouyöáéíóúýæ]))([bdg]|f(?![ft]))((?i:[jiyeíýæ]?))", resolve_single, entrée)
    entrée = re.sub("^(s?[ptkbdg]|sl|h[nrljv])([jiyeíýæ]?)", resolve_initial, entrée, flags=re.IGNORECASE)

    # Voyelles
    entrée = re.sub(
        "(?i:(au|ei|ey|[aeiouyöáéíóúýæ]))([ɲŋńǹh]|[ptklmnfs]{2}|s[ptk]|[ptk][lns]|[lmnrḷṃṇṛxɣ][ptkslmnrv]|gr|vk|ft|ꝁ[ts]|[PTKMNRLSF])?",
        resolve_vowels, entrée)

    return entrée


def accentuer(entrée: str, majuscule: bool = True) -> str:
    return base_ac(entrée, noyaux=["au", "ei", "œy", "ai", "ou"] + list("aėeɪiuʏoȯöœ"), place=1, majuscule=majuscule)


def transcrire(entrée: str) -> str:
    entrée = entrée.translate(str.maketrans("ŧđxɣ", "þðkg"))  # xt > gt ou kt!
    entrée = entrée.replace("ks", "x").replace("ç", "hj")

    return entrée


phonétiser = base_ph
