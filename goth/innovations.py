import re
from innovations import ChangementPhonétique


### INITIALEMENT DEPUIS VISL ###
class Renforcement_ww_jj(ChangementPhonétique):
    nom = "Renforcement des groupes ww et jj"
    description = "Les groupes de semi-consonnes ww et jj se renforcent en respectivement ggw et ggj. Cela " \
                       "doit arriver précocement car l'innovation se trouve en vieux norrois et (différemment) " \
                       "en gothique, pourtant censés ne pas appartenir au même groupement. Sans doute un " \
                       "argument pour la théorie du continuum dialectal."
    sources = ["NWG"]

    motif = re.compile("ww|jj")
    règle_remplacement = {"ww": "ggw", "jj": "ggj"} # je laisse les occlusives par analogie avec gémination
###


class AjustementsTemporaires1(ChangementPhonétique):
    nom = "Ajustements temporaires du gothique"
    description = "Ajustements temporaires : ǥ initial devient occlusif, ꝁ se glottalise en ħ."
    motif = re.compile("^ǥ|ꝁ")
    règle_remplacement = {"ǥ": "g", "ꝁ": "ħ"}


# Initiative perso
class SyncopeVocaleAtoneThématique(ChangementPhonétique):
    nom = "Syncope vocal atone thématique"
    description = "Les voyelles thématiques courtes ɑ, i, u et leurs équivalents nasaux disparaissent, sauf u avant " \
                  "la marque désinentielle -z."
    motif = re.compile("(i?j?(ả|ȧz)|[iuįų]|iz)$")
    règle_remplacement = {"į": "", "ų": "", "ả": "",
                          "i": "", "u": "", "ȧ": "",
                          "ȧz": "z", "iz": "z",
                          "jȧz": "jiz", "jả": "i",
                          "ijȧz": "īz", "ijả": "i"}


# Initiative perso: wō > wō
class RéductionVocaleAtoneFinale(ChangementPhonétique):
    motif = re.compile("(ȧi$|(?<!w)[êīọộòȍ])$")
    règle_remplacement = {"ả": "", "į": "", "ų": "",
                          "ȧi": "ȧ",
                          "ê": "ē",
                          "ī": "i",
                          "ọ": "ȧ", "ộ": "ọ", "ò": "ȧ", "ȍ": "ọ"}


class DisparitionNasalisation(ChangementPhonétique):
    nom = "Disparition de la nasalisation"
    description = "Les voyelles nasales nasales longues deviennent orales."
    sources = ["GL"]
    motif = re.compile("[àòĩũÀÒĨŨ]")
    règle_remplacement = {"à": "ạ", "ò": "ọ", "ĩ": "ī", "ũ": "ū"}


# ATTENTION : Pas éclairci, p-ê similaire mais pas relié au processus du vieux norrois
class Renforcement_ggj(ChangementPhonétique):
    nom = "Renforcement du groupe ggj"
    description = "Partie spécifiquement gothique de la loi de Holtzmann : le groupe -ggj- nouvellement " \
                  "renforcé depuis le groupe de semi-consonnes -jj- devient dental. Peut-être est-ce que " \
                  "l'étape -ggj- n'a jamais eu lieu en gothique."
    sources = ["IGTU", "HL"]
    motif = re.compile("ggj")
    règle_remplacement = "ddj"


class PlosivationSonoresDerrièreConsonne(ChangementPhonétique):
    nom = "Plosivation des fricatives sonores derrière une consonne"
    description = "Les fricatives sonores ƀ, đ, ǥ deviennent occlusives derrière toutes consonnes, et à l'initiale " \
                  "dans le cas de ǥ, dernière fricative sonore à cette position jusqu'ici."
    sources = ["GL"]
    motif = re.compile("(?<=(?i:[^ȧeėiouạēẹīọū]))[ƀđǥ]")
    règle_remplacement = {"ƀ": "b", "đ": "d", "ǥ": "g"}


# Anciennement sigmatisation, attention aux exceptions :
# n ? fraluznaną > fralusnan ! mais garaznô > garazna
# intervocalique ?? hauzīniz > hauseins wtf, hauzijaną > hausjan, laizō > laisō après diphtongues ?
# marzijaną > marzjan
# WHAT mimzą > mimz !! maiþmaz > maiþms, malmaz > malmas, je comprends plus rien
# avant j:
# habjaną > hafjan est selon wikt le seul à s'assourdir de toutes les [bdg]j
# nazjaną > nasjan, wazjaną > wasjan mais hazjaną > hazjan
class AssourdissementFinalOuDevantConsonnesSourdes(ChangementPhonétique):
    motif = re.compile("[ƀđǥz](?=[ptkzsꝑŧꝁ]|$)")  # ajout du z dans groupe suivant pour choper les zz > ss
    règle_remplacement = {"ƀ": "ꝑ", "đ": "ŧ", "ǥ": "ꝁ", "z": "s"}


class Mutation_fl_En_thl(ChangementPhonétique):
    nom = "Mutation du groupe fl en þl"
    description = "Le groupe fl subit une mutation vers þl mais apparemment seulement dans l'environnement " \
                  "de h, hs ou kw."
    sources = ["IGTU"]
    motif = re.compile("^ꝑl(?=(?i:ȧi|ȧu|eu|ọu|[ȧeėiouạēẹīọū])(ħ|kw))")
    règle_remplacement = "ŧl"


# cette élévation a dû se produire avant la monophtongaison de ai et au, sinon le produit de cette monophtongaison se
# mêle à celle de l'élévation et produit par exemple PG augô > **ōgō
class Élévation_e_o_LongsMiouverts(ChangementPhonétique):
    nom = "Élévation de ɛ̄ et ɔ̄"
    description = "Les voyelles longues ɛ̄ et ɔ̄ s'élèvent en respectivement ē et ō sauf devant une voyelle."
    sources = ["GL"]
    motif = re.compile("[ẹọẸỌ](?![ȧạėẹeēiīȯọoōuū])")
    règle_remplacement = {'ẹ': 'ē', 'ọ': 'ō'}


class Abaissement_e_i_u_Devant_r_h_hw(ChangementPhonétique):
    nom = "Umlaut par r, h, hw"
    description = "Les voyelles courtes e, i et u s'abaissent en respectivement ɛ, ɛ et ɔ devant un r ou un h(w)."
    sources = ["GL"]
    motif = re.compile("(?i:e|(?<![ie])u|(?<!ȧ)i)(?=[rħ])")
    règle_remplacement = {"e": "ė", "i": "ė", "u": "ȯ"}


# Si cette élévation s'est produite avant l'abaissement précédent, même pas besoin de e > ɛ
class Élévation_e_court(ChangementPhonétique):
    nom = "Élévation du e court"
    description = "Le e court qui n'a pas été précédemment abaissé, s'élève. Cela a pour conséquence l'absence de e " \
                  "court en gothique. Semble inclure la diphtongue eu qui devient iu."
    source = ["GL"]
    motif = re.compile("[Ee]|EU|eu")
    règle_remplacement = {"e": "i", "eu": "iu"}


# ō n'existe pas en PGERM : elle apparaît en GOTH suite à l'élévation de ɔ̄ pas devant une voyelle, mais ça permet de
# jouer avec l'ordre des innovations plus facilement
class Abaissement_e_o_longs_DevantVoyelles(ChangementPhonétique):
    nom = "Abaissement de ē et ō devant voyelles"
    description = "Les voyelles longues ē et (si elle existe) ō s'abaissent en respectivement ɛ̄ et ɔ̄ devant une " \
                  "voyelle."
    sources = ["GL"]
    motif = re.compile("[ēĒōŌ](?=[ȧạėẹeēiīȯọoōuū])")
    règle_remplacement = {"ē": "ẹ", "ō": "ọ"}


class Monophtongaison_au_ai(ChangementPhonétique):
    nom = "Monophtongaison de ɑu et ɑi"
    description = "Les diphtongues ɑu et ɑi se simplifient en les voyelles longues ɔ̄ et ɛ̄."
    sources = ["GL"]
    motif = re.compile("ȧu|ȧi|ȦI|ȦU")
    règle_remplacement = {"ȧu": "ọ", "ȧi": "ẹ"}


évolution = [
        # initiatives perso
        AjustementsTemporaires1,
        SyncopeVocaleAtoneThématique,
        RéductionVocaleAtoneFinale,
        DisparitionNasalisation,

        # conditons d'apparition des consonnes
        Renforcement_ww_jj,
        Renforcement_ggj,
        PlosivationSonoresDerrièreConsonne,
        AssourdissementFinalOuDevantConsonnesSourdes,
        Mutation_fl_En_thl,

        # conditions d'apparition des voyelles
        Élévation_e_o_LongsMiouverts,
        Abaissement_e_o_longs_DevantVoyelles,
        Abaissement_e_i_u_Devant_r_h_hw,
        Élévation_e_court,
        Monophtongaison_au_ai
    ]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée
