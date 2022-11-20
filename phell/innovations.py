import re
from innovations import ChangementPhonétique, Centumisation


class AssourdissementAspirées(ChangementPhonétique):
    nom = "Assourdissement des consonnes aspirées"
    description = "Les consonnes sonores aspirées du proto-indo-européen s'assourdissent."
    sources = ["PHL"]
    motif = re.compile("[bdg]ʷ?ʰ")
    règle_remplacement = {"bʰ": "pʰ", "dʰ": "tʰ", "gʰ": "kʰ", "gʷʰ": "kʷʰ"}


# similaire à PGERM, mais j'avais jamais compris jusqu'ici
class LabialisationÉlongatrice_kw(ChangementPhonétique):
    nom = "Labialisation élongatrice du groupe kw"
    description = "Le groupe kw se transforme en la labio-vélaire kʷ, avec parfois élongation en -kkʷ."
    sources = ["PHL"]
    motif = re.compile("kw")
    règle_remplacement = "kkʷ"


class LoiDOsthoff(ChangementPhonétique):
    nom = "Loi d'Osthoff"
    description = "La loi d'Osthoff décrit le raccourcissement des voyelles précédant une consonne résonante dans" \
                  "une syllable longue."
    sources = ["PHL", "OL"]
    motif = re.compile("(?i:[āēīōū])(?=[rlmnwy](?i:[^aeiouāēīōū]))")
    règle_remplacement = {"ā": "a", "ē": "e", "ī": "i", "ō": "o", "ū": "u"}


class Débuccalisation_s_Intervocalique(ChangementPhonétique):
    nom = "Débuccalisation de s intervocalique et initial"
    description = "La consonne s intervocalique, ainsi qu'à l'initial devant voyelle se débuccalise graduellement " \
                  "vers h. Cet environnement vaut également pour les consonnes syllabiques."
    sources = ["PHL"]
    motif = re.compile("(?i:((?<=^)|(?<=[aeiouāēīōūḷṃṇṛ]))s(?=[aeiouāēīōūḷṃṇṛ]))")
    règle_remplacement = "h"


class Renforcement_y_Initial(ChangementPhonétique):
    nom = "Renforcement du y initiale en dy"
    description = "Le y initial indo-européen se renforce en dy, il suivra ensuite la palatalisation générale."
    sources = ["PHL"]
    motif = re.compile("^j")
    règle_remplacement = "dj"

# théoriquement devrait également prendre dʰy, mais dʰ n'existe plus apès assourdissement des aspirées
class PalatalisationDentalesDevant_y(ChangementPhonétique):
    nom = "Palatalisation des dentales devant y"
    description = "Première partie de la palatalisation des consonnes devant y : Les groupes ty et tʰy deviennent ts; " \
                  "le groupe dy devient dz."
    sources = ["PHL"]
    motif = re.compile("[dt]ʰ?j")
    règle_remplacement = {"dj": "dz", "tj": "ts", "tʰj": "ts"}


class AssimilationGroupesDentalesEt_s(ChangementPhonétique):
    nom = "Assimilation des groupes de dentale suivie de s"
    description = "Les groupes de dentale suivie de s hérités du proto-indo-européen, ds, ts et tʰs, fusionnent en ts."
    sources = ["PHL"]
    motif = re.compile("ds|tʰs")
    règle_remplacement = "ts"


# attention dilemme: gʷíh₃woh₂ > gʷyṓwō > ďṓwō > zô  vs.  gʷih₃wós > gʷīwos > bíos, p-ê wí empêche dipht ? mais dwóh₁ > dúwō alors wtf
class TraitementLaryngales(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        motif_épenthèse = re.compile("(?P<pre>^|.)(?P<lar>[hḥ][₀₁₂₃])(?P<post>.|$)")
        def règle_épenthèse(candidat):
            if candidat.group("lar")[0] == "ḥ":
                return candidat.group("pre") + "e" + "h" + candidat.group("lar")[1] + candidat.group("post")
            if not candidat.group("pre") or candidat.group("pre").lower() not in list("aeiouāēīūṛḷṃṇ"):  # [^C]H
                if candidat.group("post").lower() in list("aeiouāēīōū"):  # [^C]HV
                    return candidat.group()
                elif candidat.group("post").lower() in list("ḷṃṇṛ"):  # [^C]HR
                    ép = {"ḷ": "el", "ṃ": "em", "ṇ": "en", "ṛ": "er", "Ḷ": "El", "Ṃ": "Em", "Ṇ": "En", "Ṛ": "Er"}
                    return candidat.group("pre") + candidat.group("lar") + ép.get(candidat.group("post"))
                else:  # [^C]HC
                    return candidat.group("pre") + candidat.group("lar") + "e" + candidat.group("post")
            elif candidat.group("pre").lower() in list("iuṛḷṃṇ"):  # [Riu]H
                ép = {"i": "je", "u": "we", "ṛ": "re", "ḷ": "le", "ṃ": "me", "ṇ": "ne",
                      "I": "jE", "U": "wE", "Ṛ": "rE", "Ḷ": "lE", "Ṃ": "mE", "Ṇ": "nE"}
                if not candidat.group("post") or candidat.group("post").lower() in list("aeiouāēīōūṛḷṃṇ"):  # [Riu]H[VR$]
                    if candidat.group("pre").lower() in list("ṛḷṃṇ"):  # CRH[VR$]:
                        ép = {"ḷ": "al", "ṃ": "am", "ṇ": "an", "ṛ": "ar", "Ḷ": "Al", "Ṃ": "Am", "Ṇ": "An", "Ṛ": "Ar"}
                        return ép.get(candidat.group("pre")) + candidat.group("lar") + candidat.group("post")
                    else:  # VRH[VR$]
                        return candidat.group()
                else:  # [Riu]HC
                    return ép.get(candidat.group("pre")) + candidat.group("lar") + candidat.group("post")
            else:  # VH
                return candidat.group()
        forme_phono = re.sub(motif_épenthèse, règle_épenthèse, forme_phono)

        motif_coloration = re.compile("(?P<h2>(?<=h₂)[eE]|[eE](?=h₂))|(?P<h3>(?<=h₃)[eE]|[eE](?=h₃))")
        def règle_coloration(candidat):
            if candidat.group("h2"):
                return {"e": "a", "E": "A"}.get(candidat.group())
            elif candidat.group("h3"):
                return {"e": "o", "E": "O"}.get(candidat.group())
        forme_phono = re.sub(motif_coloration, règle_coloration, forme_phono)

        forme_phono = re.sub("H|h[₀₁₂₃]", "ʔ", forme_phono)
        # ^ transforme toutes les laryngales succintement en "laryngales résiduelles" à la mode PBALTSLAV

        motif_disparition = re.compile("(?P<lar>(?i:[aeiou])?ʔ)")
        règle_disparition = {"aʔ": "ā", "eʔ": "ē", "iʔ": "ī", "oʔ": "ō", "uʔ": "ū",
                             "Aʔ": "Ā", "Eʔ": "Ē", "Iʔ": "Ī", "Oʔ": "Ō", "Uʔ": "Ū",
                             "ʔ": ""}  # ˀ restants de par ex CRHV, ^HV
        forme_phono = re.sub(motif_disparition, lambda candidat: règle_disparition.get(candidat.group()), forme_phono)

        motif_hiatus = re.compile("(?i:[īū](?=[aeiouāēīōūḷṃṇṛ])|(?<=[aeiouāēīōū])[ḷṃṇṛ])")
        règle_hiatus = {"i": "ij", "I": "Ij", "u": "uw", "U": "Uw",
                        "ḷ": "l", "ṃ": "m", "ṇ": "n", "ṛ": "r"}
        forme_phono = re.sub(motif_hiatus, lambda candidat: règle_hiatus.get(candidat.group()), forme_phono)

        return forme_phono


# Selon Andrew Sihler
class PalatalisationDevant_y(ChangementPhonétique):
    nom = "Palatalisation devant y"
    description = "Deuxième partie de la palatalisation des consonnes devant y : Les groupes py et phy deviennent pť ; " \
                  "le groupe by n'a laissé aucune trace qui puisse permettre de définir son effet de palatalisaton ; " \
                  "les groupes tsy et dzy, dont le y est replacé par analogie après la première palatalisation des " \
                  "dentales deviennent respectivement ťť et ďď ; les groupes kʰy, kʷy et kʷʰy deviennent également ťť " \
                  "et les groupes gy et gʷy également ďď ; les groupes ly et ry deviennent respectivement ľľ et řř ; " \
                  "les groupes my et ny deviennent tous deux ňň ; le groupe sy se débuccalise en hy puis devient yy, " \
                  "auquel fusionne le groupe wy."
    sources = ["PHL"]
    motif = re.compile("[ptkbdglhws]ʷ?ʰ?j")
    règle_remplacement = {"pj": "pť", "pʰj": "pť", "bj": "bď",
                          "tsj": "ťť", "kj": "ťť", "kʷj": "ťť", "kʰj": "ťť", "kʷʰj": "ťť",
                          "dzj": "ďď", "gj": "ďď", "gʷj": "ďď",
                          "lj": "ľľ", "mj": "ňň", "nj": "ňň", "rj": "řř", "sj": "jj", "wj": "jj"}


class LoiDeGrassmann(ChangementPhonétique):
    nom = "Loi de Grassmann"
    description = "La loi de Grassmann, de dissimilation des aspirées, décrit la perte de l'aspiration d'une consonne " \
                  "lorsqu'une autre consonne aspirée suit dans le mot. Affecte également la consonne simple h qui " \
                  "disparaît."
    sources = ["PHL"]
    motif = re.compile("[hʰ](?=.+ʰ)")


### IMPORTÉ DEPUIS PGERM ###

class Dentalisation_m_Final(ChangementPhonétique):
    motif = re.compile("m$")
    règle_remplacement = "n"


class LoiDeCowgill(ChangementPhonétique):
    nom = "Loi de Cowgill"
    description = "La loi de Cowgill décrit l'élévation de la voyelle o en u entre une consonne labiale et une " \
                  "consonne résonante, dans quelque ordre qu'elles soient."
    sources = ["PHL", "CL"]
    motif = re.compile("((?<=[lmnrľňř])[oO](?=([mbp]|[gk]ʷ)))|((?<=[mbp])|(?<=[mbp]ʰ)|(?<=[gk]ʷ))[oO](?=[lmnrľňř])")
    règle_remplacement = {"o": "u"}



évolution = [
    Centumisation,
    AssourdissementAspirées,
    LabialisationÉlongatrice_kw,
    LoiDOsthoff,
    Débuccalisation_s_Intervocalique,
    Renforcement_y_Initial,
    PalatalisationDentalesDevant_y,
    AssimilationGroupesDentalesEt_s,
    TraitementLaryngales,
    PalatalisationDevant_y,
    LoiDeGrassmann,
    # perte consonnes occlusives fincales ici
    Dentalisation_m_Final,
    LoiDeCowgill,
]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée
