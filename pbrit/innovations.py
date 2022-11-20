from innovations import ChangementPhonétique
import re


class Traitement_kw(ChangementPhonétique):
    motif = re.compile("kʷ")
    règle_remplacement = "p"

class Renforcement_w_Initial(ChangementPhonétique):
    motif = re.compile("^w")
    règle_remplacement = "gʷ"


class Perte_f(ChangementPhonétique):
    motif = re.compile("^ꝑ")

class Traitement_s_Initial(ChangementPhonétique):
    motif = re.compile("^s[ꝑrw]?(?=(?P<apres>.))")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if len(dict_de_groupes.group()) == 2:
            return {"sꝑ": "ꝑ", "sr": "ꝑr", "sw": "ħʷ"}.get(dict_de_groupes.group())
        elif dict_de_groupes.group("apres") in list("aeiouāēīōūAEIOUĀĒĪŌŪ"):
            return "ħ"
        elif dict_de_groupes.group("apres") in list("lmn"):
            return ""
        else:
            return "s"


# ɸ > w avec seuls exemple concrets loɸernos > llowern, et uɸo- > uwo- > wo- > gwo-, avec contre-exemple neɸūss > nei...
# attention au kw > p > VbV
class LénitionIntervocalique(ChangementPhonétique):
    motif = re.compile("(?i:(?<=[aeiouāēīōū])[bdgꝑptkm](?=[aeiouāēīōū]))|(?<!^)[bdgꝑptkm](?=[rl])")
    règle_remplacement = {"p": "b", "t": "d", "k": "g",
                          "b": "ƀ", "d": "đ", "g": "ǥ",
                          "ꝑ": "w", "m": "ᵬ"}

class TraitementGéminées(ChangementPhonétique):
    motif = re.compile("(?P<plosive>[ptkd])(?P=plosive)")
    règle_remplacement = {"pp": "ꝑ", "tt": "ŧ", "kk": "ꝁ", "dd": "d"}


# [lr]p > f (emprunt ?) manque de ressource
# [^lmnr][ptkbdg] pas très clair
class FricatisationAprèsLiquides(ChangementPhonétique):
    motif = re.compile("(?<=[lr])[kbdg]|(?<=[r])[t]")
    règle_remplacement = {"t": "ŧ", "k": "ꝁ", "b": "ƀ", "d": "đ", "g": "ǥ"}


class MutationsVocaliques(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        # u ou i courts suivis d'un a(:) dans la syllabe finale
        umlaut_en_a_final = re.compile("(?i:(?<![aoe])[ui](?=[^aeiouāīū]+[aā][^aeiouāīū]*$))")
        forme_phono = re.sub(umlaut_en_a_final, lambda cand: {"u": "o", "i": "e",
                                                              "U": "O", "I": "E"}.get(cand.group()), forme_phono)

        # e suivi d'un i dans la syllabe finale
        umlaut_du_i_court_final = re.compile("(?i:[e](?=[^aeiouāīū]+[i][^aeiouāīū]*$))")
        forme_phono = re.sub(umlaut_du_i_court_final, lambda cand: {"e": "ɨ", "E": "Ɨ"}.get(cand.group()), forme_phono)

        # a, e, o, u suivis d'un ī ou j dans la syllabe finale
        # "front high vowels", mais uxsū > üx, dubrokū > düβrgi semble indiquer que ū aussi, peut-être ū > ī déjà à ce moment-là ?
        # aussi kanawū > kėnėw
        # sauf que swesūr > hwehir, swekrū > hwegr
        umlaut_en_i_final = re.compile("(?i:[aeou](?=[^aeiouāīū]+[īūj][^aeiouāīū]*$))")
        forme_phono = re.sub(umlaut_en_i_final, lambda cand: {"u": "y", "o": "y", "e": "ɨ", "a": "ɛ",
                                                              "U": "Y", "O": "Y", "E": "Ɨ", "A": "Ɛ"
                                                              }.get(cand.group()), forme_phono)


        # a, e, o, u suivis d'une voyelle antérieure haute ou j
        umlaut_en_i_interne = re.compile("(?i:[aeou](?=[^aɛeiɨouyāīū]+[iīɛyj]))")
        forme_phono = re.sub(umlaut_en_i_interne, lambda cand: {"u": "y", "o": "ø", "e": "ɛ", "a": "ɛ",
                                                                "U": "Y", "O": "Ø", "E": "Ɛ", "A": "Ɛ"
                                                                }.get(cand.group()), forme_phono)

        # le reste change accordément
        forme_phono = re.sub("(?i:o[ui]|au|[ea]i|[iāīū])", lambda cand: {"i": "ɨ", "ī": "i", "ū": "i", "ā": "ɔ", "au": "ɔ",
                                                                         "ou": "ʉ", "oi": "ʉ",  "ai": "oɨ", "ei": "uɨ",
                                                                         "I": "Ɨ", "Ī": "I", "Ū": "I", "Ā": "Ɔ", "AU": "Ɔ",
                                                                         "OU": "Ʉ", "OI": "Ʉ", "AI": "OƗ", "EI": "UƗ"
                                                                         }.get(cand.group()), forme_phono)

        return forme_phono


class AjustementsTemporaires(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        forme_phono = re.sub("(?<=ꝁ)s", "", forme_phono)
        forme_phono = re.sub("[aAeEɛƐoOɨƗyY]?ꝁt", lambda cand: {"aꝁt": "aɨŧ", "Aꝁt": "AƗŧ",
                                                            "oꝁt": "oɨŧ", "Oꝁt": "OƗŧ",
                                                            "eꝁt": "eiŧ", "Eꝁt": "Eiŧ",
                                                            "ɛꝁt": "eiŧ", "Ɛꝁt": "Eiŧ",
                                                            "ɨꝁt": "iŧ", "Ɨꝁt": "Iŧ",
                                                            "yꝁt": "yiŧ", "Yꝁt": "YIŧ"
        }.get(cand.group(), "ŧ"), forme_phono)
        forme_phono = re.sub("(?=(?i:[^aeƐiɨoɔuʉyø]))g(?=n)", "ɨ", forme_phono)
        forme_phono = re.sub("[nms]$", "", forme_phono) # [mn] sans doute par nasalisation intermédiaire
        forme_phono = re.sub("(?i:((?<=[aeƐiɨoɔuʉūyø].)|(?<=[aeƐiɨoɔuʉūyø]..))[aeƐiɨoɔuʉūyø])$", "", forme_phono)
        forme_phono = re.sub("m[brl]|n[dp]|bb|ss$",
                             lambda cand: {"mb": "mm", "mr": "br", "ml": "bl", "nd": "nn", "np": "mp", "bb": "b", "ss": "s"
                              }.get(cand.group()), forme_phono)
        # forme_phono = re.sub("(?i:[aeiouāēīōū])$", lambda cand: cand.group() + "ħ", forme_phono)  # ?
        forme_phono = re.sub("j$", "đ", forme_phono)
        forme_phono = forme_phono.translate(str.maketrans("ꝑʷ", "fw"))
        return forme_phono


évolution = [
    Traitement_kw,
    Renforcement_w_Initial,
    Perte_f,
    Traitement_s_Initial,
    LénitionIntervocalique,
    TraitementGéminées,
    FricatisationAprèsLiquides,
    MutationsVocaliques,
    AjustementsTemporaires,
]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée

