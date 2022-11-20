from innovations import ChangementPhonétique
import re

# NORD-OUEST


class Ajustements_temporaire(ChangementPhonétique):
    motif = re.compile("ọz?$")
    règle_remplacement = {"ọz": "ạz", "ọ": "ū"}

# ATTENTION : Développement consécutif de ǣ en ON i / OGERM a a priori pas implémenté, ni la diphtongue
class RéductionVocaliqueAtone(ChangementPhonétique):
    nom = "Raccourcissement des voyelles longues en dernière syllabe"
    description = "Dans la dernière syllabe, œ̄ et œ̄i sont raccourcis en œ puis élevé en u, ë est raccourci en " \
                       "è puis élevé en e* (développement consécutif en i en norrois, a en germanique occidental)."
    sources = ["PHE"]
    motif = re.compile("ȧi|ȧu|[ẹệòȍộū]|ọ(?=[^ȧeiȯu]+$)")  # ɔ̄ mais pas médial, donc que des consonnes jusqu'à la fin
    règle_remplacement = {"ộ": "ọ", "ȍ": "ọ", "ò": "ạ", "ọ": "ạ", "ẹ": "i", "ệ": "ạ", "ȧi": "ē", "ȧu": "ọ", "ū": "u"}


# Potentiellement commun avec ci-dessus et ajustemps ingv, mais il faut voir à rendre tout ça cohérent...
class Élévation_omiouv(ChangementPhonétique):
    nom = "Élévation du ɔ oral en o"
    description = "Le ɔ oral s'élève en o."
    motif = re.compile("(?i:[ȯọộ])")
    règle_remplacement = {"ȯ": "o", "ọ": "ō", "ộ": "ô"}


# cf mutation en a dans discussions
# Rajouté : exception du j qui bloque la proximité du a (hugjaną !> **hogjaną)
class UmlautEn_a(ChangementPhonétique):
    nom = "Mutation vocalique en a"
    description = "U est abaissé en O lorsque la syllabe suivante contient une voyelle basse."
    sources = ["PHE", "haraldr"]
    chronologie = +200
    motif = re.compile("(?<![ȦE])[U](?!n)(?=[^j]+[ȧạậoōảòȍ])")
    règle_remplacement = {"U": "O"}


# ATTENTION : Différence de chronologie avec le raccourcissement précédent à implémenter !
class Abaissement_e_Long(ChangementPhonétique):
    nom = "Abaissement de ẹ"
    description = "ẹ (peut-ệtre déjà prononcé ǣ depuis le PG) est abaissé en ā. Précède le raccourcissement" \
                       "des voyelles longues en germanique occidental, mais le suit en vieux norrois."
    sources = ["PHE"]
    motif = re.compile("Ẹ")
    règle_remplacement = "Ạ"


# désactivté, penser à récuperer nom et descr avant suppression !
class MonophtongisationDiphtonguesNonAccentuées_NOGERM(ChangementPhonétique):
    nom = "Monophtongisation des diphtongues non-accentuées"
    description = "Les diphtongues ai et au ne portant pas l'accent, toujours dans les désinences, deviennent " \
                       "respectivement ẹ et ō."
    sources = ["PHE"]
    motif = re.compile("ȧi|ȧu")
    règle_remplacement = {"ȧi": "ẹ", "ȧu": "ō"}



# OUEST




class OcclusionDentaleFricativeSonore(ChangementPhonétique):
    nom = "Occlusion de đ"
    description = "En germanique occidental, đ est devenu une occlusive en toutes positions."
    sources = ["PHOE", "HGCS"]
    chronologie = "2ème - 4ème siècles"
    motif = re.compile("đ")
    règle_remplacement = "d"


'''
# Ceci devrait se trouver en fin de PGERM, mais fait sauter formes canoniques comme *ubiri, peut-être que ça ne concerne
# que les formes verbales (biridi) ?, les autres exemples du lexique PIE => PGERM n'étant pas vérifiées dans wiktionary...
class RaccourcissementTroisièmeSyllabe_VANGL(Innovation):
    nom = "Raccourcissement de la troisième syllabe."
    description = "Raccourcissement des mots par la perte des voyelles courtes dans les syllabes au-delà de la deuxième."
    sources = ["PHE"]
    motif = re.compile("[ȦEIOU].+[ȧeiou].+(?P<x>[ȧeiou])")
    # ATTENTION : Version VANGL de la mutation en I, qui ne concerne que les courtes. Pour l'instant impossible à fusionner
# avec la version VISL. Les longues et diphtongues devraient suivre le même processus plus tard (à vérifier).
class UmlautEn_i_VANGL(Innovation):
    nom = "Mutation allophonique vocalique en i"
    description = "Cette mutation concerne les voyelles courtes a, e, u qui sont élevées ou avancées par effet " \
                       "de proximité avec i (ou j) dans la syllabe suivante. Cette mutation est allophonique à ce " \
                       "stade, et peut-être même déjà présente en proto-germanique. Les voyelles longues et les " \
                       "diphtongues suivront ce processus par la suite."
    sources = ["PHE"]
    motif = re.compile("(?i:(?P<x>[ȧou](?!i))[^ȧeiouạẹīōū])+[ij]")
    règle_remplacement = {"ȧ": "æ", "o": "ø", "u": "y",
                                   "Ȧ": "Æ", "O": "Ø", "U": "Y"}
'''


# Note pour le futur : n'affecte pas les langues du sud et du centre de l'Allemagne.
class Perte_z_Final(ChangementPhonétique):
    nom = "Perte du z final."
    description = "Le z final se perd."
    sources = ["PHE"]
    motif = re.compile("z$")


# Similaire (mais relié ?) à la rhotacisation du VISL
class Rhotacisation(ChangementPhonétique):
    nom = "Rhotacisation"
    description = "Changement du z en r."
    sources = ["PHE"]
    motif = re.compile("z")
    règle_remplacement = "r"


class RéassignementGroupes_ww_jj(ChangementPhonétique):
    nom = "Réassignement des groupes -ww- et -jj-"
    description = "Les groupes -ww- et -jj-, quelles qu'en soient les origines, se séparent en deux " \
                       "constituantes : la première vient créer une diphtongue avec la voyelle précédente, la " \
                       "seconde engage la syllabe suivante."
    sources = ["HL"]
    motif = re.compile("ww|jj")
    règle_remplacement = {"ww": "Uw", "jj": "Ij"}


# ATTENTION : Probablement incomplet ! Affecte diphtongues débutant par i ou u, dont  les j / w sous-jacents sont
# doublés. ij à clarifier.
class Gémination(ChangementPhonétique):
    nom = "Gémination du germanique occidental"
    description = "Après une voyelle courte, une consonne ou demi-consonne suivie de j (ou ij) se double. Le j " \
                       "se perd. N'affecte que partiellement les consonnes r et l."
    sources = ["PHE", "WGG"]
    motif = re.compile("(?<=(?i:[ȧeiouøyæ]))[ptkꝑŧꝁƀđǥbdgnl](?=j)")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        return dict_de_groupes.group()*2


# Inconsistent : aplaz => æppel mais tahrą => tẹar (tæhher dialectal)
class GéminationPar_l_r_OGERM(ChangementPhonétique):
    motif = re.compile("(?<=(?i:[ȧeiouøyæ]))[ptkꝑŧꝁƀđǥbdgnl](?=[lr])")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        return dict_de_groupes["consonne"]*2


class GraphieObstruantes1(ChangementPhonétique):
    motif = re.compile("ǥǥ|ƀƀ")
    règle_remplacement = {"ǥǥ": "gg", "ƀƀ": "bb"}


class Délabialisation(ChangementPhonétique):
    motif = re.compile("(?<=n[kg])w")


class AjustementsTemporaires_OGERM(ChangementPhonétique):
    motif = re.compile("ō$")
    règle_remplacement = "ạ"


évolution = [

    # Northwest Germanic period
    Ajustements_temporaire,  # ōz$ > āz$, ō$ > ū$
    RéductionVocaliqueAtone,
    Élévation_omiouv,
    RéassignementGroupes_ww_jj,
    UmlautEn_a,
    Abaissement_e_Long,

    # West germanic period
    OcclusionDentaleFricativeSonore,
    Perte_z_Final,
    Rhotacisation,
    Gémination,
    # GéminationPar_l_r_OGERM,  # inconsistant
    Délabialisation,
    GraphieObstruantes1,
    # AjustementsTemporaires_OGERM,  # ō$ > ā
]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée

