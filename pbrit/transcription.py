import re


def transcrire(entrée: str) -> str:
    entrée = entrée.lower()
    entrée = re.sub("^[lr]|l(?=t)", lambda cand: {"l": "ll", "r": "rr"}.get(cand.group()), entrée)
    entrée = entrée.replace("ᵬ", "β̃")  # attention au tilde ;)
    entrée = entrée.translate(str.maketrans("ƀđǥħꝁŧɛøɔy", "βðɣhxθėöọü"))
    return entrée
