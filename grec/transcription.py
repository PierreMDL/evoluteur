import re


corres = {
    "α": "a", "ά": "A", "ε": "ė", "έ": "Ė", "ι": "i", "ί": "I", "ο": "ȯ", "ό": "Ȯ", "υ": "i", "ύ": "I",
    "η": "i", "ή": "I", "ω": "ȯ", "ώ": "Ȯ",
    "αυ": "af", "αύ": "Af", "ευ": "ėf", "εύ": "Ėf", "ου": "u", "ού": "U", "ηυ": "if", "ηύ": "iF",
    "αι": "ė", "αί": "Ė", "ει": "i", "εί": "I", "οι": "i", "οί": "I", "υι": "i", "υί": "I",
    "π": "p", "τ": "t", "κ": "k",  # c devant i, e, t
    "β": "v", "δ": "đ", "γ": "ǥ",  # ʝ devant i, e
    "φ": "f", "θ": "ŧ", "χ": "ꝁ",  # ç devant i, e
    "μπ": "mb",  # b à l'initiale seulement?
    "ντ": "nd",  # d à l'initiale seulement ?
    "γγ": "ŋg",  # nʝ devant i, e; g à l'initiale -j devant i, e apparemment
    "λ": "l", "μ": "m", "ν": "n", "ρ": "ɾ",
    "λι": "ʎ", "νι": "ɲ",
    "σ": "s",  # z devant consonne sonore
    "ς": "s",  # idem
    "ζ": "z",
    "ξ": "ks",  # gz après n
    "ψ": "ps",
    "τσ": "ʦ",
    "τζ": "ʣ",
}

palatalization = {
    "n t": "n d", "n k": "n g",
    " mb": " b", " nd": " d", " ŋ": " ",
    "ki": "ci", "kI": "cI", "kė": "cė", "kĖ": "cĖ", "kt": "ct",
    "ǥi": "ʝi", "ǥI": "ʝI", "ǥė": "ʝė", "ǥĖ": "ʝĖ",
    "ꝁi": "çi", "ꝁI": "çI", "ꝁė": "çė", "ꝁĖ": "çĖ",
    "sv": "zv", "sm": "zm",
}


def régexiser(entrée: str) -> str:

    de = "|".join(sorted(corres.keys(), key=lambda k: len(k), reverse=True))
    résoudre_orthographe = lambda match: corres.get(match.group(), match.group())
    res = re.sub(de, résoudre_orthographe, entrée.lower())

    de = "|".join(sorted(palatalization.keys(), key=lambda k: len(k), reverse=True))
    résoudre_palatalization = lambda match: palatalization.get(match.group(), match.group())
    res = re.sub(de, résoudre_palatalization, res)

    return res
