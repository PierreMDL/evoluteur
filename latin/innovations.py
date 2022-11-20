from innovations import ChangementPhonétique
import re


### IMPORTÉ DEPUIS OGERM ###

# Similaire (mais relié ?) à la rhotacisation du VISL
class Rhotacisation(ChangementPhonétique):
    nom = "Rhotacisation"
    description = "Changement du z en r."
    sources = ["PHE"]
    motif = re.compile("z")
    règle_remplacement = "r"

###


class AjustementsTemporaires(ChangementPhonétique):
    motif = re.compile("(?<!l)l(?![iīl])")
    règle_remplacement = "ɫ"
    # ^ création du l pinguis


class LoiDExon(ChangementPhonétique):
    nom = "Loi d'Exon"
    description = "La loi d'Exon décrit la syncope de la première de deux syllabes médiales légères (voyelle courte " \
                  "+ consonne simple)."
    sources = ["HL"]
    motif = re.compile("[aeiouə](?=[^aeiouāēīōūə][aeiouə][^aeiouāēīōūə][aeiouāēīōūə])")
    # ^ après la voyelle accentuée : une voyelle courte, suivie d'une consonne, suivie d'une voyelle courte, suivie
    # ^ d'une consonne, suivie d'une voyelle


# prend potentiellement rdis, que la source ne mentionne pas, mais en même temps j'ai pas trouvé de -ndis à la main...
class SyncopeApresGroupesConsonnes(ChangementPhonétique):
    nom = "Syncope après certains groupes de consonnes"
    description = "Une syncope du i désinentiel survient dans les groupes -ntis, -ndis, rtis."
    sources = ["HL"]
    motif = re.compile("(?<=[rn][dt])i(?=s)")



class Assimilations(ChangementPhonétique):
    motif = re.compile("((?i:(?<=^)|(?<=[aeiouāēīōū])|(?<=[aeiouāēīōū][nr])))(m[sgrk]|b[kr]|d[kt]|s[mn]k?|ksf|[td]s|np|sd|gs|(?<=^)(gn|w[lɫ]))")
    règle_remplacement = {"ms": "ns", "mg": "ng", "mr": "rr", "mk": "nk",
                          "bk": "kk", "br": "rr", "dk": "kk",
                          "dt": "tt", "ts": "ss", "ds": "ss",
                          "sm": "m", "ksm": "m", "sn": "n", "ksn": "n", "ksf": "kf", "sd": "d",
                          "np": "mp", "gs": "ks", "smk": "nk",
                          "gn": "n", "wl": "l", "wɫ": "ɫ"}  # seulement à l'initiale (wl seul exemple: wlāna > lāna)


# évidemment pour ex > ē, mais aussi pour louksna > lūna, même si allongement évidemment ne concerne pas les diphtongues
class Assimilation_ks_DevantConsonne(ChangementPhonétique):
    motif = re.compile("(?i:(?<![aeiou])[aeiou])?ks(?=[^aeiouāēīōū])")
    règle_remplacement = {"aks": "ā", "eks": "ē", "iks": "ī", "oks": "ōks", "uks": "ū",
                          "Aks": "Ā", "Eks": "Ē", "Iks": "Ī", "Oks": "Ōks", "Uks": "Ū", "ks": ""}



# "parfois initial": tris > ter,
# parti pris : voyelle courte atone derrière syllabe courte tonique (deux consonnes homorganiques acceptées)
# problèmes posés : feros !> fers, swekuros !> sokerus cf dossier discussions
class SyncopePuisÉpenthèse_l_r(ChangementPhonétique):
    nom = "Syncope puis épenthèse autour de l et r"
    description = "Une voyelle courte suivant l ou r disparaît, puis un ə épenthétique apparaît devant éventuellement."
    sources = ["HL"]
    motif = re.compile("(?<![AEIOUw])[AEIOU]([^aeiouāēōū]|nd|mb|ng)?((?<!ɫ)ɫ|(?<!l)l|(?<!r)r)[aeiouə](?![aeiou]|[^aeiouāēīōū]{2,}|$)")

    @classmethod
    def règle_remplacement(cls, candidat):
        if len(candidat.group()) == 3:
            para = candidat.group()[:-1]
        else:
            para = candidat.group()[:-2] + "ə" + candidat.group()[-2]
        return para.replace("l", "ɫ")




#  "Late PITAL", rajouté si un r précédent pour assimilation
class Zétacisation(ChangementPhonétique):
    nom = "Zétacisation"
    description = "Le s intervocalique devient sonore."
    motif = re.compile("(?i:(?<=[aeiouāēīōūər])s(?=[aeiouāēīōūə]))")
    règle_remplacement = "z"


class Débuccalisation(ChangementPhonétique):
    nom = "Débuccalisation"
    description = "La vélaire fricative sourde ꝁ se débuccalise vers h ; la vélaire fricative sonore intervocalique" \
                  " se débuccalise vers ɦ."
    sources = ["PIL"]
    motif = re.compile("ꝁ|(?i:(?<=[aeiouāēīōūə])ǥ(?=[aeiouāēīōūə]))")
    règle_remplacement = {"ꝁ": "h", "ǥ": "ɦ"}


# Prémisces tout de même étranges. dw > b et maintenant du > b, tl > kl et maintenant dl > bl, dr > br et plus tôt
# ŧ > f partout... N'empêche, r et l sont les deux consonnes syllabiques qui produisent un o épenthétique
# attention, virer le o quand on aura implémenté chgt des voyelles !
# rajouté le o (> u), si on place cette reloc après réduction atone, on pourra le virer
class Relocalisation_d_En_b_Devant_r_u_l(ChangementPhonétique):
    nom = "Relocalisation de đ en ƀ devant r, u ou l"
    description = "La consonne fricative dentale sonore đ se relocalise en bilabiale devant r, u ou l."
    sources = ["HL"]
    motif = re.compile("đ(?=[roulɫ])")
    règle_remplacement = "ƀ"


class OcclusionBuccalesSonores(ChangementPhonétique):
    nom = "Occlusion des buccales fricatives sonores"
    description = "Les consonnes fricatives sonores buccales (excluant ɦ) gagnent une occlusion : ƀ devient b, ð " \
                  "devient d, ǥ devient g."
    sources = ["PIL"]
    motif = re.compile("[ƀđǥ]")
    règle_remplacement = {"ƀ": "b", "đ": "d", "ǥ": "g"}


class Traitement_dw_gw(ChangementPhonétique):
    nom = "Traitement des groupes dʷ et gʷ"
    description = "Le groupe dʷ se relocalise en b ; le groupe gʷ, sauf suivant n, perd son obstruation. Cela concède " \
                  "au latin un certain nombre de b là où le proto-indo-européen n'en montrait que de rares."
    sources = ["PIL"]
    motif = re.compile("dʷ|(?<!n)gʷ")
    règle_remplacement = {"dʷ": "b", "gʷ": "w"}


# J'en profite pour mettre les θ, and χʷ > f qu'on ne sait pas trop s'ils avaient survécu jusqu'ici
class Relocalisation_phi_En_f(ChangementPhonétique):
    nom = "Relocation de ꝑ en f"
    description = "La consonne fricative bilabiale sourde se relocalise en labio-dentale."
    sources = ["HL"]
    motif = re.compile("[ꝑŧ]|[hꝁ]ʷ")
    règle_remplacement = "f"


class ReculGroupe_we_Accentué(ChangementPhonétique):
    nom = "Recul des groupes swe ou we + labiales accentués"
    description = "Les groupes accentués (c'est-à-dire à l'initiale) swe-, ou we- suivi d'une consonne labiale ou d'un " \
                  "l pinguis (non suivi d'un i ou d'un autre l), reculent en so-, ou wo."
    sources = ["HL"]
    motif = re.compile("(?<=s)wE|(?<=w)E(?=[mbpɫ])")
    règle_remplacement = {"wE": "O", "E": "O"}


# ^en- toujours élevé en ^in-, doit arriver avant assimilation pour que enreverēns > inreverēns > irreverēns
class Élévation_e_Devant_ng_nk_gn(ChangementPhonétique):
    nom = "Élévation du e devant ŋ"
    description = "Le e tonique s'élève en i devant la consonne ŋ, donc devant les groupes -ng-, -nk- et -gn-."
    sources = ["HL"]
    motif = re.compile("^[EƏ](?=n)|[EƏ](?=ng|nk|gn)")
    règle_remplacement = {"E": "I", "Ə": "I"}


# ATT devrait peut-être prendre en compte longues diphtongues āi, ēi, ōi (slt désinentielles ?)
class RéductionVocaliqueAtone(ChangementPhonétique):
    nom = "Réduction vocalique atone"
    sources = ["HL"]

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        # TRANSFORMATION DIPHTONGUES #
        motif_dipht_1 = re.compile("(?i:eiw?|ou)")
        règle_dipht_1 = {"ei": "ī", "eiw": "īw", "EI": "Ī", "EIw": "E", "ou": "ū", "OU": "Ū"}
        forme_phono = re.sub(motif_dipht_1, lambda candidat: règle_dipht_1.get(candidat.group()), forme_phono)
        # ^ wiki dit que ei > ẹ̄, ou > ọ̄ (plus hautes que ē, ō), mais est-ce que ē, ō se seraient en fait pas abaissées ?
        # ^ EIw > Ēw, ok, mais apparemment seulement si voyelle postérieure derrière: deiwos > deus, deiwoi > dīi
        # ^ "The late Old Latin form *dẹ̄vos regularly lost its -v- before a rounded vowel" (wikt deus)

        motif_dipht_2 = re.compile("ai|AI|au")
        règle_dipht_2 = {"ai": "ī", "AI": "AE", "au": "ū"}
        forme_phono = re.sub(motif_dipht_2, lambda candidat: règle_dipht_2.get(candidat.group()), forme_phono)
        # ^ au médial rarement "oe"

        motif_dipht_3 = re.compile("(?i:oi|OI)(?=(?P<voyelle>.*[aeiouāēīōūə])?)")
        def règle_dipht_3(candidat):
            if candidat.group("voyelle"):
                return "ū"
            else:
                return "ī"
        forme_phono = re.sub(motif_dipht_3, règle_dipht_3, forme_phono)
        # ^ oi > oe > ū, sauf exceptions (poena, foedus), oi > ī en mono

        # Normalement à ce niveau-là il n'y a plus de diphtongues à part au, ae, oe

        # TRANSFORMATION VOYELLES COURTES MÉDIALES #
        motif_med_dvt_lrw = re.compile("(?<![ao])[aeiouə][ɫrw](?=.*[aeiouāēīōūə])")
        règle_med_dvt_lrw = {"ar": "er", "ir": "er", "or": "er", "ur": "er", "er": "er", "ər": "er",
                             "aɫ": "oɫ", "iɫ": "oɫ", "oɫ": "oɫ", "uɫ": "oɫ", "eɫ": "oɫ", "əɫ": "oɫ",
                             "aw": "uw", "iw": "uw", "ow": "uw", "uw": "uw", "ew": "uw", "əw": "uw"}
                             # attention : "in which case the /w/ is not written"

        forme_phono = re.sub(motif_med_dvt_lrw, lambda candidat: règle_med_dvt_lrw.get(candidat.group()), forme_phono)
        # ^ médiales courtes devant ɫ, r, w

        motif_med_dvt_l_ping = re.compile("(?<![aeiouāēīōūə])oɫ(?=.*[aeiouāēīōūə])")
        forme_phono = re.sub(motif_med_dvt_l_ping, "uɫ", forme_phono)
        # ^ ol médial continue son chemin vers ul sauf s'il suit une voyelle

        motif_med_dvt_CV = re.compile("(?<![ao])[aeiouə](?=[^aeiouāēīōūɫrw]j?[aeiouāēīōūə])") # refakjō > reficiō, le j compte pas comme une consonnne
        forme_phono = re.sub(motif_med_dvt_CV, "i", forme_phono)
        # ^ médiales courtes devant une de toutes les autres consonnes + voyelle : devient i
        # ^ Variation between i and (often earlier) u is common before a single labial consonant (p, b, f, m), underlyingly the sonus medius vowel
        # ^ "But they sometimes become e [...] when immediately following a vowel"

        motif_med_dvt_CC = re.compile("(?<![ao])[aeiouə](?=[^aeiouāēīōūɫrw][^aeiouāēīōūə].*[aeiouāēīōūə])")
        règle_med_dvt_CC = {"a": "e", "e": "e", "i": "i", "o": "u", "u": "e", "ə": "e"}
        forme_phono = re.sub(motif_med_dvt_CC, lambda candidat: règle_med_dvt_CC.get(candidat.group()), forme_phono)
        # ^ médiales courtes devant une de toutes les autres consonnes + consonne : a, e, u > e, o > u, i > i


        # TRANSFORMATION VOYELLES COURTES FINALES #
        motif_fin_dvt_C = re.compile("(?<![ao])[aeiouə](?=[^aeiouāēīōūmn]$)")
        règle_fin_dvt_C = {"a": "i", "e": "i", "i": "i", "o": "u", "u": "u", "ə": "i"}
        forme_phono = re.sub(motif_fin_dvt_C, lambda candidat: règle_fin_dvt_C.get(candidat.group()), forme_phono)
        # ^ finales courtes devant une simple consonne finale (outre nasales)

        motif_fin_dvt_CC = re.compile("(?<![ao])[aeiouə](?=[mn]$|[^aeiouāēīōū]{2,}$)")
        règle_fin_dvt_CC = {"a": "e", "e": "e", "i": "e", "o": "u", "u": "u", "ə": "e"}
        forme_phono = re.sub(motif_fin_dvt_CC, lambda candidat: règle_fin_dvt_CC.get(candidat.group()), forme_phono)
        # ^ finales courtes devant un groupe de consonnes ou une simple nasale

        forme_phono = re.sub(re.compile("(?<![aoi])[aeiouə]$"), "e", forme_phono)
        # ^ courtes absolument finales, rajouté !ia$ pour suffixe d'origine grec -ía (GR sikilía > LAT sicilia)

        # RACCOURCISSEMENT VOYELLES LONGUES FINALES
        motif_fin_longues = re.compile("[āēīōū](?!s)(?=[^aeiouāēīōū]+$)")
        règle_fin_longues = {"ā": "a", "ē": "e", "ī": "i", "ō": "o", "ū": "u"}
        forme_phono = re.sub(motif_fin_longues, lambda candidat: règle_fin_longues.get(candidat.group()), forme_phono)
        # ^ finales longues sauf devant s

        forme_phono = re.sub(re.compile("ā$"), "a", forme_phono)
        # ^ le ā absolument final est le seul à se raccourcir

        return forme_phono


# PHL y fait référence, complété par wikt infīnītus > īnfīnītus, infernus > īnfernus, etc.
class ÉlongationDevant_ns_nf(ChangementPhonétique):
    nom = "Élongation des voyelles devant les groupes -ns et -nf-"
    description = "Les voyelles suivies de n puis une fricative (en latin s et f) s'allongent."
    sources = ["PHL"]
    motif = re.compile("(?i:[aeiou])(?=n[sf])")
    règle_remplacement = {"a": "ā", "e": "ē", "i": "ī", "o": "ō", "u": "ū"}


class Traitement_dw_Init(ChangementPhonétique):
    nom = "Traitement du groupe dw- initial"
    description = "Le groupe dw- à l'initiale devient -b"
    sources = ["HL"]
    motif = re.compile("^d[wu](?=[aeiouāēīōū])")
    règle_remplacement = "b"


# indiqué comme plutôt PITAL, mais pas trouvé d'exemple PIE VyV > PITAL VV alors que nombreux PITAL VjV > LATIN VV
class Perte_j_Intervocalique(ChangementPhonétique):
    motif = re.compile("(?i:(?<=[aeiouāēīōūə]))j(?=[aeiouāēīōūə])")


class AjustementsTemporaires2(ChangementPhonétique):

    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        forme_phono = re.sub("[rs]s", lambda candidat: {"ss": "s", "rs": "r"}.get(candidat.group()), forme_phono)
        # ^ ss > s, rs > s notamment après une métathèse / syncope agros > agers > ager

        forme_phono = re.sub("(?<!j)[uU]w|ʷ[uU]", lambda cand: {"uw": "u", "Uw": "U", "ʷu": "u", "ʷU": "U"}.get(cand.group()), forme_phono)
        # ^ raccourcissement uw > u
        # ^ kwu > ku mais pas cerwus !> cerus, ensuite des fois ku > kwu par analogie (ecus > equus, anticus > antiquus)

        forme_phono = re.sub("(?i:(?<=[^aeiouāēīōūkr])w(?=[aeiouāēīōū]))", "u", forme_phono)

        forme_phono = re.sub("[āĀ]ō|[ēĒ]ō", lambda cand: {"āō": "ō", "Āō": "Ō", "ēō": "eō", "Ēō": "EŌ"}.get(cand.group()), forme_phono)
        # ^ résolution des diphtongues survenant par ex suite à la suppression d'un j intervocalique

        forme_phono = forme_phono.replace("ʷ", "")
        # ^ qu'est-ce qu'ils foutent encore là ?

        return forme_phono


évolution = [
    AjustementsTemporaires,
    Relocalisation_d_En_b_Devant_r_u_l,  # ajouté o provisoirement, penser à le virer !
    SyncopeApresGroupesConsonnes,
    Élévation_e_Devant_ng_nk_gn,
    Assimilation_ks_DevantConsonne,  # mon initiative
    LoiDExon,  # a dû se produire avant zétacisation pour que magisemos > maksimus
    Assimilations,
    SyncopePuisÉpenthèse_l_r,
    Zétacisation,
    Débuccalisation,
    OcclusionBuccalesSonores,
    Traitement_dw_gw,
    Rhotacisation,  # Très commun, donc je le pique au OGERM
    Relocalisation_phi_En_f,  # vraiment ? wiki "Latin classique" semble dire que non...
    ReculGroupe_we_Accentué,
    RéductionVocaliqueAtone,
    ÉlongationDevant_ns_nf,
    Traitement_dw_Init,
    Perte_j_Intervocalique,
    AjustementsTemporaires2
]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation.appliquer(entrée)
    return entrée
