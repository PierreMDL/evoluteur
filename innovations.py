import re


class Innovation:
    nom = None
    description = None
    chronologie = None
    sources = None
    motif = re.compile("^$")  # matche rien
    règle_remplacement = ""

    @classmethod
    def appliquer(cls, forme_phono, info=None) -> str:
        pass


class ChangementPhonétique(Innovation):
    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        assert (type(forme_phono) is str), TypeError(type(forme_phono))
        if type(cls.règle_remplacement) is dict:

            def est_accentué(res):
                if res.group().isupper() and res.group() not in cls.règle_remplacement.keys():
                    return cls.règle_remplacement.get(res.group().lower()).upper()
                    # ^ si la clé de la maj n'est pas donnée dans le dict, l'impliquer
                else:
                    return cls.règle_remplacement.get(res.group())
            # ^ permet de se passer de transcrire un dict de remplacement en maj en cas d'accentuation

            forme_phono, changements = re.subn(cls.motif, est_accentué, forme_phono)
        else:
            forme_phono, changements = re.subn(cls.motif, cls.règle_remplacement, forme_phono)
        return forme_phono


class DéplacementAccent(Innovation):
    @classmethod
    def appliquer(cls, forme_phono: str, info=None) -> str:
        nouvel_accent = re.search(cls.motif, forme_phono.lower())
        if nouvel_accent:
            forme_phono = forme_phono.lower()
            forme_phono = forme_phono[:nouvel_accent.start()] + nouvel_accent.group().upper() + forme_phono[nouvel_accent.end():]
            changement = True
        else:
            changement = False
        return forme_phono


"""
    Innovations communes
"""


class Centumisation(ChangementPhonétique):
    motif = re.compile("[ḱǵ]")
    règle_remplacement = {"ḱ": "k", "ǵ": "g"}
    nom = "Centumisation"
    description = "Les consonnes palato-vélaires perdent leur palatalisation et éventuellement fusionnent avec les " \
                  "vélaires."
