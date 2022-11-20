from innovations import ChangementPhonétique
import re


class AjustementsTemporaires1(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        forme_phono = re.sub("[ảȧ]$", "", forme_phono)  # [aą]$ déjà notés disparu en OGERM mais prob avec VANGL donc bon, ici
        return forme_phono


class OcclusionFricativesSonores(ChangementPhonétique):
    nom = "Occlusion des fricatives sonores"
    description = "Les deux fricatives sonores restantes de la première mutation consonnantique gagne une " \
                       "occlusion : ƀ devient b, ǥ devient g."
    sources = ["OHG", "HGCS"]
    chronologie = "7ème / 8ème siècles"
    motif = re.compile("[ƀǥ]")
    règle_remplacement = {"ƀ": "b", "ǥ": "g"}


class MutationConsonnantiquePartie1(ChangementPhonétique):
    nom = "Mutation consonnantique, partie 1"
    description = "Première partie de la mutation consonnantique du vieux haut allemand concernant les consonnes " \
                     "p, t et k non-géminées, post-vocaliques, qui deviennent en fin de mot ou devant consonnes " \
                     "les fricatives f, ȥ et x, et se doublent entre voyelles."
    chronologie = "4ème / 5ème siècles"
    sources = ["OHG", "HGCS"]
    motif = re.compile("(?<=(?i:[ȧeiouạēẹīōū]))((?<!p)p(?!p)|(?<!t)t(?![tr])|(?<!k)k(?!k))(?=(?P<apres>.|$))")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes["apres"] in list("ȧeiou"):
            return {"p": "ff", "t": "ȥȥ", "k": "xx"}.get(dict_de_groupes.group())
        else:
            return {"p": "f", "t": "ȥ", "k": "x"}.get(dict_de_groupes.group())


class MutationConsonnantiquePartie2(ChangementPhonétique):
    nom = "Mutation consonnantique, partie 2"
    description = "Deuxième partie de la mutation consonnantique du vieux haut allemand concernant les consonnes " \
                     "p, t et k initiales, post-résonantes ou géminées qui deviennent les affriquées pf, tȥ et kx " \
                     "(cette dernière évolution étant limitée à certains dialectes allemands supérieurs)."
    sources = ["OHG", "HGCS"]
    chronologie = "5ème / 6ème siècles pour t > tȥ, 6ème / 7ème siècles pour p > pf, 7ème / 8ème siècles pour k > kx"

    motif = re.compile("^[pt](?!r)|(?<=[lrmn])[pt]|pp|tt") # rajouter k pour dialectes all sup
    règle_remplacement = {"p": "pf", "t": "tȥ", "k": "kx", "pp": "pf", "tt": "tȥ", "kk": "kx"}


class MutationConsonnantiquePartie3(ChangementPhonétique):
    nom = "Mutation consonantique, partie 3"
    description = "Troisième partie de la mutation consonnantique du vieux haut allemand concernant les consonnes " \
                       "b, d et g qui perdent leur sonorité et deviennent p, t, k. En allemand standard, seuls les" \
                       "d et g géminés subissent cette évolution."
    sources = ["OHG", "HGCS"]
    chronologie = "8ème / 9ème siècles"

    motif = re.compile("d|dd|gg") # simplifier géminées, modifier tableau ci-dessous pour dialectes suisses et autrichiens
    règle_remplacement = {"bb": "pp", "d": "t", "gg": "kk"}


class MutationFricativeDentale(ChangementPhonétique):
    nom = "Mutation de la fricative dentale"
    description = "La fricative dentale ŧ devient occlusive et sonore et devient d."
    sources = ["OHG", "HGCS"]
    chronologie = "9ème / 10ème siècles"

    motif = re.compile("ŧ")
    règle_remplacement = "d"


# ATTENTION : Il s'agit de ē2 du proto-germanique ! Pas ē1 qui vient par exemple de ai non-accentué (NO) !
# TODO : ne mute probablement que les diphtongues accentuées !! Vérifier ça asap
class Dipthongaisons(ChangementPhonétique):
    nom = "Diphtongaisons"
    description = "Les diphtongues ē et ō deviennent les diphtongues ie et uo."
    sources = ["OHG"]

    motif = re.compile("[ēĒōŌ]")
    règle_remplacement = {"ē": "e", "Ē": "IE", "ō": "a", "Ō": "UO"}  # corrigé pour faire apparaître innacentué en courtes


# ATTENTION : Monophtongaison en ê et ô selon wiki, pas ē et ō, également au > ô devant toutes dentales, n = dentale ?
class MutationsOuMonophtongaisons(ChangementPhonétique):
    nom = "Mutations ou monophtongaisons"
    description = "Les dipthongues ai et au subissent une monophtongaison respectivement vers ē devant h, r, w " \
                       "ou en fin de mot, vers ō devant h, r ou une dentale, ou bien une mutation respectivement " \
                       "vers ei et au dans les autres cas."
    sources = ["OHG"]
    motif = re.compile("(ȧi|ȧu|ȦI|ȦU)(?=(?P<apres>.|$))")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes.group() in ["ȧi", "ȦI"]:
            if dict_de_groupes["apres"] == "" or dict_de_groupes["apres"] in "hrw":
                return {"ȧi": "ē", "ȦI": "Ē"}.get(dict_de_groupes.group())
            else:
                return {"ȧi": "ei", "ȦI": "EI"}.get(dict_de_groupes.group())
        elif dict_de_groupes.group() in ["ȧu", "ȦU"]:
            if dict_de_groupes["apres"] == "" or dict_de_groupes["apres"] not in "hrdtn":  # ATTENTION : n pas sûr ! (dentale ?), et s? (lausaz => lōs=
                return {"ȧu": "ou", "ȦU": "OU"}.get(dict_de_groupes.group())
            else:
                return {"ȧu": "ō", "ȦU": "Ō"}.get(dict_de_groupes.group())




# ATTENTION : iu également devant une labiale ou une vélaire dans les dialectes de l'allemand supérieur
# Ça ressemble à l'harmonisation eu > jó / jú du vieux norrois
class Élévation_eu(ChangementPhonétique):
    nom = "Mutation de eu"
    description = "La diphtongue eu subit une mutation vocalique vers iu par l'effet d'une voyelle haute (i ou u) dans" \
                  " la syllabe suivante, ou dans le cas contraire vers eo puis io."
    sources = ["OHG"]
    motif = re.compile("(eu|EU)(?=[^ȧeiouạēẹīōū]+(?P<ui>[ui])?)")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if not dict_de_groupes.group() == "":
            return {"eu": "io", "EU": "IO"}.get(dict_de_groupes.group())
        else:
            return {"eu": "iu", "EU": "IU"}.get(dict_de_groupes.group())




# Mon initiative, fehu > fihu, sebun > sibun, meluk > miluk indique un effet d'umlaut régulier
# comme en gothique ?
class Élévation_e_Devant_u(ChangementPhonétique):
    motif = re.compile("[eE](?=(?![iI]).+u)")
    règle_remplacement = {"e": "i", "E": "I"}


class MutationEn_i(ChangementPhonétique):
    motif = re.compile("[ȧȦ](?![iIuU]|ꝁ[ꝁts]|xx|[^ȧeiouạēẹīōū]w|[lr][^ȧeijouạēẹīōū])(?=.+[ij])")
    règle_remplacement = {"ȧ": "e", "Ȧ": "E"}


class Perte_h_w_InitiauxDevantConsonne(ChangementPhonétique):
    nom = "Perte de w et h devant une consonne"
    description = "Les consonnes h et w disparaissent devant une autre consonne."
    sources = ["OHG"]
    motif = re.compile("^[ꝁw](?=(?i:[^ȧeiouạēẹīōū]))")


# Pas représenté à l'écrit
class Chuintisation_s(ChangementPhonétique):
    nom = "Chuintisation du s"
    description = "Le s devient la chuintante ʃ à l'initiale devant consonne, et le groupe sk en toute position."
    sources = ["HGCS"]
    motif = re.compile("sk|(?<=r)s|^s(?=[tplmn])")
    règle_remplacement = "ʃ"


class AssourdissementFinal(ChangementPhonétique):
    nom = "Assourdissement final"
    description = "Les consonnes finales s'assourdissent."
    sources = ["HGCS"]
    motif = re.compile("[bdg]$")
    règle_remplacement = {"b": "p", "d": "t", "g": "k"}


class AjustementsTemporaires2(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        forme_phono = forme_phono.translate(str.maketrans("ȧạȦẠꝑƀ", "aāAĀff"))  # ces sons-là n'existent plus en vha
        return forme_phono


évolution = [
    AjustementsTemporaires1,
    OcclusionFricativesSonores,
    MutationConsonnantiquePartie1,
    MutationConsonnantiquePartie2,
    MutationConsonnantiquePartie3,
    MutationFricativeDentale,
    Dipthongaisons,
    MutationsOuMonophtongaisons,
    Élévation_eu,
    Élévation_e_Devant_u, # mon initiative : sebun > sibun, etc.
    MutationEn_i,
    Perte_h_w_InitiauxDevantConsonne, # wrōgijaną => ruogen, mais hlahjaną => hlahhan !
    Chuintisation_s,
    AssourdissementFinal,
    AjustementsTemporaires2
]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée
