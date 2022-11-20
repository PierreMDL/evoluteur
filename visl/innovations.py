from innovations import ChangementPhonétique
import re


### NO GERM ###


class Ajustements_temporaires(ChangementPhonétique):
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


###




class AjustementsTemporaires(ChangementPhonétique):
    nom = "Ajustements temporaires du vieux norrois"
    description = "Suppression de la nasale courte finale ą, traitement des voyelles atones finales (peut-être " \
                  "redondant avec la suite ou même le précédent), et surtout rhotacisation du z final."

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        forme_phono = re.sub(re.compile("(?<=ȧn)ả$"), "", forme_phono)
        forme_phono = re.sub(re.compile("[òōảųz]$"), lambda res: {"ò": "ạ", "ō": "ạ", "ả": "ȧ", "z": "R", "ų": "u"
                                                                  }.get(res.group()), forme_phono)
        return forme_phono


class Renforcement_ww_jj(ChangementPhonétique):
    nom = "Renforcement des groupes ww et jj"
    description = "Les groupes de semi-consonnes ww et jj se renforcent en respectivement ggw et ggj. Cela " \
                       "doit arriver précocement car l'innovation se trouve en vieux norrois et (différemment) " \
                       "en gothique, pourtant censés ne pas appartenir au même groupement. Sans doute un " \
                       "argument pour la théorie du continuum dialectal."
    sources = ["NWG"]

    motif = re.compile("ww|jj")
    règle_remplacement = {"ww": "ggw", "jj": "ggj"} # je laisse les occlusives par analogie avec gémination


# similaire à gémination OGERM mais seulement ǥ (g pas possible : jamais après une voyelle) et k (ꝁ? perdu plus tard?)
class Gémination(ChangementPhonétique):
    nom = "Gémination du vieux norrois"
    description = "Le principe de gémination en vieux norrois se restreint aux consonnes vélaires ǥ, ꝁ et k : " \
                  "celles-ci se doublent lorsqu'elles sont précédées d'une voyelle courte et suivies de j. " \
                  "L'occlusive vélaire sonore g ne pouvait historiquement pas se trouver dans cet environnement."

    motif = re.compile("(?<=(?i:[ȧeiouøyė]))(?P<consonne>[ǥkꝁ])(?=j)")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        return dict_de_groupes["consonne"]*2




class Perte_j_Initial(ChangementPhonétique):
    motif = re.compile("^j")


# ajout perso pour que lahsaz > lax (! **láx), exactement pareil en VANGL, cf destin_du_h
class PlosivationGroupe_hs(ChangementPhonétique):
    motif = re.compile("(?=(?P<longue>(?i:ȧu|ė[iy]|i[ūō]|eu|[ạēīōūẹǿȳàẽĩõũ]))?)ꝁs(?=(?P<t>t)?)")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes["longue"] or dict_de_groupes["t"]:
            return ""
        else:
            return "k"


# Mon initiative, allonge voyelle précédente, allonge quelques consonnes suivantes
# ATTENTION: il faut comme assimilation instaurer forme courte / forme longue selon environnement
class AssimilationCompensatrice_h_Postvocalique(ChangementPhonétique):
    motif = re.compile("(?P<avant>(?i:(?<![ėȧīe])[ȧeėiouyø]))?(?<!^)ꝁ(?P<apres>t)?")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        pre = ""
        post = ""
        if dict_de_groupes["avant"]:
            pre = {"ȧ": "ạ", "e": "ē", "ė": "ẹ", "i": "ī", "o": "ō", "u": "ū", "y": "ȳ", "ø": "ǿ",
                   "Ȧ": "Ạ", "E": "Ē", "Ė": "Ẹ", "I": "Ī", "O": "Ō", "U": "Ū", "Y": "Ȳ", "Ø": "Ǿ",
                  }.get(dict_de_groupes["avant"])
        if dict_de_groupes["apres"]:
            post = {"t": "tt"}.get(dict_de_groupes["apres"])
        return pre + post


# RUKI chez les Germains, auh > ō ?
class RUKI(ChangementPhonétique):
    motif = re.compile("(?i:ȧi)(?=[ꝁwr])")
    règle_remplacement = {"ȧi": "ạ"}


class HarmonisationDipthongues(ChangementPhonétique):
    motif = re.compile("(?i:ȧi|eu)")
    règle_remplacement = {"ȧi": "ėi", "eu": "iū"}


# pas forcément au point : ON semble indiquer un dipthongaison longue ē > jā/jǭ, seul ē dans ce cas est ancien eh-
class Diphtongaison(ChangementPhonétique):
    nom = "Diphtongaison"
    sources = ["HAR", "NGL", "ON"]
    motif = re.compile("(?<![wrl])[EĒ](?=.*(?P<apres>[wȧạuū]))")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes["apres"] in list("ȧạ"):
            return {"E": "jȦ", "Ē": "jẠ"}.get(dict_de_groupes.group())
        elif dict_de_groupes["apres"] in list("wuū"):
            return {"E": "jȮ", "Ē": "jỌ"}.get(dict_de_groupes.group())


class Perte_w_Devant_o_u(ChangementPhonétique):
    motif = re.compile("w(?=[uoUO])")


class AssourdissementFinal(ChangementPhonétique):
    sources = ["NGL"]
    motif = re.compile("[bdg]$")
    règle_remplacement = {"b": "p", "d": "t", "g": "k"}


class UmlautEn_i(ChangementPhonétique):
    motif = re.compile("(?i:ȧu|iū|[ȧeouạōū])(?=.*[ij])")
    règle_remplacement = {"ȧ": "ė", "e": "i", "o": "ø", "u": "y", "ạ": "ẹ", "ō": "ǿ", "ū": "ȳ", "ȧu": "ėy", "iū": "ȳ"}


class UmlautEn_z(ChangementPhonétique):
    motif = re.compile("(?i:ȧu|iū|[ȧoeuạōū])(?=z)")
    règle_remplacement = {"ȧ": "ė", "e": "i", "o": "ø", "u": "y", "ạ": "ẹ", "ō": "ǿ", "ū": "ȳ", "ȧu": "ėy", "iū": "ȳ"}


class UmlautEn_u(ChangementPhonétique):
    motif = re.compile("(?i:ėi|[ȧạėẹiī](?![uūō]))(?=.+[uw])")
    règle_remplacement = {"ȧ": "ȯ", "ạ": "ọ", "ė": "ø", "ẹ": "ǿ", "i": "y", "ī": "ȳ", "ėi": "ėy"}


class NasalisationCompensatrice(ChangementPhonétique):
    motif = re.compile("(?P<voy>(?i:(?<![ėeȧī])[ȧeėioȯuyø]))(?P<consnas>[mn])(?=(?P<apres>[ȧeėioȯuyøạēẹīōọūȳǿgnmbdpꝑŧk]))?")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes["apres"]:  # si consonne nasale suivie d'une voyelle, ou d'une consonne homorganique (g, m, b, ƀ, ꝑ, n, d)
            nasale_courte = {
                "ȧ": "ả", "e": "ę", "ė": "ẻ", "i": "į", "o": "ǫ", "ȯ": "ỏ", "u": "ų", "y": "ỷ", "ø": "ở",
                "Ȧ": "Ả", "E": "Ę", "Ė": "Ẻ", "I": "Į", "O": "Ǫ", "Ȯ": "Ỏ", "U": "Ų", "Y": "Ỷ", "Ø": "Ở"
            }.get(dict_de_groupes["voy"])
            return nasale_courte + dict_de_groupes["consnas"]  # alors nasale courte + la consonne nasale qui survit
        else:
            nasale_longue = {
                "ȧ": "à", "e": "ẽ", "ė": "è", "i": "ĩ", "o": "õ", "ȯ": "ò", "u": "ũ", "y": "ỳ", "ø": "ờ",
                "Ȧ": "À", "E": "Ẽ", "Ė": "È", "I": "Ĩ", "O": "Õ", "Ȯ": "Ò", "U": "Ũ", "Y": "Ỳ", "Ø": "Ờ"
            }.get(dict_de_groupes["voy"])
            return nasale_longue  # sinon nasale longue, compensée par la disparition de la consonne nasale




# toutes ces voyelles, notamment les nasales, notamment longues, ne se trouvaient sans doute pas atone
class SyncopeAtone(ChangementPhonétique):
    motif = re.compile("[ȧeėioȯuyøảęẻįǫỏųỷởạēẹīōọūȳǿàẽèĩõòũỳờ](?=.?$)")
    règle_remplacement = {
            "ȧ": "", "e": "", "i": "", "o": "", "u": "",
            "ạ": "ȧ", "ē": "e", "ī": "i", "ō": "o", "ū": "u",
            "à": "ả", "ẽ": "ę", "è": "ẻ", "ĩ": "į", "õ": "ǫ", "ò": "ỏ", "ũ": "ų", "ỳ": "ỷ", "ờ": "ở"}


# att assimil -zn- ne devrait pas prendre en compte le suffixe verba -na- (uznaną > orna)
# fusionner z et R (càd transformer z en R en toute position plus avant), attention à dalaz > dalr tout de même !!!
class AssimilationsDiverses(ChangementPhonétique):
    motif = re.compile("(?P<voyelle>(?i:[ȧeėioȯuyøảęẻįǫỏųỷởạēẹīōọūȳǿàẽèĩõòũỳờ]))?(mp|mꝑ|nt|nk|sR|lŧ|nŧ|z[dnrl]|[rl]z|(?<![^ȦĖEI][ȦĖEIOȮUYØẢĘẺĮǪỎŲỶỞ])[nl]R)")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes["voyelle"]:
            rempl = {"mp": "pp", "mꝑ": "mm", "nt": "tt", "nk": "kk", "lR": "ll", "nR": "nn", "sR": "ss", "lŧ": "ll",
                     "nŧ": "nn", "zd": "dd", "zn": "nn", "zr": "rr", "rz": "rr", "zl": "ll", "lz": "ll"}.get(dict_de_groupes.group(2))
        else:
            # juste la première lettre du groupe derrière consonne pour empêcher ebnaz => jafnn
            rempl = {"mp":  "p", "mꝑ":  "m", "nt":  "t", "nk":  "k", "lR":  "l", "nR":  "n", "sR":  "s", "lŧ":  "l",
                     "nŧ":  "n", "zd":  "d",  "zn": "n", "zr":  "r", "rz":  "r", "zl":  "l", "lz":  "l"}.get(dict_de_groupes.group(2))
        return (dict_de_groupes["voyelle"] or "") + rempl




class Perte_w_Devant_r(ChangementPhonétique):
    motif = re.compile("w(?=r)")


class AjustementsTemporaires2(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        forme_phono = re.sub(re.compile("(?<!^)(ŧ)"), "đ", forme_phono)
        forme_phono = forme_phono.translate(str.maketrans("wŧꝁǥꝑđRƀz", "vþhgfðrfr"))
        forme_phono = forme_phono.replace("ks", "x")
        return forme_phono


évolution = [
    # NOGERM
    Ajustements_temporaires,
    RéductionVocaliqueAtone,
    Élévation_omiouv,
    UmlautEn_a,
    Abaissement_e_Long,

    # VNORR
    AjustementsTemporaires,
    Renforcement_ww_jj,
    Gémination,
    Perte_j_Initial,
    PlosivationGroupe_hs,  # ajout perso pour expliquer lahsaz > lax (! **láx)
    AssimilationCompensatrice_h_Postvocalique,  # doit se faire avant diphtongaison pour éviter que fehu > fjǫ
    RUKI,  # ajout perso pour expliquer flaihaz > flár
    HarmonisationDipthongues,
    Diphtongaison,
    Perte_w_Devant_o_u,
    AssourdissementFinal,
    UmlautEn_i,
    UmlautEn_z,
    UmlautEn_u,

    # VISL
    NasalisationCompensatrice,
    SyncopeAtone,
    AssimilationsDiverses,
    Perte_w_Devant_r,
    AjustementsTemporaires2
]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée
