from innovations import ChangementPhonétique
import re


class AjustementsTemporaires(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        forme_phono = re.sub("(?i:[òộȍ])", lambda opostnas: {"ỏ": "ǫ", "ò": "õ", "ȍ": "ö",
                                                           "Ỏ": "Ǫ", "Ò": "Õ", "Ȍ": "Ö"
                                                             }.get(opostnas.group()), forme_phono) # élévation du ɔ nasal

        return forme_phono


# ATTENTION, normalement la nasalisation proto-germanique tardif a déjà rendu anh => ãh, est-ce que ceci est rendondant ?
# en tout cas le ã produit précédemment doit également devenir õ pour que þanhtaz => þōht
class NasalisationIngvaeonique(ChangementPhonétique):
    motif = re.compile("((?i:[ȧeiou]))[mn](?=[sꝑŧꝁ])")

    @classmethod
    def règle_remplacement(self, dict_de_groupes):
        return {"ȧ": "à", "e": "ẽ", "i": "ĩ", "o": "õ", "u": "ũ",
                "Ȧ": "À", "E": "Ẽ", "I": "Ĩ", "O": "Õ", "U": "Ũ"}.get(dict_de_groupes.group(1))


class Élévation_a_LongNasal(ChangementPhonétique):
    motif = re.compile("[àÀ]")
    règle_remplacement = {"à": "õ"}


# Selon PHE : sauf suivi de w
class PremièreÉlévation_a_Partie1(ChangementPhonétique):
    nom = "Première élévation du a"
    description = "Première partie de l'élévation du a, concernant le ā (oral) qui s'élève vers ǣ."
    sources = ["PHOE", "PHE"]
    motif = re.compile("(?i:ạ)(?![mn])")
    règle_remplacement = {"ạ": "ǣ"}


class Monophtongaison_ai(ChangementPhonétique):
    nom = "Monophtongaison de la diphtongue ai"
    description = "La diphtongue -ɑi- héritée du proto-germanique se simplifie en -ā-. Ce changement s'opère " \
                       "nécessairement après la première élévation du ā, ce qui explique que la diphtongue n'ait " \
                       "pas pris le même chemin. À scorer, cette monophtongaison a pu également faire partie de " \
                       "l'harmonisation des diphtongues plus tardivement dans l'histoire du vieil anglais."
    sources = ["PHOE"]

    motif = re.compile("ȧi|ȦI")
    règle_remplacement = {"ȧi": "ạ"}


# Selon PHE : sauf si suivi d'une géminée ou d'une voyelle postérieure
# pourquoi faranaz > farænæ et pas færænæ ?
class PremièreÉlévation_a_Partie2(ChangementPhonétique):
    nom = "Élévation du a court"
    description = "Le a oral court est élevé en æ. Atone et suivie d'une nasale, elle subit la même élévation, " \
                       "ce qui suggère qu'elle était restée orale également dans ce cas précis."
    sources = ["PHE", "PHOE"]

    motif = re.compile("ȧ(?!u)|Ȧ(?![Umn])")
    règle_remplacement = {"ȧ": "æ"}



''' VANGL '''
class HarmonisationDiphtongues(ChangementPhonétique):
    nom = "Harmonisation des dipthongues"
    description = "Les diphtongues restantes héritées du proto-germanique au, eu et iu s'harmonisent : leurs " \
                       "composantes se réajustent sur même ouverture. La première composante s'allonge."
    sources = ["PHE", "PHOE"]

    motif = re.compile("(?i:ȧu|eu|iu)")
    règle_remplacement = {"ȧu": "ǣȧ", "eu": "ēo", "iu": "īu"}



# ajout perso pour que lahsaz > leax (! **lēax), exactement pareil en VISL, cf destin_du_h
# en VANGL doit se trouver avant dipthongaison sinon sehs > seox
class PlosivationGroupe_hs(ChangementPhonétique):
    motif = re.compile("(?P<longue>(?i:[ǣīē][ȧuyo]|[ạēīōūǣȳǿàẽĩõũ]))?ꝁs(?P<t>t)?")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes["longue"] or dict_de_groupes["t"]:
            return (dict_de_groupes["longue"] or "") + "s" + (dict_de_groupes["t"] or "")
        else:
            return "ks"


# ATTENTION : à corriger, pas de diphtongaison devant -llj-, et i diphtongue devant w mais pas wi
class Diphtongaison(ChangementPhonétique):
    nom = "Diphtongaison"
    description = "Les voyelles antérieures courtes æ, e, i ainsi que les voyelles antérieures longues ǣ et ī " \
                       "s'allongent en diphtongues respectivement courtes æɑ, eo, iu, et longues ǣa et īu. Les " \
                       "conditions varient pour chaque élément : toutes devant h, toutes les courtes devant le " \
                       "groupe r + consonne, e et i courts devant w, æ court devant le groupe l + consonne et e " \
                       "devant les groupes lk et lh."
    sources = ["PHE", "PHOE"]
    motif = re.compile("(?i:[æei](?=ꝁ|r[^ȧeiouæyøjw])|[ei](?=w)|æ(?=l[^ȧeiouæyøjw])|e(?=l[ꝁk])|[ǣī](?=ꝁ))")
    règle_remplacement = {"æ": "æȧ", "e": "eo", "i": "iu", "ǣ": "ǣȧ", "ī": "īu"}


# Rajouté : -(i)j- bloque le rétablissement du ɑ ! (explique farjaną > færjaną > ferian et pas **færian ou pire)
class Rétablissement_a(ChangementPhonétique):
    nom = "Restauration du a"
    description = "Le æ court précédemment élevé est restauré en ɑ lorsqu'une voyelle postérieure suit."
    sources = ["PHE", "PHOE"]
    motif = re.compile("[æÆ](?![ȧȦ])(?=[^iīj]*[ȧoōảǫõuū])")
    règle_remplacement = {"æ": "ȧ"}


# "for [ɣ] and /sk/ only, after other front vowels (/e/, /eː/, /æ/, /æː/)" pas y ni ø ?
class Palatalisation(ChangementPhonétique):
    nom = "Palatalisation"
    description = "Les consonnes, groupes et géminées vélaires sk, k, kk, g, gg, et ǥ se palatalisent en " \
                       "respectivement ʃ, tʃ, ttʃ, dʒ, ddʒ, et ʝ dans l'environnement de voyelles antérieures : " \
                       "toutes devant i, ī et j et derrière i, ī si aucune voyelle postérieure ne suit ; sk et ǥ " \
                       "derrière toutes voyelles antérieures si aucune voyelle postérieure ne suit ; k (à " \
                       "l'initiale) et ǥ devant toutes voyelles antérieures ; sk à l'initiale quel que soit " \
                       "l'environnement."
    sources = ["PHOE", "PHE"]
    motif = re.compile("(?i:((sk|gg|kk|[kgǥ])(?=[iīj]))|(((?<=^)k|ǥ)(?=[eyøæ]))|((?<=[iī])(sk|gg|kk|[kgǥ])(?![ȧạouōūw]))|((?<=[eēæǣyø])(sk|ǥ)(?![ȧạouōūw]))|(^sk))")
    règle_remplacement = {"k": "ʧ", "kk": "tʧ", "g": "ʤ", "gg": "dʤ", "ǥ": "ʝ", "sk": "ʃ"}

        # sauvegarde de l'ancien motif basé sur PHE pour référence :
        # self.motif = re.compile("(?i:(sk|(?<![aeiouæøyāēīōūȳǿǣ])ǥ(?=[eiyøæēīȳǿǣ])|(?<=[eiyøæēīȳǿǣ])ǥ(?![aeiouæøyāēīōūȳǿǣ])|[kg]{1,2}(?=[iīj])|(?<=[iī])[kg](?![aeiouæøyāēīōūȳǿǣ])|^k(?=[eiyøæēīȳǿǣ])))")


class DiphtongaisonPalatale(ChangementPhonétique):
    nom = "Diphtongaison palatale"
    description = "Après une consonne initiale nouvellement palatalisée, les voyelles antérieures e, ē, æ, ǣ " \
                       "deviennent respectivement les diphtongues ie, īe, eɑ et ēɑ."
    sources = ["PHOE", "PHE"]
    motif = re.compile("(?<=^[ʃʒʝj])(?i:[eēæǣ](?![ȧo]))")
    règle_remplacement = {"e": "iy", "ē": "īy", "æ": "æȧ", "ǣ": "ǣȧ"}


# Sans doute convention d'écriture pour a, o, u et pas véritable changement phonologique !
class FausseDiphtongaisonPatale_VANGL(ChangementPhonétique):
    nom = "Fausse diphtongaison palatale"
    description = "Après une consonne nouvellement palatalisée, les voyelles postérieures u, o et ɑ sont " \
                       "respectivement transcrites par les diphtongues eo, eo et ea. Il s'agit vraisemblablement " \
                       "d'une convention d'écriture plus que d'un véritable changement phonologique."
    sources = ["PHOE", "PHE"]
    motif = re.compile("(?=[ʧʃʤʝj])(?i:[ȧou])")
    règle_remplacement = {"u": "eo", "o": "eo", "ȧ": "æȧ"}


class Métathèse(ChangementPhonétique):
    nom = "Métathèse"
    description = "La consonne r et une voyelle courte suivante subissent une métathèse devant s, n et parfois d."
    sources = ["PHOE"]
    motif = re.compile("(?<!(?i:[^ȧeiouyæøạēīōū]))r[ȧeiouæyø](?=[snd])")

    @classmethod
    def règle_remplacement(cls, dict_de_groupe):
        return dict_de_groupe.group()[1] + dict_de_groupe.group()[0]




class UmlautEn_i_2(ChangementPhonétique):
    motif = re.compile("(?i:[æǣ]ȧ|[eē]o|[iī]u|ȧ[mn]|[ȧæeouạōū])(?=[^ȧeouæạēīōūǣ]*[ij])")
    règle_remplacement = {"ȧ": "æ", "æ": "e", "o": "ø", "e": "i", "u": "y", "æȧ": "iy", "iu": "iy", "eo": "iu",
                          "ạ": "ǣ",           "ō": "ǿ",           "ū": "ȳ", "ǣȧ": "īy", "īu": "īy", "ēo": "īu",
                          "ȧm": "em", "ȧn": "en", "Ȧm": "Em", "Ȧn": "En"}  # laisser Ȧm et Ȧn comme ça svp


# modifié pour prendre en compte les voyelles précédentes pour que hają > hwæġ (et pas **hwæi) et trewwaz > trēow (et pas **trēou)
class Perte_a_AtoneFinal(ChangementPhonétique):
    nom = "Perte du a atone final"
    description = "Le ɑ et (surtout) ses variantes élevée et nasale æ et ɑ̨ disparaissent en position finale."
    motif = re.compile("(?i:(?P<avant>((?![ȧeouyøæạēōūǣȳǿ])i?j|(?<![ȧeiouyøæạēīōūǣȳǿ])w)?))([æȧả])$")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        return {"": "", "j": "i", "ij": "ī", "w": "u"}.get(dict_de_groupes["avant"])




class SyncopationMédiale(ChangementPhonétique):
        # médial, en syllabe ouverte donc seulement une consonne non-finale suivante
    motif = re.compile("[ȧæe](?=[^ȧeiouyøæạēīōūǣȳǿ][ȧeiouyøæạēīōūǣȳǿ])")


class PerteVoyellesFerméesFinales(ChangementPhonétique):
        # finale, derrière syllabe longue donc voyelle longue + consonne, ou diphtongue + consonne, ou plus d'une consonne
    motif = re.compile("(?=(?i:((?<=[ạēīōūǣȳǿ][^ȧeiouyøæạēīōūǣȳǿ])|(?<=[ǣīēæie][ȧuyo][^ȧeiouyøæạēīōūǣȳǿ])|(?<=[^ȧeiouyøæạēīōūǣȳǿ]{2}))))[iu]$")


class PerteVoyellesFerméesMédiales(ChangementPhonétique):
        # médial, derrière syllabe longue et en syllabe ouverte, v'là le sujet quoi
    motif = re.compile("(?=(?i:((?<=[ạēīōūǣȳǿ][^ȧeiouyøæạēīōūǣȳǿ])|(?<=[ǣīēæie][ȧuyo][^ȧeiouyøæạēīōūǣȳǿ])|(?<=[^ȧeiouyøæạēīōūǣȳǿ]{2}))))[iu](?=[^ȧeiouyøæạēīōūǣȳǿ][ȧeiouyøæạēīōūǣȳǿ])")


class Perte_j_DerrièreSyllabeLongue(ChangementPhonétique):
    motif = re.compile("(?=(?i:((?<=[ạēīōūǣȳǿ][^ȧeiouyøæạēīōūǣȳǿ])|(?<=[ǣīēæie][ȧuyo][^ȧeiouyøæạēīōūǣȳǿ])|(?<=[^ȧeouyøæạēīōūǣȳǿ]{2}))))j")

    # pour référence, supprimer le i? et l'interdiction de i précédent permet le hiatus de frijondz -> friōnd -> frīond -> frēond
    # ("(?i:((?<=[āēīōūǣȳǿ][^aeiouyøæāēīōūǣȳǿ])|(?<=[ǣīēæie][auyo][^aeiouyøæāēīōūǣȳǿ])|(?<=[^aeiouyøæāēīōūǣȳǿ]{2}))(?P<x>i?j))")


''' PAS AU POINT
# derrière perte de j à cause de sa complexité, et parce que hiatus par perte de h plus loin se débrouille tout seul
class AssimilationVocalique_VANGL(Innovation):
    motif = re.compile("(?P<x>(?i:(?P<longue>[īēǣ][auyo]|[āēīōūȳǿǣ])|(?P<courte>[ieæ][auyo]|[aeiouyæø]))(?P<post>[æō]))")
    règle_remplacement = self.fonc_a_passer

    def règle_remplacement(self, dict_de_groupes):
        if dict_de_groupes["longue"]:
            return dict_de_groupes["longue"] # si la voyelle ou diphtongue précédente est déjà longue : pas de rallongement
        else : # voyelle ou diphtongue précédent déjà long
            return dict_de_groupes["ant"]
'''


# Accordément au dialect west-saxon (une consonne : labiale ou liquide), sinon on s'en sort plus
class MutationPostérieure(ChangementPhonétique):
    motif = re.compile("(?<![iI])[IEie](?=[ꝑƀbwlr][ȧouạōū])")
    règle_remplacement = {"e": "eo", "i": "iu"}


# gestion des hiatus (en tout dernier) pas très beau mais ça semble fonctionner
class PerteCompensatrice_h_Intervocalique(ChangementPhonétique):
    motif = re.compile("(?P<ant>(?i:[æieǣīē][ȧuyo]|[ạēīōūȳǣǿàĩũȧeiouæyø]))(?P<laterale>[rl]?)ꝁ(?![ptkꝑŧꝁ]|$)(?P<post>[ȧæiouạōǣ]?)")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        voyelle = dict_de_groupes["ant"]
        latérale = dict_de_groupes["laterale"]
        if voyelle.lower() in list("ạēīōūȳǣǿàĩũ") + ["ǣɑ", "īu", "īy", "ēo"]:
            return voyelle + latérale + (dict_de_groupes["post"] if latérale else "")
        else:
            return {"ȧ": "ạ", "e": "ē", "i": "ī", "o": "ō", "u": "ū", "y": "ȳ", "æ": "ǣ", "ø": "ǿ",
                    "æȧ": "ǣȧ", "iu": "īu", "iy": "īy", "eo": "ēo",
                    "Ȧ": "Ạ", "E": "Ē", "I": "Ī", "O": "Ō", "U": "Ū", "Y": "Ȳ", "Æ": "Ǣ", "Ø": "Ǿ",
                    "ÆȦ": "ǢȦ", "IU": "ĪU", "IY": "ĪY", "EO": "ĒO",
                    }.get(voyelle) + latérale + (dict_de_groupes["post"] if latérale else "")




# Rajouté : ǣ > e (skurtijǭ > skurtijā > skurtijǣ > scyrtǣ > scyrte), ī > e (magadīn > mæġdīn > mæġden )
class RéductionVocaleAtone(ChangementPhonétique):
    motif = re.compile("[ôōæǣiī]|ē(?!o)|u(?!$)")
    règle_remplacement = {"ẹ": "e", "ē": "e", "ō": "ȧ", "ī": "e", "æ": "e", "ǣ": "e", "i": "e", "u": "o"}



class UmlautPalatal(ChangementPhonétique):
    motif = re.compile("(?i:eo|io|e)(?=ꝁ[stŧ])")
    règle_remplacement = {"eo": "i", "iu": "i", "e": "i"}


class Désarrondissement_ø(ChangementPhonétique):
    motif = re.compile("(?i:[øǿ])")
    règle_remplacement = {"ø": "e", "ǿ": "ē"}

class RaccourcissementVocaliquePrégroupal_VANGL(ChangementPhonétique):
    motif = re.compile("(?i:[ạēīōūȳǣ])(?=[^ȧeiouyæøạēīōūȳǣ]{3})")
    règle_remplacement = {'ạ': 'ȧ', 'ē': 'e', 'ī': 'i', 'ō': 'o', 'ū': 'u', 'ǣ': 'æ', 'ȳ': 'y'}

class Abaissement_iu(ChangementPhonétique):
    motif = re.compile("(?i:iu|īu)")
    règle_remplacement = {"iu": "eo", "īu": "ēo"}

class Renforcement_ġ_Initial(ChangementPhonétique):
    motif = re.compile("^ǥ")
    règle_remplacement = "g"

class AjustementsTemporaires2(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        forme_phono = forme_phono.translate(str.maketrans("ꝑƀ", "ff"))
        forme_phono = re.sub("(?i:[àẽĩõũ])", lambda nas: {"ẽ": "ē", "õ": "ō", "à": "ā", "ĩ": "ī", "ũ": "ū",
                                                        "Ẽ": "Ē", "Õ": "Ō", "À": "Ā", "Ĩ": "Ī", "Ũ": "Ū"
                                                          }.get(nas.group()), forme_phono)
        return forme_phono



évolution = [
    # Ingvaeonic and Anglo-Frisian period
    AjustementsTemporaires,  # pour faire disparaître les labio-vélaires nasales
    NasalisationIngvaeonique,
    Élévation_a_LongNasal,
    PremièreÉlévation_a_Partie1,
    Monophtongaison_ai,
    PremièreÉlévation_a_Partie2,

    # Old English period : assimilation des hiatus à rajouter
    HarmonisationDiphtongues,
    Diphtongaison,
    Rétablissement_a,
    Palatalisation,
    # Second Fronting goes here
    DiphtongaisonPalatale,
    # FausseDiphtongaisonPatale_VANGL,  # convention graphique à faire sauter pour tomber sur les bonnes formes
    Métathèse,  # application aléatoire, faire gaffe
    UmlautEn_i_2,
    Perte_a_AtoneFinal,
    SyncopationMédiale,
    PerteVoyellesFerméesFinales,
    PerteVoyellesFerméesMédiales,
    Perte_j_DerrièreSyllabeLongue,
    # AssimilationVocalique_VANGL,  # Pas au point !
    MutationPostérieure,
    PlosivationGroupe_hs,  # ajout perso pour que lahsaz > leax (! **lēax)
    PerteCompensatrice_h_Intervocalique,
    UmlautPalatal,
    RéductionVocaleAtone,
    Désarrondissement_ø,
    # RaccourcissementVocaliquePrégroupal_VANGL,
    Abaissement_iu,
    Renforcement_ġ_Initial,
    AjustementsTemporaires2
]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée
