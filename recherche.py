from mwclient import Site
import re


# TODO - connexion établie
user_agent = "Évoluteur/2.0 (pierre.simon.mdl@gmail.com)"
host = "en.wiktionary.org"
site = None


def connecter_site():
    global site
    return site or Site(host=host, clients_useragent=user_agent)


correspondances_parties = {
    "lemmes": "lemmas",
    "adjectifs": "adjectives",
    "verbes": "verbs",
    "adverbes": "adverbs",
    "conjonctions": "conjunctions",
    "déterminants": "determiners",
    "interjections": "interjections",
    "noms": "nouns",
    "numéraux": "numerals",
    "prépositions": "prepositions",
    "noms propres": "proper_nouns",
    "préfixes": "prefixes",
    "suffixes": "suffixes",
    "racines": "roots",
}


def obt_liste_pages(base, cible="lemmes", caches_pages=None):

    if caches_pages is None:
        caches_pages = {}

    if cible not in caches_pages.keys():
        return []  # la catégorie n'existe pas pour cette langue

    if not caches_pages[cible]:
        titre_catégorie = base + "_" + correspondances_parties[cible]
        catégorie = connecter_site().categories[titre_catégorie]
        générateur_catégorie = catégorie.members()  # c'est ça qui charge
        caches_pages[cible] = list(générateur_catégorie)

    return caches_pages[cible]


def obt_lexique(base, cible="lemmes", caches_pages=None):

    def extraire_mot_du_titre(name):
        if not name.startswith("Reconstruction:"):  # il s'agit d'une page de reconstruction (≠ Category:)
            return
        return name.split("/")[-1]

    def extraire_et_filtrer_mot_du_titre(name):
        word = extraire_mot_du_titre(name)
        if word and not (" " in word) and not ("-" in word):  # pas un mot composé, pas une racine ou un affixe
            return word
        return

    if liste_pages := obt_liste_pages(base, cible, caches_pages):
        fonc_extraire = extraire_et_filtrer_mot_du_titre if cible == "lemmes" else extraire_mot_du_titre
        return list(filter(None, map(lambda page: fonc_extraire(page.name), liste_pages)))
    else:
        return []


def rech_lexique(motif, fonc_rappel, cible):
    lexique = fonc_rappel(cible=cible)
    return [mot for mot in lexique if re.search(motif, mot)]


correspondances_abréviations = {
    "VANGL": "ang",
    "MANGL": "enm",
    "ANGL": "en",
    "VHA": "goh",
    "VISL": "non",
    "ISL": "is",
}

corres_reverse = {k: v for v, k in correspondances_abréviations.items()}


# FIXME - Ça ne fonctionne pas avec les templates desctree de wiktionary, qu'il faudrait développer (lourd)
#  Autant utiliser beautifulsoup directement ?
def obt_descendants(motif, langues, base, cible="lemmes", caches_pages=None):
    assert type(langues) is list  # sinon ça bogue grave

    liste_pages = obt_liste_pages(base, cible, caches_pages)
    res = []

    for page in liste_pages:
        if not page.name.startswith("Reconstruction:"):  # il s'agit d'une page de reconstruction (≠ Category:)
            pass
        elif not re.search(motif, page.name.split("/")[-1]):
            pass
        else:
            mot = page.name.split("/")[-1]
            print(mot)
            first_part = "{{desc[|](?P<lang>"
            middle_part = "|".join([correspondances_abréviations[langue] for langue in langues])  # TODO - capter KeyValue, doublons
            last_part = ")[|](?P<desc>[^|}]+)(?P<extra>[|].+)?}}"
            motif_desc = re.compile(first_part + middle_part + last_part)
            print(motif_desc)
            matches = re.finditer(motif_desc, page.text())
            dict_réponses = {}

            for match in matches:
                lang, desc, extra = match.group("lang", "desc", "extra")
                dict_réponses.update({corres_reverse[lang]: desc})  # TODO - Potentiellement plusieurs réponses, la dernière écrase toutes les autres !

            if len(dict_réponses.keys()) > 0:  # TODO - trouver plus beau ?
                res.append((mot, dict_réponses))

    return res

# TODO - implé
# obtenir prononciation => str ?

