from recherche import obt_lexique as o_m, rech_lexique as r_m

base = "Proto-Indo-European"

# TODO - intégrer la recherche par athématique, protéro, hystéro, statif, perfectif, etc.
caches_pages = dict.fromkeys(
    [
        "lemmes",
        "adjectifs",
        "verbes",
        "adverbes",
        "conjonctions",
        "déterminants",
        "interjections",
        "noms",
        "numéraux",
        "préfixes",
        "suffixes",
        "racines",
     ],
    [])


def obt_lexique(cible="lemmes"):
    return o_m(base, cible, caches_pages=caches_pages)


def rech_lexique(motif, cible="lemmes"):
    motif = motif.translate(str.maketrans({
        "ḷ": "l̥", "ṃ": "m̥", "ṇ": "n̥", "ṛ": "r̥",
        "Ḷ": "ĺ̥", "Ṃ": "ḿ̥", "Ṇ": "ń̥", "Ṛ": "ŕ̥",
    }))
    return r_m(motif=motif, fonc_rappel=obt_lexique, cible=cible)
