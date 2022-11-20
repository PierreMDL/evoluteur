from recherche import obt_lexique as o_m, rech_lexique as r_m

base = "Proto-West_Germanic"

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
        "prépositions",
        "noms propres",
        "préfixes",
        "suffixes",
     ],
    [])


def obt_lexique(cible="lemmes"):
    return o_m(base, cible, caches_pages=caches_pages)


def rech_lexique(motif, cible="lemmes"):
    return r_m(motif=motif, fonc_rappel=obt_lexique, cible=cible)
