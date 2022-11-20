import re


corres_voyelles = {
    "अ": "a", "आ": "ā", "ा": "ā",
    "इ": "i", "ई": "ī", "ि": "i", "ी": "ī",
    "उ": "u", "ऊ": "ū",
    "ऋ": "ṛ", "ॠ": "ṝ", "ृ": "ṛ",
    "ऌ": "ḷ", "ॡ": "ḹ",
    "ए": "ē", "ऐ": "ai",
    "ओ": "ō", "औ": "au",
    "अं": "aṃ", "अः": "aḥ", "ं": "aṃ",
}

corres_consonnes = {
    "प": "p", "त": "t", "ट": "ṭ", "च": "c", "क": "k",
    "फ": "pʰ", "थ": "tʰ", "ठ": "ṭʰ", "छ": "cʰ", "ख": "kʰ",
    "ब": "b", "द": "d", "ड": "ḍ", "ज": "j", "ग": "g",
    "भ": "bʰ", "ध": "dʰ", "ढ": "ḍʰ", "झ": "jʰ", "घ": "gʰ",
    "म": "m", "न": "n", "ण": "ṇ", "ञ": "ñ", "ङ": "ṅ",
    "व": "v", "ल": "l", "र": "r", "य": "y", "ह": "h",
    "स": "s", "ष": "ṣ", "श": "ś",
}


def régexiser(entrée: str) -> str:

    de_voyelles = "[" + "".join(sorted(corres_voyelles.keys(), key=lambda k: len(k), reverse=True)) + "]"
    rempl_voyelles = lambda match: corres_voyelles.get(match.group(), match.group())
    entrée = re.sub(de_voyelles, rempl_voyelles, entrée)

    de_consonnnes = "[" + "".join(sorted(corres_consonnes.keys(), key=lambda k: len(k), reverse=True)) + "][" + "".join(
        corres_voyelles.values()) + "्]?"

    def rempl_consonnes(match):
        cons = corres_consonnes.get(match.group()[0])
        if len(match.group()) > 1:
            voy = match.group()[-1]
            if voy == "्":
                return cons
            else:
                return cons + voy
        else:
            return cons + "a"

    entrée = re.sub(de_consonnnes, rempl_consonnes, entrée)

    return entrée
