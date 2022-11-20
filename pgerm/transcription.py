import re
from transcription import phonétiser as base_ph, accentuer as base_ac


corres_regex_voyelles_antérieures = {
    "ō": "ọ", "ô": "ộ", "ǭ": "ò", "ǫ̂": "ȍ",
    "a": "ȧ", "ā": "ạ", "ą": "ả", "ą̄": "à",
    "ē": "ẹ", "ê": "ệ",
}

corres_regex_consonnes_fricatives = {
    "b": "ƀ", "d": "đ", "g": "ǥ", "f": "ꝑ", "þ": "ŧ", "h": "ꝁ",
}

corres_regex_nasales = {
    "ȧnꝁ": "àꝁ", "inꝁ": "ĩꝁ", "unꝁ": "ũꝁ",
}

corres_regex_occlusions = {
    "ƀ": "b", "đ": "d", "ǥ": "g",
    "ƀƀ": "bb", "đđ": "dd", "ǥǥ": "gg",
}


def régexiser(entrée: str) -> str:
    entrée = re.sub("ą̄|ǫ̂|[aāąēêōôǭ]", lambda ant: corres_regex_voyelles_antérieures.get(ant.group()), entrée)
    entrée = re.sub("[bdgfþh]", lambda cons: corres_regex_consonnes_fricatives.get(cons.group()), entrée)
    entrée = re.sub("[ȧiu]nꝁ", lambda nas: corres_regex_nasales.get(nas.group()), entrée)
    entrée = re.sub("^[đƀ]|(?<=m)ƀ|(?<=n)[đǥ]|(?<=[lzr])đ|ƀƀ|đđ|ǥǥ", lambda fric: corres_regex_occlusions.get(fric.group()), entrée)
    # ^ ATT : "Evidence for /d/ after /r/ is conflicting: Gothic waurd "word" (not *waurþ, with devoicing),  Old Norse orð" ^

    return entrée


def accentuer(entrée: str, majuscule: bool = True) -> str:
    return base_ac(entrée, noyaux=["ȧi", "ȧu", "eu", "iu", "ọu"] + list("ȧeiuạēẹīọūộệảįųàĩòũȍ"), place=1, majuscule=majuscule)
    # # ^ ɔ̄u peut-être inexistant si loi de Malhow appliquée avant PG ^


corres_regex_trans_nas = {
    "àꝁ": "ȧnꝁ", "ĩꝁ": "inꝁ", "ũꝁ": "unꝁ",
}

corres_regex_trans_post = {
    "ọ": "ō", "ộ": "ô", "ò": "ǭ", "ȍ": "ǫ̂",
    "ȧ": "a", "ạ": "ā", "ả": "ą", "à": "ą̄",
    "ẹ": "ē", "ệ": "ê",
}

corres_regex_trans_fric = {
    "ꝑ": "f", "ŧ": "þ", "ꝁ": "h",
    "ƀ": "b", "đ": "d", "ǥ": "g",
}


def transcrire(valeur: str) -> str:
    valeur = valeur.lower()
    valeur = re.sub("[àĩũ]ꝁ", lambda nas: corres_regex_trans_nas.get(nas.group()), valeur)
    valeur = re.sub("[ọộòȍȧạảàẹệ]", lambda post: corres_regex_trans_post.get(post.group()), valeur)
    valeur = re.sub("[ꝑŧꝁƀđǥ]", lambda fric: corres_regex_trans_fric.get(fric.group()), valeur)

    return valeur


def phonétiser(entrée: str) -> str:
    entrée = base_ph(entrée)
    return re.sub("(?<=[ɑe])u", "u̯", entrée)
