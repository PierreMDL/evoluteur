from innovations import  ChangementPhonétique, DéplacementAccent, Centumisation
import re


### IMPORTÉ DEPUIS PGERM ###
# ajouté m, n aussi
class LoiDeDybo(ChangementPhonétique):
    nom = "Loi de Dybo"
    description = "Une voyelle longue atone est raccourcie lorsqu'elle est suivie de l ou r puis de la syllabe" \
                       "accentuée. Effectif en proto-germanique, proto-italic, proto-balto-slave et proto-celtique."
    sources = ["DG"]
    motif = re.compile("[āēīōū](?=[mnlr][^aeiouāēīōūêôûə]*[AEIOUĀĒĪŌŪÊÔÛƏ])")
    règle_remplacement = {"ā": "a", "ē": "e", "ī": "i", "ō": "o", "ū": "u"}


###

### IMPORTÉ DEPUIS PITAL ###

class Assimilation_p_En_kw(ChangementPhonétique):
    motif = re.compile("p(?=.+kʷ)")
    règle_remplacement = "kʷ"

###


class MutationLaryngales_Partie1(ChangementPhonétique):
    @classmethod
    def appliquer(self, forme_phono: str, info=None) -> str:

        # Ceci me semble douteux : ǵr̥h₂nóm, pl̥h₂méh₂, pl̥h₁nós donnent des a courts...
        # motif_épenthèse = re.compile("(?i:[ḷṃṇṛ]h[₀₁₂₃](?=[lmnr]))")
        # def règle_épenthèse(candidat):
        #     return {"ḷ": "la", "ṃ": "ma", "ṇ": "na", "ṛ": "ra",
        #             "Ḷ": "lA", "Ṃ": "mA", "Ṇ": "nA", "Ṛ": "rA"}.get(candidat.group()[0]) + candidat.group()[1:]
        # forme_phono = re.sub(motif_épenthèse, règle_épenthèse, forme_phono)

        motif_coloration = re.compile("(?P<h2>(?<=h₂)[eE]|[eE](?=h₂))|(?P<h3>(?<=h₃)[eE]|[eE](?=h₃))")
        def règle_coloration(candidat):
            if candidat.group("h2"):
                return {"e": "a", "E": "A"}.get(candidat.group())
            elif candidat.group("h3"):
                return {"e": "o", "E": "O"}.get(candidat.group())
        forme_phono = re.sub(motif_coloration, règle_coloration, forme_phono)

        motif_disparition = re.compile(""  # à l'initiale
                                       "(?i:(?<=^)[hḥ][₀₁₂₃](?![ḷṃṇṛ]))"  
                                       "|"  # devant une voyelle, sauf si également derrière une voyelle
                                       "(?i:(?<![aeiouāēīōū])[hḥ][₀₁₂₃](?=[aeiouāēīōū]))"
                                       "|"  # derrière une voyelle dans la syllabe prétonique
                                       "(?<=[aeiouāēīōū])[hḥ][₀₁₂₃](?=[^aeiouāēīōū]+[AEIOUĀĒĪŌŪḶṂṆṚḤ])"  
                                       "|"  # Entre deux plosives, mais pas en syllabe initiale
                                       "((?<=[aeiouāēīōūḷṃṇṛ][ptkbdgʷʰ])|(?<=[aeiouāēīōūḷṃṇṛ].[ptkbdgʷʰ])|(?<=[aeiouāēīōūḷṃṇṛ]..[ptkbdgʷʰ]))[hḥ][₀₁₂₃](?=[ptkbdg])",
                                       re.X)
        forme_phono = re.sub(motif_disparition, "", forme_phono)

        motif_allongement = re.compile("(?i:[aeiou])[hḥHḤ][₀₁₂₃]")
        def règle_allongement(candidat):
            return {"a": "ā", "e": "ē", "i": "ī", "o": "ō", "u": "ū",
                    "A": "Ā", "E": "Ē", "I": "Ī", "O": "Ō", "U": "Ū"}.get(candidat.group()[0])
        forme_phono = re.sub(motif_allongement, règle_allongement, forme_phono)
        return forme_phono


class DéplacementAccent(DéplacementAccent):
    motif = re.compile("[aeiouāēīōūḷṃṇṛ]")


class VocalisationLaryngales(ChangementPhonétique):
    motif = re.compile("(?i:(?<![^aeiouāēīōūḷṃṇṛ][lmnr])([hḥ][₀₁₂₃])(?=j[aeiouāēīōū]))")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        return "ī" if dict_de_groupes.group()[0].islower() else "Ī"


class MutationLaryngales_Partie2(ChangementPhonétique):
    motif = re.compile("(?i:(?<=[^aeiouāēīōūḷṃṇṛ])[hḥ][₀₁₂₃](?=[^aeiouāēīōūḷṃṇṛ]|$))")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        return "a" if dict_de_groupes.group()[0].islower() else "A"


class TraitementDeuxDentales(ChangementPhonétique):
    motif = re.compile("(t|dʰ?){2}")
    règle_remplacement = "ss"


class Traitement_m_DevantSemiconsonnes(ChangementPhonétique):
    motif = re.compile("m[jw]")
    règle_remplacement = {"mj": "nj", "mw": "w"}

class Assimilation_w_DerrièreVélaires(ChangementPhonétique):
    motif = re.compile("[gk]ʰ?w")
    règle_remplacement = {"gw": "gʷ", "gʰw": "gʷʰ", "kw": "kʷ"}

class Traitement_gw_Initial(ChangementPhonétique):
    motif = re.compile("gʷ(?!ʰ)")
    règle_remplacement = "b"


class PerteAspiration(ChangementPhonétique):
    motif = re.compile("ʰ")


class Épenthèse_Partie1(ChangementPhonétique):
    motif = re.compile("(?i:[ḷṃṇṛ])(?=[bdg]ʷ?(?<!ʰ))")
    règle_remplacement = {"ḷ": "la", "ṃ": "ma", "ṇ": "na", "ṛ": "ra",
                          "Ḷ": "lA", "Ṃ": "mA", "Ṇ": "nA", "Ṛ": "rA"}

class ÉpenthèsePartie2(ChangementPhonétique):
    @classmethod
    def appliquer(cls, forme_phono: str) -> str:
        motif_initial = re.compile("(?i:^[hḥ][₀₁₂₃][ḷṃṇṛ](?=[^aeiouāēīōūḷṃṇṛ]))")
        def règle_initial(groupe_de_dict):
            return {"ḷ": "al", "ṃ": "am", "ṇ": "an", "ṛ": "ar",
                    "Ḷ": "Al", "Ṃ": "Am", "Ṇ": "An", "Ṛ": "Ar"}.get(groupe_de_dict.group()[-1])
        forme_phono = re.sub(motif_initial, règle_initial, forme_phono)

        motif_occlusive_sourde = re.compile("(?i:(?<=[^aeiouāēīōūḷṃṇṛ])[ḷṃṇṛ][hḥ][₀₁₂₃](?=[ptk]))")
        def règle_occlusive_sourde(groupe_de_dict):
            return {"ḷ": "la", "ṃ": "ma", "ṇ": "na", "ṛ": "ra",
                    "Ḷ": "lA", "Ṃ": "mA", "Ṇ": "nA", "Ṛ": "rA"}.get(groupe_de_dict.group()[0])
        forme_phono = re.sub(motif_occlusive_sourde, règle_occlusive_sourde, forme_phono)

        motif_restant = re.compile("(?i:(?<=[^aeiouāēīōūḷṃṇṛ])[ḷṃṇṛ][hḥ][₀₁₂₃](?=(?P<apres>.)))")
        def règle_restant(groupe_de_dict):
            if groupe_de_dict.group("apres").lower() not in list("aeiouāēīōūḷṃṇṛ"):
                return {"ḷ": "lā", "ṃ": "mā", "ṇ": "nā", "ṛ": "rā",
                        "Ḷ": "lĀ", "Ṃ": "mĀ", "Ṇ": "nĀ", "Ṛ": "rĀ"}.get(groupe_de_dict.group()[0])
            else:
                return {"ḷ": "al", "ṃ": "am", "ṇ": "an", "ṛ": "ar",
                        "Ḷ": "Al", "Ṃ": "Am", "Ṇ": "An", "Ṛ": "Ar"}.get(groupe_de_dict.group()[0])
        forme_phono = re.sub(motif_restant, règle_restant, forme_phono)

        return forme_phono


class Coloration_e_AprèsRésonanteEt_a(ChangementPhonétique):
    motif = re.compile("[eE](?=[lmnr]a)")
    règle_remplacement = {"e": "a"}


class ÉpenthèsePartie3(ChangementPhonétique):
    motif = re.compile("(?i:[ḷṃṇṛ])(?=(?P<plosive>[ptkbdg]?))")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes.group("plosive"):
            return {"ḷ": "li", "ṃ": "am", "ṇ": "an", "ṛ": "ri",
                    "Ḷ": "lI", "Ṃ": "Am", "Ṇ": "An", "Ṛ": "rI"}.get(dict_de_groupes.group())
        else:
            return {"ḷ": "al", "ṃ": "am", "ṇ": "an", "ṛ": "ar",
                    "Ḷ": "Al", "Ṃ": "Am", "Ṇ": "An", "Ṛ": "Ar"}.get(dict_de_groupes.group())


class Élévation_e_o_longs(ChangementPhonétique):
    motif = re.compile("(?i:[ē]|[ō](?=[^aeiouāēīōū]*$))")
    règle_remplacement = {"ē": "ī", "ō": "ū"}


class TraitementDeuxPlosives(ChangementPhonétique):
    motif = re.compile("(?P<plosive>[bdgptk]ʷ?ʰ?)(?!(?P=plosive))(?=[bdgptks])")
    règle_remplacement = "ꝁ"

class Disparition_p(ChangementPhonétique):
    motif = re.compile("p(?=(?P<apres>.))")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if not dict_de_groupes.group("apres") or dict_de_groupes.group("apres") not in list("mnr"):
            return "ꝑ"
        elif dict_de_groupes.group("apres") in list("r"):
            return "b"
        elif dict_de_groupes.group("apres") in list("mn"):
            return "w"

class Abaissement_o_long(ChangementPhonétique):
    motif = re.compile("[ōŌ]")
    règle_remplacement = {"ō": "ā"}

class Assimilation_ew_uwa(ChangementPhonétique):
    motif = re.compile("[eE](?=w)|[uU](?=w[aA])")
    règle_remplacement = {"e": "o", "u": "o"}

class AjustementsTemporaores_PCELT(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        forme_phono = forme_phono.replace("mt", "nt")
        return forme_phono


évolution = [
    # LATE PIE
    Centumisation,
    TraitementDeuxDentales,
    MutationLaryngales_Partie1,

    # ITALO-CELT
    LoiDeDybo,
    DéplacementAccent,
    VocalisationLaryngales,
    MutationLaryngales_Partie2,
    Épenthèse_Partie1,
    Traitement_m_DevantSemiconsonnes,
    Assimilation_p_En_kw,
    ÉpenthèsePartie2,

    # EARLY PCELT
    Assimilation_w_DerrièreVélaires,
    Traitement_gw_Initial,
    PerteAspiration,
    Coloration_e_AprèsRésonanteEt_a,
    ÉpenthèsePartie3,
    Élévation_e_o_longs,

    # LATE PCELT
    TraitementDeuxPlosives,
    Disparition_p,
    Abaissement_o_long,
    Assimilation_ew_uwa,
]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée

