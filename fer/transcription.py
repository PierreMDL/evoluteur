import re


def resolve_vowels(match) -> str:

    if match:
        corres = {
            "a": "a", "e": "ɛ", "i": "ɪ", "o": "ɔ", "u": "ʊ", "y": "ʏ", "ø": "œ",
            "á": "ɔ", "í": "ʊi", "ó": "ɔ", "ú": "ʏ", "æ": "ɛ",
            "ei": "ai", "ey": "ɛ", "oy": "ɔi"
        }

    else:
        corres = {
            "a": "ɛa", "e": "e", "i": "i", "o": "o", "u": "u", "y": "y", "ø": "ø",
            "á": "ɔa", "í": "ʊi", "ó": "œu", "ú": "ʉu", "æ": "e",
            "ei": "ai", "ey": "ei", "oy": "ɔi",
        }

    vowel = corres.get(match.group().lower())

    return vowel.lower() if match.group().islower() else vowel.upper()


def régexiser(entrée: str) -> str:
    # Accentuation
    entrée = re.sub("(ei|ey|oy|[aeiouyøáíóúýæ])", lambda match: match.group().upper(), entrée, count=1)

    # Voyelles
    entrée = re.sub("(ei|ey|oy|[aeiouyøáíóúýæ])", resolve_vowels, entrée, flags=re.IGNORECASE)

    return entrée
