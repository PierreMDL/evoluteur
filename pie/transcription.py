import re
from transcription import syllabifier as base_syllabifier


def régexiser(entrée: str) -> str:
    entrée = entrée.translate(str.maketrans("0123", "₀₁₂₃"))
    # ^ numéros des laryngales en indice, convention graphique des laryngales
    entrée = re.sub("(?=[gk])w|(h(?![̥₀₁₂₃]))", lambda h_w: {"h": "ʰ", "w": "ʷ"}.get(h_w.group()), entrée)
    # ^ w en exposant si g ou k précèdent, h si numéro ne suit pas : conv graphique des labio-vélaire et aspirées
    entrée = re.sub("H(?![₀₁₂₃])", "h₀", entrée)
    # ^ H pas suivi d'un numéro = laryngale de nature inconnue ; H suivi d'un numéro = laryngale accentuée
    entrée = re.sub("(?i:m̥|n̥|l̥|r̥|h̥|ḿ̥|ń̥|ĺ̥|ŕ̥|h̥́)", lambda syll: {"m̥": "ṃ", "n̥": "ṇ", "l̥": "ḷ", "r̥": "ṛ", "h̥": "ḥ",
                                                         "M̥": "Ṃ", "N̥": "Ṇ", "L̥": "Ḷ", "R̥": "Ṛ", "H̥": "Ḥ"
                                                         }.get(syll.group()), entrée)
    entrée = re.sub("(?i:(?<![aeiouáéíóúēōḗṓywṃṇḷṛ])([mnlr])(?![aeiouáéíóúēōḗṓywṃṇḷṛḥ]))",
                    lambda réson: {"m": "ṃ", "n": "ṇ", "l": "ḷ", "r": "ṛ",
                                   # "h₀": "ḥ₀", "h₁": "ḥ₁", "h₂": "ḥ₂", "h₃": "ḥ₃",
                                   "M": "Ṃ", "N": "Ṇ", "L": "Ḷ", "R": "Ṛ", "H": "Ḥ",
                                   # "H₀": "Ḥ₀", "H₁": "Ḥ₁", "H₂": "Ḥ₂", "H₃": "Ḥ₃",
                                   }.get(réson.group()), entrée)
    # ^ implication des consonnes syllabique si pas proximité avec une voyelle (ou semi-voyelle)

    entrée = entrée.translate(str.maketrans("áéíóúḗṓy", "AEIOUĒŌj"))
    entrée = re.sub("(ḿ̥|ń̥|ĺ̥|ŕ̥|h̥́|m̥|n̥|l̥|r̥|h̥)", lambda syll: {"ḿ̥": "Ṃ", "ń̥": "Ṇ", "ĺ̥": "Ḷ", "ŕ̥": "Ṛ", "h̥́": "Ḥ",
                                                                          "m̥": "ṃ", "n̥": "ṇ", "l̥": "ḷ", "r̥": "ṛ", "h̥": "ḥ"
                                                                          }.get(syll.group()), entrée)
    # ^ remplacement des consonnes syllabiques avec ronds souscrits (deux caractères unicode) par équivalent avec
    # ^ points souscrits (un caractère unicode) et des voyelles accentuées par des majuscules (plus simples à
    # ^ l'utilisation
    return entrée


def transcrire(entrée: str) -> str:
    entrée = re.sub("(?i:[ṃṇḷṛḥ])", lambda syll: {'ṃ': 'm̥', 'ṇ': 'n̥', 'ḷ': 'l̥', 'ṛ': 'r̥', "ḥ": "h̥",
                                                    'Ṃ': 'M̥', 'Ṇ': 'N̥', 'Ḷ': 'L̥', 'Ṛ': 'R̥', "Ḥ": "H̥"
                                                  }.get(syll.group()), entrée)
    # ^ rond souscrit = convention graphique des consonnes syllabiques

    entrée = re.sub("[AEIOUĒŌ]|M̥|N̥|L̥|R̥|H̥", lambda maj: {"A": "á", "E": "é", "I": "í", "O": "ó", "U": "ú",
                                                           "Ē": "ḗ", "Ō": "ṓ",
                                                           "M̥": "ḿ̥", "N̥": "ń̥", "L̥": "ĺ̥", "R̥": "ŕ̥", "H̥": "h̥́"
                                                             }.get(maj.group()), entrée)
    # ^ représentation des voyelles accentuées avec accents aigus
    entrée = entrée.replace("j", "y")
    return entrée


def syllabifier(valeur: str) -> list[dict]:
    noyaux = [
        # ATONES
        "a", "e", "i", "o", "u",
        "ā", "ē", "ī", "ō", "ū",
        "ej", "oj", "je", "jo",
        "ḷ", "ṛ", "ṃ", "ṇ",
        "h₁", "h₂", "h₃", "h₀",

        # ACCENTUÉE
        "A", "E", "I", "O", "U",
        "Ā", "Ē", "Ī", "Ō", "Ū",
        "Ej", "Oj", "jE", "jO",
        "Ḷ", "Ṛ", "Ṃ", "Ṇ",
        "H₁", "H₂", "H₃", "H₀",
    ]
    return base_syllabifier(valeur, noyaux)
