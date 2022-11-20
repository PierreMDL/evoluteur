import re
from innovations import ChangementPhonétique


# def remove_h(match):
#     groups = match.groupdict(default="")
#     quality_list = ["aAāĀ", "eEēĒ", "iIīĪ", "oOōŌ", "uUūŪ", "yYȳȲ"]
#     if any(map(lambda vowels: groups["pre"] in list(vowels) and groups["post"] in list(vowels), quality_list)):
#         long = {"o": "ō", "i": "ī", "e": "ē", "a": "ā", "u": "ū"}.get(groups["pre"].lower())
#         return long.upper() if (groups["pre"].isupper() or groups["post"].isupper()) else long
#     else:
#         return groups["pre"] + groups["post"]
# remove_h_and_resolve_hiatus.motif = "(?P<pre>[aeiouAEIOUāēīōūĀĒĪŌŪ]?)h(?P<post>[aeiouAEIOUāēīōūĀĒĪŌŪ]?)"
# proto_west_romance = re.sub(remove_h_and_resolve_hiatus.motif, remove_h_and_resolve_hiatus.remplacement, proto_west_romance)

class ÉpenthèseInitiale(ChangementPhonétique):
    motif = re.compile("^s(?=[ptk])")
    règle_remplacement = "is"


class BousculementVocalique(ChangementPhonétique):
    motif = re.compile("(?i:oe|ae|au|[aeiouyāēīōūȳ])")
    règle_remplacement = {
        "a": "a", "ā": "a", "e": "ė", "ē": "e", "i": "ɪ", "ī": "i", "o": "ȯ", "ō": "o", "u": "ʊ", "ū": "u", "y": "ɪ",
        "ȳ": "i", "ae": "ė", "oe": "e", "au": "aw",
        "A": "A", "Ā": "A", "E": "Ė", "Ē": "E", "I": "Ɪ", "Ī": "I", "O": "Ȯ", "Ō": "O", "U": "Ʊ", "Ū": "U", "Y": "Ɪ",
        "Ȳ": "I", "AE": "Ė", "OE": "E", "AU": "Aw",
    }


# Attention ! Ici motif cherche voyelle accentuée précédente, mais != unisyllabique !
class Disparition_m_Final(ChangementPhonétique):
    motif = re.compile("(?<![AEIOUĖȮꞮƱ])m$")
    description = "Le m final disparaît sauf dans les mots unisyllabique."


class Disparition_n_Assimilation_r_Avant_S(ChangementPhonétique):
    motif = re.compile("[nr](?=s)")
    règle_remplacement = {"n": "", "r": "s"}


class MétathèseFinale(ChangementPhonétique):
    motif = re.compile("[ėȯ]r$")
    règle_remplacement = {"ȯr": "rȯ", "ėr": "rė"}


class SyncopeMédiale(ChangementPhonétique):
    motif = re.compile("(?<=[gk])[aeiouėȯɪʊ](?=[lr][aeiouėȯɪʊ][^AEIOUĖȮꞮƱ]*$)")
    description = "Syncope de la voyelle médiale dans les mots suffixés en -culus, etc."


class DiphtongaisonHiatus(ChangementPhonétique):
    motif = re.compile("[ieɪė](?=(?i:[aeiouėȯɪʊ]))")
    règle_remplacement = "ʝ"


class Palatalisation(ChangementPhonétique):
    motif = re.compile("[kgdt][jʝ]|[kg](?=[eėiEĖI])")
    règle_remplacement = {
        "kj": "kkj", "kʝ": "kkj", "gj": "ʝ", "gʝ": "ʝ", "dj": "ʝ", "dʝ": "ʝ",
        "k": "kj", "g": "ʝ", "tj": "tj", "tʝ": "tj"
    }


class SecondePalatalisation(ChangementPhonétique):
    motif = re.compile("(kk|[kt])(?=j)")
    règle_remplacement = {"kk": "tts", "k": "ts", "t": "ts"}


class PalatalisationDevant_t_s(ChangementPhonétique):
    motif = re.compile("k(?=[ts])")
    règle_remplacement = "j"


class DiphtongaisonDansSyllabeOuverte(ChangementPhonétique):
    motif = re.compile("(?<![jʝw])[ĖȮ](?![^aeiouėȯɪʊj]{2})")
    règle_remplacement = {"Ė": "jE", "Ȯ": "wO"}


class SecondeSyncopeMédiale(ChangementPhonétique):
    motif = re.compile("(?i:(?<=[aeiouėȯɪʊ].)|(?<=[aeiouėȯɪʊ]..))[aeiouėȯɪʊ](?i:(?=.[aeiouėȯɪʊ])|(?=..[aeiouėȯɪʊ]))")


class MutationConsonnantique(ChangementPhonétique):
    motif = re.compile("(?<=(?i:[aeiouėȯɪʊ]))([ptkbdgf]|[pkg]l|tsj)(?=(?i:[aeiouėȯɪʊr]))|[td]$")
    règle_remplacement = {
        "b": "ƀ", "d": "đ", "g": "j", "f": "ƀ", "p": "b", "t": "d", "k": "g", "pl": "bl",
        "kl": "gl", "gl": "jl", "tsj": "dzj",
    }


class PalatalisationNasalesEtLiquides(ChangementPhonétique):
    motif = re.compile("(?<!^)(gn|ngj|gl|jl)")
    règle_remplacement = {"gn": "ɲ", "ngj": "ɲ", "gl": "ʎ", "jl": "ʎ"}


class Renforcement_j_InitialEtPostconsonnantique(ChangementPhonétique):
    motif = re.compile("(?<!(?i:[aeiouėȯɪʊzs]))ʝ")
    règle_remplacement = "dʒ"


class PalatalisationPostPalatales(ChangementPhonétique):
    motif = re.compile("(?<=[jʝ])([ptkbdgr])")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        return dict_de_groupes.group() + "j"


évolution = [
    # PROTO-WEST-ROMANCE
    ÉpenthèseInitiale,
    BousculementVocalique,
    Disparition_m_Final,
    Disparition_n_Assimilation_r_Avant_S,
    MétathèseFinale,
    SyncopeMédiale,
    DiphtongaisonHiatus,
    Palatalisation,

    # PROTO-GALLO-IBÉRO-ROMANCE
    SecondePalatalisation,
    PalatalisationDevant_t_s,
    DiphtongaisonDansSyllabeOuverte,
    SecondeSyncopeMédiale,
    MutationConsonnantique,
    PalatalisationNasalesEtLiquides,

    # EARLY OLD FRENCH
    Renforcement_j_InitialEtPostconsonnantique,
    PalatalisationPostPalatales,

]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée


lexique = {
    "syncope": ["kAlidum", "dormitOrium", "vIrides", "subitĀnum", "Okulus", "deskEndere", "mAkula"],
    "dissimilation": ["mOllere", "nUmerum"],
    "monophtongation": ["pOEna", "kAElum", "kAUsa"],
    "diphtongation": ["pEtra", "mAre", "flŌrem", "mĒ", "pĒjor"],
    "hiatus": ["kOhortem"],
    "métathèse": ["kwAttuor", "sUper"],
    "m final": ["nOwum", "rEm"],
    "palatalisation": ["ekstrĀneum", "mEdium", "gElū", "tAkeo", "tItio", "nOktem", "pAks", "medietĀtem"],
    "épenthèse": ["spĪnam"],
    "assimilation":  ["dOrsum"],
    "lénition": ["mAgum", "makerIa", "pOpulus", "lOkum"],
    "doublons": ["mAnika", "grĀnika", "windikĀre", "karrikĀre"]
}
