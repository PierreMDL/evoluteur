from innovations import ChangementPhonétique
import re
from transcription import syllabifier


class LVélarisé(ChangementPhonétique):
    motif = re.compile("l")
    règle_remplacement = "ł"


class ÉpenthèseDevantONasal(ChangementPhonétique):
    motif = re.compile("^ỏ")
    règle_remplacement = "vỏ"


class Palatalisation(ChangementPhonétique):
    motif = re.compile(".(?=[īiēeẻẽ])")

    def règle_remplacement(self, match):
        return match.group() + "ʲ"


class Palatalisation2(ChangementPhonétique):
    motif = re.compile("[ďťňřľ]")
    règle_remplacement = {
        "ď": "ʣʲ", "ť": "ʦʲ", "ň": "nʲ", "ř": "rʲ", "ľ": "lʲ",
    }


class SonorisationDiphtonguesLiquides(ChangementPhonétique):
    motif = re.compile("(?P<pre>[^aāeēẻiīoōỏuūyȳ]ʲ?)(?P<liq>[oe][rł])(?P<post>[^aāeēẻiīoōỏuūyȳ]ʲ?)")

    def règle_remplacement(self, match):
        pre = match.group("pre")
        liq = match.group("liq")
        post = match.group("post")

        if liq[-1] == "r":
            if liq == "er":
                if post in ["tʲ", "dʲ", "ʃʲ", "ʒʲ", "ʧʲ", "ʤʲ"]:
                    return pre + "er" + post
                if post[0] in ["ꝁ", "k", "g", "m", "p", "b"]:
                    return pre + "erʲ" + post
            return pre + "ar" + post

        if liq[-1] == "ł":
            if pre[0] in ["t", "d", "ʃ", "ʒ", "ʧ", "ʤ", "s"]:
                if post[0] == "n":
                    return pre[0] + "ło" + post
                return pre[0] + "łū" + post
            return pre + liq + post

        return pre + liq + post


class AvancementEDevantAlvéolaires(ChangementPhonétique):
    motif = re.compile("[eē](?=[sltł](?!ʲ))")
    règle_remplacement = {"e": "o", "ē": "a"}


class DisparitionCompensatriceYersFaibles:
    def appliquer(self, entrée):
        syllabes = syllabifier(entrée, list("aāeēẻiīoōỏuūȳ"))
        if len(syllabes) > 1:
            for nb, syllabe in enumerate(reversed(syllabes)):
                if nb == 0:
                    syllabe["noyau"] = re.sub("[iu]", "", syllabe["noyau"])
                elif not syllabes[nb-2]["noyau"]:
                    syllabe["noyau"] = re.sub("[aeiouyẻỏ]", lambda match: {
                        "i": "e", "u": "e",  # transformation des yers
                        "a": "ā", "e": "ē", "o": "ō", "y": "ȳ", "ẻ": "ẽ", "ỏ": "õ",  # allongement compensatoire
                    }.get(match.group()), syllabe["noyau"])
                else:
                    syllabe["noyau"] = re.sub("[iu]", "", syllabe["noyau"])

        entrée = "".join([x for y in syllabes for x in y.values()])
        entrée = re.sub("0", "", entrée)
        return entrée


class FusionNasales(ChangementPhonétique):
    motif = re.compile("[ẻỏẽõ]")
    règle_remplacement = {"ẻ": "ą", "ỏ": "ą", "ẽ": "ã", "õ": "ã"}


class DisparitionLongueur(ChangementPhonétique):
    motif = re.compile("[īȳūōāēãą]")
    règle_remplacement = {
        "ī": "i", "ȳ": "y", "ū": "u", "ō": "u", "ā": "a", "ē": "e", "ã": "ả", "ą": "ẻ",
    }


class Palatalisation3(ChangementPhonétique):
    motif = re.compile("[sztdnrlʒʤʣʦʧ]ʲ")
    règle_remplacement = {
        "sʲ": "ɕ", "zʲ": "ʑ", "tʲ": "ʨ", "dʲ": "ʥ", "nʲ": "ɲ", "rʲ": "ř", "lʲ": "l",
        "ʃʲ": "ʃ", "ʒʲ": "ʒ", "ʦʲ": "ʦ", "ʣʲ": "ʣ", "ʧʲ": "ʧ", "ʤʲ": "ʤ",
    }


class VocalisationLVélarisé(ChangementPhonétique):
    motif = "ł"
    règle_remplacement = "w"


class RenforcementIotisation(ChangementPhonétique):
    motif = re.compile("ʲ(?=[aeiou])")
    règle_remplacement = "j"


class DisparitionIotisation(ChangementPhonétique):
    motif = re.compile("ʲ")


évolution = [
    LVélarisé,
    ÉpenthèseDevantONasal,
    Palatalisation,
    Palatalisation2,
    SonorisationDiphtonguesLiquides,
    AvancementEDevantAlvéolaires,
    DisparitionCompensatriceYersFaibles,
    FusionNasales,
    DisparitionLongueur,
    Palatalisation3,
    VocalisationLVélarisé,
    RenforcementIotisation,
    DisparitionIotisation,
]


def évoluer(entrée):
    for innovation in évolution:
        entrée = innovation().appliquer(entrée)
    return entrée

