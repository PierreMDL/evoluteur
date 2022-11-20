from innovations import ChangementPhonétique, DéplacementAccent, Centumisation
import re


# pas de loi d'Eichner
class MutationLaryngales(ChangementPhonétique):
    motif = re.compile("(?P<avant>^|.)(?P<laryngale>[hḥ][₀₁₂₃])(?P<apres>.|$)")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes["laryngale"][0] == "ḥ":
            return dict_de_groupes.group("avant") + "a" + dict_de_groupes.group("apres")
        if dict_de_groupes["avant"] == "" or dict_de_groupes["avant"] not in list("aeiouAEIOUēōĒŌ"):
            if dict_de_groupes["apres"] in list("aeiouAEIOUēōêôĒŌÊÔ"):
                if dict_de_groupes["laryngale"] == "h₃" and dict_de_groupes["apres"] in list("eE"):
                    return dict_de_groupes["avant"] + ("o" if dict_de_groupes["apres"].islower() else "O")
                elif dict_de_groupes["laryngale"] == "h₂" and dict_de_groupes["apres"] in list("eE"):
                    return dict_de_groupes["avant"] + ("a" if dict_de_groupes["apres"].islower() else "A")
                else:
                    return dict_de_groupes["avant"] + dict_de_groupes["apres"]
            else:
                if dict_de_groupes["avant"] == "":
                    return dict_de_groupes["apres"]
                else:
                    return dict_de_groupes["avant"] + "ə" + dict_de_groupes["apres"]
        elif dict_de_groupes["avant"] in list("aeiouAEIOUēōĒŌ"):
            if dict_de_groupes["apres"] == "" or dict_de_groupes["apres"] not in list("aeiouAEIOUēōêôĒŌÊÔ"):
                if dict_de_groupes["laryngale"] == "h₃" and dict_de_groupes["avant"] in list("eE"):
                    return ("ō" if dict_de_groupes["avant"].islower() else "Ō") + dict_de_groupes["apres"]
                elif dict_de_groupes["laryngale"] == "h₂" and dict_de_groupes["avant"] in list("eE"):
                    return ("ā" if dict_de_groupes["avant"].islower() else "Ā") + dict_de_groupes["apres"]
                else:
                    return   {"a": "ā", "e": "ē", "i": "ī", "o": "ō", "u": "ū",
                              "A": "Ā", "E": "Ē", "I": "Ī", "O": "Ō", "U": "Ū",
                              "ē": "ê", "ō": "ô", "Ē": "Ê", "Ō": "Ô"}.get(dict_de_groupes["avant"]) + dict_de_groupes["apres"]
            elif dict_de_groupes["apres"] in list("aeiouAEIOUēōêôĒŌÊÔ"):
                if dict_de_groupes["laryngale"] == "h₃" and dict_de_groupes["avant"] in list("eE"):
                    return dict_de_groupes["avant"] + "ô" if dict_de_groupes["apres"].islower() else "Ô"
                elif dict_de_groupes["laryngale"] == "h₂" and dict_de_groupes["avant"] in list("eE"):
                    return dict_de_groupes["avant"] + "â" if dict_de_groupes["apres"].islower() else "Â"
                else:
                    return {"e": "ê", "o": "ô", "u": "û", "E": "Ê", "O": "Ô", "U": "Û"
                            }.get(dict_de_groupes["avant"].upper() if dict_de_groupes["apres"].isupper() else dict_de_groupes["avant"])


class Perte_y_Intervocalique(ChangementPhonétique):
    motif = re.compile("(?i:(?P<avant>[ȧeiuēīọūêộảįųĩòȍ])j(?P<apres>[ȧeiuēīọūêộảįųĩòȍ]))")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes["avant"][0].lower() != dict_de_groupes["apres"][0]: # hiatus
            return dict_de_groupes["avant"] + dict_de_groupes["apres"] # = dipthongue
        else:
            return {"ȧ": "ạ", "Ȧ": "Ạ", "e": "ē", "E": "Ē", "u": "ū", "U": "Ū"}.get(dict_de_groupes["avant"])
            # ^ laisser le dict min / maj sauf si on sait ce qu'on fait


class DéplacementAccent(DéplacementAccent):
    motif = re.compile("[əaeiouāēīōūêôû]")

###



# Il faut apparemment faire la différence entre schwa de laryngales qui devient a et schwa d'épenthèse qui fait e...
class Traitement_schwa_DeLaryngales(ChangementPhonétique):
    motif = re.compile("[əƏ]")
    règle_remplacement = {"ə": "a"}


class Assimilation_p_En_kw(ChangementPhonétique):
    motif = re.compile("p(?=.+kʷ)")
    règle_remplacement = "kʷ"


# Comme en PGERM mais aussi avant voyelles (d'où newos => nowos)
class Recul_ew(ChangementPhonétique):
    motif = re.compile("[eEēĒ]w")
    règle_remplacement = {"ew": "ow", "Ew": "Ow", "ēw": "ow", "Ēw": "Ow"}


class PerteLabialesDevantConsonnes(ChangementPhonétique):
    motif = re.compile("ʷ(?=ʰ?(?i:[^ʰaeiouāēīōūḷṃṇṛ]))")


class FricatisationSpirantes(ChangementPhonétique):
    motif = re.compile("(^|.)([bdg]ʷ?ʰ)")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes.group(1) == "":
            rempl = {"bʰ": "ꝑ", "dʰ": "ŧ", "gʰ": "ꝁ", "gʷʰ": "ꝁʷ"}.get(dict_de_groupes.group(2))
        else:
            rempl = {"bʰ": "ƀ", "dʰ": "đ", "gʰ": "ǥ", "gʷʰ": "ǥʷ"}.get(dict_de_groupes.group(2))
        return (dict_de_groupes.group(1) or "") + rempl


class Vocalisation_s_Médial(ChangementPhonétique):
    motif = re.compile("(?<!^)s(?!$)")
    règle_remplacement = "z"


class AssourdissementObstruantesDevantSourdes(ChangementPhonétique):
    motif = re.compile("[bdgƀđǥz](?=[stpk])")
    règle_remplacement = {"b": "p", "d": "t", "g": "k",
                          "ƀ": "ꝑ", "đ": "ŧ", "ǥ": "ꝁ",
                          "z": "s"}


class Traitement_sr_zr(ChangementPhonétique):
    motif = re.compile("[sz](?=r)")
    règle_remplacement = {"s": "ŧ", "z": "đ"}


# ATTENTION: wiki dit vers f, mais ꝑ dans tableau phono, donc...
class SimplificationFricatives(ChangementPhonétique):
    motif = re.compile("ŧ|ꝁʷ")
    règle_remplacement = "ꝑ"


class Relocation_tl(ChangementPhonétique):
    motif = re.compile("tl")
    règle_remplacement = "kl"


# "resonant + laryngeal, when before a consonant", mais j'ai rien trouvé comme ça : [ḷṃṇṛ]h[₁₂₃][aeiouāēō]...
# si épenthèse après perte laryngales, ə est peut-être déjà a, d'où a ici:
# ne tient pas compte du fait qu'il peut potentiellement y avoir des schwa accentués, très rares mais bon
class Épenthèse(ChangementPhonétique):
    motif = re.compile("[ḷṃṇṛḶṂṆṚ]a?")
    règle_remplacement = {"ḷ": "ol", "ṃ": "əm", "ṇ": "ən", "ṛ": "or",
                          "Ḷ": "Ol", "Ṃ": "Əm", "Ṇ": "Ən", "Ṛ": "Or",
                          "ḷa": "lā", "ṃa": "mā", "ṇa": "nā", "ṛa": "rā",
                          "Ḷa": "lĀ", "Ṃa": "mĀ", "Ṇa": "nĀ", "Ṛa": "rĀ"}


# DÉSACTIVÉ : tout concorde à dire que c'est de la merde : moldus > mollis, h₁nómn̥ > nomen, tl̥néh₂ti > tollet...
class Élévation_a_DevantLabialesEt_l_PITAL(ChangementPhonétique):
    motif = re.compile("[oOōŌ](?=[lmbpꝑ])")
    règle_remplacement = {"o": "a", "ō": "ā"}




class AnalyseEnDiphtongues(ChangementPhonétique):
    motif = re.compile("(?i:[aeoāēō])[wj](?!(?i:[aeiouāēīōūə]))")
    règle_remplacement = {"aw": "au", "ow": "ou", "ōw": "ō",
                          "Aw": "AU", "Ow": "OU", "Ōw": "ō",
                          "aj": "ai", "oj": "oi", "ej": "ei",
                          "Aj": "AI", "Oj": "OI", "Ej": "EI",
                          "āj": "ai", "ōj": "ōi", "ēj": "ei",
                          "Āj": "AI", "Ōj": "ŌI", "Ēj": "EI"}


évolution = [
    Centumisation,
    MutationLaryngales,  # attention, incomplet, PITAL a qqs cas particuliers
    Traitement_schwa_DeLaryngales,
    Perte_y_Intervocalique,  # bizarre mais oui
    Recul_ew,  # et ça aussi oui
    Assimilation_p_En_kw,
    PerteLabialesDevantConsonnes,
    FricatisationSpirantes,
    Vocalisation_s_Médial,
    AssourdissementObstruantesDevantSourdes,  # placée ici plutôt qu'avant fricati: ghosteyes => hoztēs => hostēs
    Traitement_sr_zr,
    SimplificationFricatives,
    Relocation_tl,
    Épenthèse,
    # Élévation_a_DevantLabialesEt_l_PITAL,  # absolument pas probant !
    DéplacementAccent,
    AnalyseEnDiphtongues
]



def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée

