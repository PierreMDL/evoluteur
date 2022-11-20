import re
from innovations import ChangementPhonétique, DéplacementAccent, Centumisation


class Épenthèse(ChangementPhonétique):
    nom = "Épenthèse du proto-germanique"
    description = "Voyelle u épenthétique derrière consonnes sonores"
    chronologie = "-3500"
    motif = re.compile("[ḷṃṇṛḶṂṆṚ]")
    règle_remplacement = {"ḷ": "ul", "ṃ": "um", "ṇ": "un", "ṛ": "ur",
                          "Ḷ": "Ul", "Ṃ": "Um", "Ṇ": "Un", "Ṛ": "Ur",}


class AssimilationObstruantes(ChangementPhonétique):
    motif = re.compile("[bdgt]ʰ?[st]")
    règle_remplacement = {"bs": "ps", "ds": "ts", "gs": "ks", "bʰs": "ps", "dʰs": "ts", "gʰs": "ks",
                          "bt": "pt", "dt": "ss", "gt": "kt", "bʰt": "pt", "dʰt": "ss", "gʰt": "kt",
                          "ts": "ts", "tt": "ss"}
    nom = "Assimilation des obstruantes devant S ou T"


class RaccourcissementGéminées(ChangementPhonétique):
    nom = "Raccourcissement des géminées"
    description = "La géminée ss, ainsi que les éventuelles géminées apparues dans le cadre de la loi de " \
                       "Kluge, sont raccourcies après une consonne, diphtongue ou voyelle longue."
    motif = re.compile("(?<![aeiouAEIOU])(ss|pp|tt|kk)")
    règle_remplacement = {"ss": "s", "pp": "p", "tt": "t", "kk": "k"}


class SurélongationVoyellesLonguesFinales(ChangementPhonétique):
    motif = re.compile("[ĒŌēō]$")
    règle_remplacement = {"ē": "ê", "ō": "ô"}


# Derrière mutation laryngales dans PGL mais évidemment il faut bien que cette loi s'applique avant...
# ATTENTION : "possibly h₂", un exemple donné
class LoiDeCowgill(ChangementPhonétique):
    motif = re.compile("(?<=[mlrnwjiuIU])h[₂₃]w")  # "résonantes", donc pas voyelle, mais pour que gwih3waz => kwikwaz, il faut bien que le i soit "résonant"
    règle_remplacement = "gʷ"


# selon Lehmann
class LoiDeHoltzmann(ChangementPhonétique):
    nom = "Loi de Holtzmann (selon Lehmann)"
    description = "Partie profonde de la loi de Holtzmann, selon laquelle les semi-consonnes w et j, dans " \
                       "certaines conditions, se doublent. Selon l'interprétation de Lehmann, elles se doublent " \
                       "en proximité avec une laryngales : le w entre une voyelle courte et une laryngale, le j " \
                       "entre a ou i et une laryngale, ou après un groupe formé de a et d'une laryngale."
    sources = ["HL"]
    motif = re.compile("(?<=[aeiouAEIOU])w(?=h[₀₁₂₃])|(?<=[aiAI])j(?=h[₀₁₂₃])|(?=[aA]h[₀₁₂₃])j")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        return dict_de_groupes.group() * 2


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


class Délabialisation(ChangementPhonétique):
    motif = re.compile("ʷ(?=ʰ?[uU]n?t)")
    nom = "Délabialisation devant /ut/"
    description = "Délabialisation devant le groupe /ut/ ou /unt/"


# ajouté m, n aussi
class LoiDeDybo(ChangementPhonétique):
    nom = "Loi de Dybo"
    description = "Une voyelle longue atone est raccourcie lorsqu'elle est suivie de l ou r puis de la syllabe" \
                       "accentuée. Effectif en proto-germanique, proto-italic, proto-balto-slave et proto-celtique."
    sources = ["DG"]
    motif = re.compile("[āēīōū](?=[mnlr][^aeiouāēīōūêôûə]*[AEIOUĀĒĪŌŪÊÔÛƏ])")
    règle_remplacement = {"ā": "a", "ē": "e", "ī": "i", "ō": "o", "ū": "u"}


class PerteVoyellesCourtesFinales(ChangementPhonétique):
    motif = re.compile("((?i:[aeiouāēīōūêôûə][wj]?))([^wj]*)([wj]?[aeoAEO])$")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes[3].isupper():
            return dict_de_groupes[1].upper() + dict_de_groupes[2]
        else:
            return dict_de_groupes[1] + dict_de_groupes[2]


class MutationConsonnantiqueGermanique1(ChangementPhonétique):
    motif = re.compile("(kʷ|gʷ|(?<![skp])(?<!k[ʷʰ])(?<!kʷʰ)t|(?<!s)[pk]|b|d|g)(?![ʷʰ])")
    règle_remplacement = {"b": "ḅ",  "d": "ḍ",  "g": "g̣",  "gʷ": "g̣ʷ",
                          "p": "pʰ", "t": "tʰ", "k": "kʰ", "kʷ": "kʷʰ"}


class LoiDeKluge(ChangementPhonétique):
    nom = "Loi de Kluge"
    description = "Loi controversée qui fait apparaître des géminées par assimilation d'un n (souvent " \
                       "désinentiel)."
    sources = ["KL"]
    motif = re.compile("(?<![AEIOUĒŌ])(?<![AEIOUĒŌ][jw])(g̣ʷ?n|[ḅḍptkbdg]ʷ?ʰ?n)")
    règle_remplacement = {"pʰn": "ḅḅ", "tʰn": "ḍḍ", "kʰn": "g̣g̣", "kʷʰn": "g̣g̣ʷ",
                          "ḅn":  "ḅḅ", "ḍn":  "ḍḍ", "g̣n":  "g̣g̣", "g̣ʷn":  "g̣g̣ʷ",
                          "bʰn": "ḅḅ", "dʰn": "ḍḍ", "gʰn": "g̣g̣", "gʷʰn": "g̣g̣ʷ"}


class MutationConsonnantiqueGermanique2(ChangementPhonétique):
    motif = re.compile("gʷʰ|kʷʰ|bʰ|dʰ|gʰ|g̣ʷ|pʰ|tʰ|kʰ|kʷ|gʷ|kʰt|g̣|[ḅḍ]")
    règle_remplacement = {"bʰ": "ƀ", "dʰ": "đ", "gʰ": "ǥ", "gʷʰ": "ǥʷ",
                          "ḅ":  "p", "ḍ":  "t", "g̣":  "k", "g̣ʷ":  "kʷ",
                          "pʰ": "ꝑ", "tʰ": "ŧ", "kʰ": "ꝁ", "kʷʰ": "ꝁʷ"}


class LoiDeVerner(ChangementPhonétique):
    motif = re.compile("(?<!^)(?<![AEIOUĀĒĪŌŪÊÔÛƏ])(?<![AEIOUĀĒĪŌŪÊÔÛƏ][jwnm])((?<![ꝑŧꝁptks])s(?!s)|ꝁʷ|[ꝑŧꝁ](?!t))")  # û devrait déjà être raccourci suite à loi d'Osthoff
    règle_remplacement = {"ꝑ": "ƀ", "ŧ": "đ", "ꝁ": "ǥ", "ꝁʷ": "ǥʷ", "s": "z"}


class DéplacementAccent(DéplacementAccent):
    motif = re.compile("[əaeiouāēīōūêôû]")


class RelocalisationLabioVélaireInitiale(ChangementPhonétique):
    motif = re.compile("^ǥʷ")
    règle_remplacement = "ƀ"
    nom = "Relocalisation de /gw/ à l'initiale"


class AssimilationsDiverses(ChangementPhonétique):
    motif = re.compile("nw|ln|zm|rn|nm")
    règle_remplacement = {"nw": "nn", "ln": "ll", "zm": "mm", "rn": "rr", "nm": "mm"}


class RaccourcissementGroupeowo(ChangementPhonétique):
    motif = re.compile("owo")
    règle_remplacement = "ō"


class Recul_ew(ChangementPhonétique):
    motif = re.compile("ew(?![əaeiouāēōêôû])")
    règle_remplacement = "ow"


class Élévation_e(ChangementPhonétique):
    motif = re.compile("ej?e?")
    règle_remplacement = {"e": "i", "ej": "ī", "eje": "iji"}


class Raccourcissement_yi(ChangementPhonétique):
    motif = re.compile("i?ji")
    règle_remplacement = {"ji": "i", "iji": "ī"}


class Fusion_o_a(ChangementPhonétique):
    motif = re.compile("(?i:[oōôaāâ])")
    règle_remplacement = {"o": "ȧ", "ō": "ạ", "ô": "ậ",
                          "a": "ȧ", "ā": "ạ", "â": "ậ" }


class Dentalisation_m_Final(ChangementPhonétique):
    motif = re.compile("m$")
    règle_remplacement = "n"


class Dentalisation_m_DevantDentales(ChangementPhonétique):
    motif = re.compile("m(?=[đdŧtn])")
    règle_remplacement = "n"


class PerteNasalisatrice_n_FinalAtone(ChangementPhonétique):
    nom = "Perte compensatrice du n final atone"
    description = "La consonne n finale atone disparaît en nasalisant la voyelle précédente. Seules les " \
                       "voyelles ɑ, i, u, ɑ̄, ē, ī, ɑ̂ et ê pouvaient se trouver en cette position. Les voyelles " \
                       "nasalisées ẽ et ë s'abaissent immédiatemment et fusionnent avec ɑ̨̄ et ɑ̨̂."
    sources = ["PGL"]
    motif = re.compile("[ȧạậiuēīê]n$")
    règle_remplacement = {"ȧn": "ả", "in": "į", "un": "ų", "ạn": "à", "īn": "ĩ", "ēn": "à", "ên": "ȁ", "ận": "ȁ"}


class Traitement_schwa(ChangementPhonétique):
    motif = re.compile("(?P<avant>.|^)?(?P<schwa>[əƏ])(?P<apres>.|$)?")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes["schwa"].isupper() or \
                any(map(lambda env: env.lower() in list("ȧeiuạēīūậêûảįųàĩȁ"), dict_de_groupes.groupdict())):
            voy = "ȧ" if dict_de_groupes["schwa"].islower() else "Ȧ"
        else:
            voy = ""
        return (dict_de_groupes["avant"] or "") + voy + (dict_de_groupes["apres"] or "")




class Perte_t_FinalInaccentué(ChangementPhonétique):
    motif = re.compile("((?<=[ȧeiuạēīūậêûảįųàĩȁ])|(?<=[ȧeiuạēīūậêûảįųàĩȁ][nj]))t$")


class Désobstruation_gw(ChangementPhonétique):
    motif = re.compile("(?<!n)ǥʷ")
    règle_remplacement = "w"


class Élévation_a_Long(ChangementPhonétique):
    motif = re.compile("(?i:[ạậàȁ])")
    règle_remplacement = {"ạ": "ọ", "ậ": "ộ", "à": "ò", "ȁ": "ȍ"}


class MutationEn_i(ChangementPhonétique):
    motif = re.compile("[Ee][ij]|[Ee](?=.+[ij])")
    règle_remplacement = {"ei": "ī", "Ei": "Ī", "ej": "ī", "Ej": "Ī", "e": "i", "E": "I"}


class UmlautEn_z(ChangementPhonétique):
    motif = re.compile("[eE](?=z)")
    règle_remplacement = {"e": "i"}


class Élévation_e_DevantNasalePuisConsonne(ChangementPhonétique): # en fait devant une nasale tautosyllabique, donc pas streng$
    motif = re.compile("[eE](?=[nm](?i:[^ȧeiuēīọūêộảįųĩòȍ]+[ȧeiuēīọūêộảįųĩòȍ]))")
    règle_remplacement = {"e": "i"}


class Perte_y_Intervocalique(ChangementPhonétique):
    motif = re.compile("(?i:(?P<avant>[ȧeiuēīọūêộảįųĩòȍ])j(?P<apres>[ȧeiuēīọūêộảįųĩòȍ]))")

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        if dict_de_groupes["avant"][0].lower() != dict_de_groupes["apres"][0]: # hiatus
            return dict_de_groupes["avant"] + dict_de_groupes["apres"] # = dipthongue
        else:
            return {"ȧ": "ạ", "Ȧ": "Ạ", "e": "ē", "E": "Ē", "u": "ū", "U": "Ū"}.get(dict_de_groupes["avant"])
            # ^ laisser le dict min / maj sauf si on sait ce qu'on fait




class NasalisationCompensatriceDevant_nh(ChangementPhonétique): # Tardif !
    motif = re.compile("[ȧiuȦIU]n(?=ꝁ)")
    règle_remplacement = {"ȧn": "à", "in": "ĩ", "un": "ũ",
                          "Ȧn": "À", "In": "Ĩ", "Un": "Ũ"}


# Très moche !
class LoiDeMalhow_PGERM(ChangementPhonétique): # Tardif dans le schéma traditionnel
    nom = "Loi de Malhow"
    description = "La diphtongue longue ɔ̄u se simplifie en la diphtongue ɑu en finale ou dans une syllabe" \
                       "fermée, en la voyelle longue ɔ̄ dans une syllabe ouverte."
    sources = ["Etymological dictionary of Proto-Germanic - a sneak preview: Kroonen"]
    motif = re.compile("(?i:ọu)(?=(?P<apres>$|..?))") # suivi de fin, une, ou deux lettres

    @classmethod
    def règle_remplacement(cls, dict_de_groupes):
        séquence = dict_de_groupes["apres"]
        # si syllabe ouverte et pas finale (au moins une lettre après, et si deux lettres au moins une des deux est une voyelle)
        if len(séquence) == 1 or (len(séquence) == 2 and (séquence[0].lower() in list("ȧeiuạēīọūêộảįųĩàòȍ") or
                                                          séquence[1].lower() in list("ȧeiuạēīọūêộảįųĩàòȍ"))):
            return {"ọu": "ọ"}.get(dict_de_groupes.group())
        # si syllabe fermée et finale (aucune lettre après ou deux lettres sans voyelle)
        else:
            return {"ọu": "ȧu"}.get(dict_de_groupes.group())


# ATTENTION ! Devrait en principe contenir les géminées tôtives !
class OcclusionsDiverses(ChangementPhonétique):
    nom = "Occlusions diverses"
    description = "Les fricatives sonores gagnent une occlusion dans certains environnements : à l'initiale " \
                  "(ƀ et đ), géminées (ƀƀ, đđ et ǥǥ) derrière une consonne homoganique (mƀ, nđ, ŋǥ et ŋʷǥʷ) et " \
                  "derrière l, z et (sauf vieux norrois) r pour đ."
    sources = ["PGL"]
    motif = re.compile("^[đƀ]|(?<=m)ƀ|(?<=n)[đǥ]|(?<=[lzr])đ")
    règle_remplacement = {"ƀ": "b", "đ": "d", "ǥ": "g"}


class AjustementsTemporaires(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        forme_phono = forme_phono.translate(str.maketrans("ʷ", "w"))
        # ^ reste des labiovélaires ^ #
        forme_phono = re.sub(re.compile("(?<=[ȧeiuạēīọūêộảįųĩàòȍ])s$"), "z", forme_phono)
        # ^ analogie s final => z final ^ #
        forme_phono = re.sub("(?P<avant>[ȧeiuạēīọūêộảįųĩàòȍ])(?P<x>w(?![jw])|j(?!j))(?![ȧeiuạēīọūêộảįųĩàòȍ])",
                             lambda semi: semi.group("avant") + {"w": "u", "j": "i"}.get(semi.group("x")), forme_phono)
        forme_phono = re.sub("(?P<avant>[ȦEIUẠĒĪỌŪÊỘẢĮŲĨÀÒȌ])(?P<x>[uw](?![jw])|[ij](?!j))(?![ȧeiuạēīọūêộảįųĩàòȍ])",
                             lambda semi: semi.group("avant") + {"u": "U", "w": "U", "i": "I", "j": "I"}.get(semi.group("x")), forme_phono)
        # ^ création des diphtongues ^ #
        forme_phono = forme_phono.translate(str.maketrans("ēĒêÊ", "ẹẸệỆ"))
        # ^ transformation des ē/ê fermés en leurs équivalents ouverts, normalement un ē fermé devrait rester mais ^ #
        # ^ dans des conditions pas claires ^ #
        return forme_phono


évolution = [
    # PIE > EARLY PGERM
    Centumisation,
    Épenthèse,
    AssimilationObstruantes,
    RaccourcissementGéminées,
    SurélongationVoyellesLonguesFinales,
    LoiDeCowgill,
    LoiDeHoltzmann,
    MutationLaryngales,
    LoiDeDybo,  # doit se trouver après mutations laryngales et avant déplacement accent à l'intiiale
    Délabialisation,

    # EARLY > LATE PGERM
    PerteVoyellesCourtesFinales,
    MutationConsonnantiqueGermanique1,
    LoiDeKluge,
    MutationConsonnantiqueGermanique2,
    LoiDeVerner,
    RelocalisationLabioVélaireInitiale,
    DéplacementAccent,
    Traitement_schwa,  # déplacer après dentalisation m devant dentales explique samədos > sandaz
                                      # avant assimil div explique fulənos > fullaz
                                      # mais l'un et l'autre foire kurənom > kurną...
    AssimilationsDiverses,
    RaccourcissementGroupeowo,
    Recul_ew,
    Élévation_e,
    Raccourcissement_yi,
    Fusion_o_a,

    # LATE PGERM > PGERM
    Dentalisation_m_Final,
    Dentalisation_m_DevantDentales,
    PerteNasalisatrice_n_FinalAtone,
    Perte_t_FinalInaccentué,
    Désobstruation_gw,
    Élévation_a_Long,
    MutationEn_i,
    UmlautEn_z,
    Élévation_e_DevantNasalePuisConsonne,
    Perte_y_Intervocalique,
    NasalisationCompensatriceDevant_nh,  # convention graphique n'en tient pas compte
    OcclusionsDiverses,

    # PGERM
    AjustementsTemporaires,
]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée
