from unittest import TestCase
from .transcription import régexiser, accentuer
from transcription import phonétiser


class TestCorrect(TestCase):

    def test_consonnes_initiales(self):
        mots = {
            "keyra": "ˈcʰeiːra",
            "gera": "ˈcɛːra",
            "ganga": "ˈkauŋka",
            "gjöf": "ˈcœːv",
            "skip": "ˈscɪːp",
            "skrá": "ˈskrauː",
            "sljór": "ˈstljouːr",
            "hlæja": "ˈl̥aiːja",
            "hjálmur": "ˈçaulmʏr",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])

    def test_consonnes_internes(self):
        mots = {
            "kaldur": "ˈkʰaltʏr",
            "bolti": "ˈpɔl̥tɪ",
            "þanki": "ˈθauɲ̊cɪ",
            "lengjast": "ˈleiɲcast",
            "versla": "ˈvɛr̥stla",
            "sigra": "ˈsɪɣra",
            "sögn": "ˈsœkn",
            "hjúkra": "ˈçuːkra",
            "hverfa": "ˈkʰvɛrva",
            "ætla": "ˈaihtla",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])

    def test_consonnes_finales(self):
        mots = {
            "borg": "ˈpɔrk",
            "hólf": "ˈhoulv",
            "bugt": "ˈpʏxt",
            "lax": "ˈlaxs",
            "aðild": "ˈaːðɪlt",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])

    def test_consonnes_doubles(self):
        mots = {
            "pabbi": "ˈpʰapːɪ",
            "keppa": "ˈcʰɛhpa",
            "bygg": "ˈpɪkː",
            "kalla": "ˈkʰatla",
            "steinn": "ˈsteitn",
            "penni": "ˈpʰɛnːɪ",
            "kaffi": "ˈkʰafːɪ",
            "þurr": "ˈθʏrː",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])

    def test_consonnes_simples(self):
        mots = {
            "mig": "ˈmɪːɣ",
            "hafa": "ˈhaːva",
            "haf": "ˈhaːv",
            "tap": "ˈtʰaːp",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])

    def test_autres(self):
        mots = {
            "skipting": "ˈscɪftiŋk",
            "kafli": "ˈkʰaplɪ",
            "nafn": "ˈnapn",
            "nefnd": "ˈnɛmt",
            "nefnt": "ˈnɛm̥t",
            "fá": "ˈfauː",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])

