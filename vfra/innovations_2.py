import re
from innovations import ChangementPhonétique


# > Proto-roman ouest

class TraitementMFinal(ChangementPhonétique):
    motif = re.compile("(?i:[aeiouėɪʊ])m$")
    nom = "Traitement M final"

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes.group()[0].islower():
            return dict_de_groupes.group()[0]
        else:
            return dict_de_groupes.group()[0] + "n"


class AvancéeAccentDevantOcclusivePuisLiquide(ChangementPhonétique):
    motif = re.compile("(?P<pre>[AEIOUĖꞮƱ])(?P<inter>.+)(?P<post>[aeiouėɪʊ])(?=[ptkbdg][rl])")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        return dict_de_groupes.groupdict()["pre"].lower() + \
               dict_de_groupes.groupdict()["inter"] + \
               dict_de_groupes.groupdict()["post"].upper()


class PerteCompensatriceNAvantFricative(ChangementPhonétique):
    motif = re.compile("(?i:[aeiouėɪʊ])n(?=[szfv])")
    règle_remplacement = {
        "an": "ā", "en": "ē", "in": "ī", "on": "ō", "un": "ū",
        "An": "Ā", "En": "Ē", "In": "Ī", "On": "Ō", "Un": "Ū",
    }


class DisparitionDiphtongues(ChangementPhonétique):
    motif = re.compile("(?i:ae|oe|au)")
    règle_remplacement = {
        "ae": "ẹ", "oe": "ē", "au": "aw",
        "AE": "Ẹ", "OE": "Ē", "AU": "Aw",
    }


class RésolutionHiatus(ChangementPhonétique):
    motif = re.compile("[iėeuo](?=(?i:[aėeɪioʊuāẹēīōū]))")
    règle_remplacement = {
        "i": "j", "ė": "j", "e": "j", "u": "w", "o": "w",
    }


class Disparition_W(ChangementPhonétique):
    motif = re.compile("(?<=pp|tt|kk)w"  
                       "|w(?=[uoūō])"
                       "|(?<=[kg])w(?=[juoUO])"
                       # "|w(?=j)"  # sometimes
                       # "|w(?=(?i:[aėeiāẹēī]))"  # "occasionally" /feˈbrwaːrjus/ > /feˈbraːrjus/
                       "",
                       re.VERBOSE)


class DisparitionCompensatrice_W_J(ChangementPhonétique):
    motif = re.compile("w[OŌ]|j[EĒ]")
    règle_remplacement = {"wO": "Ō", "wŌ": "Ō", "jE": "Ē", "jĒ": "Ē"}


class Assimilation_gj_dj_Intervocaliques(ChangementPhonétique):
    motif = re.compile("(?<=(?i:[aėeɪioʊuāẹēīōū]))[gd](?=j(?i:[aėeɪioʊuāẹēīōū]))")


class Palatalisation(ChangementPhonétique):
    motif = re.compile("[tknl]j")
    règle_remplacement = {
        "tj": "tsj", "kj": "c", "nj": "ɲ", "lj": "ʎ",
    }


class GéminationConsonnesPalatalesIntervocaliques(ChangementPhonétique):
    motif = re.compile("(?<=(?i:[aėeɪioʊuāẹēīōū]))("
                       "tsj|"  # irregularly
                       "[cɲʎ]"  # regularly
                       ")(?=(?i:[aėeɪioʊuāẹēīōū]))")
    règle_remplacement = {
        "tsj": "ttsj", "c": "cc", "ɲ": "ɲɲ", "ʎ": "ʎ",
    }


class Renforcement_j(ChangementPhonétique):
    motif = re.compile("(?P<pre>"
                       "^|"
                       "(?i:[aėeɪioʊuāẹēīōū])|"
                       "[rn]d"
                       ")j(?=(?i:[aėeɪioʊuāẹēīōū]))")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if len(dict_de_groupes.groupdict()["pre"]) == 0:
            return "ɟ"
        elif len(dict_de_groupes.groupdict()["pre"]) == 1:
            return dict_de_groupes.groupdict()["pre"] + "ɟɟ"
        else:
            return dict_de_groupes.groupdict()["pre"][0] + "ɟ"  # "variably ɟ or dzj"


class Affaiblissement_g_DevantConsonneNasale(ChangementPhonétique):
    motif = re.compile("g[nm]")
    règle_remplacement = {"gn": "ǥn", "gm": "wm"}


class Fricatisation_b_w_Intervocaliques(ChangementPhonétique):
    motif = re.compile("^w|"
                       "(?<=(?i:[aėeɪioʊuāẹēīōū]))[bw](?=(?i:[aėeɪioʊuāẹēīōū]))|"
                       "([rl]b)")
    règle_remplacement = "ƀ"


class Disparition_ƀ_AvecVoyellePostérieure(ChangementPhonétique):
    motif = re.compile("(?<=(?i:[oʊuōū]))ƀ|"
                       "ƀ(?=(?i:[oʊuōū]))")


class Simplification_ks(ChangementPhonétique):
    motif = re.compile("(?i:[aėeɪioʊuāẹēīōū])ks(?i:[aėeɪioʊuāẹēīōū])|"  #  len = 4
                       ".ks$|"  # len = 3
                       "ks")  # len = 2

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if len(dict_de_groupes.group()) == 2:
            return "s"
        elif len(dict_de_groupes.group()) == 3:
            return dict_de_groupes.group()[0] + "s"
        else:
            return dict_de_groupes.group()[0] + "sk" + dict_de_groupes.group()[-1]  # "sometimes"


class ÉpenthèseInitiale(ChangementPhonétique):
    motif = re.compile("^s(?=[ptk])")
    règle_remplacement = "is"
    nom = "Épenthèse initiale"


# class PROMO_ÉpenthèseFinale(ChangementPhonétique):
#     motif = re.compile("[^AĖEꞮIOƱUĀẸĒĪŌŪ]$")
#
#     def règle_remplacement(self, dict_de_groupes):
#         res = re.findall("[aėeɪioʊuāẹēīōū]", mot)
#         if len(res) == 0:
#             return appliquer(self.motif, lambda match: match.group() + "e", mot)
#         else:
#             return mot


class RééquilibreVocalique(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        forme_phono = re.sub("[āẹēīōū]", lambda match: {"ā": "a", "ẹ": "ė", "ē": "e", "ī": "i", "ō": "o", "ū": "u"}.get(match.group()), forme_phono)
        forme_phono = re.sub("[AĖEIOU](?![^āẹēīōūaėeiou]{2})", lambda match: {'A': 'Ā', 'Ė': 'Ẹ', 'E': 'Ē', 'I': 'Ī', 'O': 'Ō', 'U': 'Ū'}.get(match.group()), forme_phono)  # allongement ??
        forme_phono = re.sub("[ĀẸĒĪŌŪ]", lambda match: {"Ā": "A", "Ẹ": "Ė", "Ē": "E", "Ī": "I", "Ō": "O", "Ū": "U"}.get(match.group()), forme_phono)  # effondrement longueur
        forme_phono = re.sub("[ėȯ]", lambda match: {"ė": "e", "ȯ": "o"}.get(match.group()), forme_phono)  # à priori inutile pour l'instant
        forme_phono = re.sub("[iu](?!$)", lambda match: {"i": "ɪ", "u": "ʊ"}.get(match.group()), forme_phono)
        return forme_phono


# > Proto-gallo-ibéro-roman

class ConvergencePalatalisation(ChangementPhonétique):
    motif = re.compile("cc?")
    règle_remplacement = {"c": "tsj", "cc": "ttsj"}


class Diphtongaison(ChangementPhonétique):
    motif = re.compile("[ĖȮ](?![^aėeɪiȯoʊu]{2})")
    règle_remplacement = {"Ė": "jĖ", "Ȯ": "Ȯw"}


class LénitionIntervocalique(ChangementPhonétique):
    motif = re.compile("(?i:(?<=[aeiouėȯɪʊ]))(tsj|[gpk]l|[bdgfptk])(?i:(?=[aeiouėȯɪʊ]))")
    règle_remplacement = {
        "b": "ƀ", "d": "đ", "g": "j", "f": "ƀ",
        "p": "b", "t": "d", "k": "g",
        "pl": "bl", "kl": "gl", "gl": "jl",
        "tsj": "dzj",
    }


class LénitionFinale(ChangementPhonétique):
    motif = re.compile("(?i:(?<=[aėeɪiȯoʊu]))[td]$")
    règle_remplacement = {"t": "d", "d": "đ"}


class Mouillage(ChangementPhonétique):
    motif = re.compile("(?<!^)(gn|ngj|gl|jl)")
    règle_remplacement = {"gn": "ɲ", "ngj": "ɲ", "gl": "ʎ", "jl": "ʎ"}



évolution = [
    # PROMO_DisparitionH
    TraitementMFinal,
    AvancéeAccentDevantOcclusivePuisLiquide,  # deux contrexemples : /ˈpalpebras/ and /ˈpullitra/
    PerteCompensatriceNAvantFricative,  # "often retained, or restored, in the prefixes in- or con-, ..."
    DisparitionDiphtongues,  # "In certain rural accents /ae̯ au̯ / > /eː/ and /oː/ respectively in Classical times"
    RésolutionHiatus,  #  "The same applies to stressed front and back vowels in antepenultimate position, ..."
    Disparition_W,
    DisparitionCompensatrice_W_J,  #  "/i(ː)/ in hiatus before an unstressed /i(ː)/ generally deletes"
    Assimilation_gj_dj_Intervocaliques,
    Palatalisation,
    GéminationConsonnesPalatalesIntervocaliques,
    Renforcement_j,  # "The sequence [nɟ] sometimes assimilates to [ɲɲ]"
    Affaiblissement_g_DevantConsonneNasale,
    Fricatisation_b_w_Intervocaliques,
    Disparition_ƀ_AvecVoyellePostérieure,
    Simplification_ks,
    ÉpenthèseInitiale,
    # PROMO_ÉpenthèseFinale,
    RééquilibreVocalique,
    ConvergencePalatalisation,
    Diphtongaison,
    LénitionIntervocalique,
    LénitionFinale,
]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée


candidats = [
    "rEm",
    "Integram",
    "spOnsa",
    "pOEna",
    "kAElum",
    "kAUsa",
    "fĪlium",
    "sApuī",
    # "battŪere",
    "kArduum",
    "Unguō",
    "kwOmodo",
    "kOkwo",
    "duŌdecim",
    # "parIetēs",
    "lAkweum",
    # "kawEola",
    # "plUwia",
    "mEdium",
    "tAkeo",
    "tItio",
    "medietĀtem",
    "ekstrĀneum",
    "hOrdeum",
    "werēkUndia",
    "sAgma",
    "rĪwus",
    "pAks",
    "kOrem",
    "mAkulā",
    "pOpulum",
    "kiwitĀtem",
    "pEtra",
    "sEptem",
]
