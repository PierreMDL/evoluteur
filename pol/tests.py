from unittest import TestCase
from .transcription import régexiser, accentuer
from transcription import phonétiser


class TestCorrect(TestCase):

    def test_szcizpiczi(self):
        mots = {
            "powściągliwość": "pɔf.ɕt͡ɕɔŋˈɡli.vɔɕt͡ɕ",
            "podróży": "pɔdˈru.ʐɨ",
            "czterdzieści": "t͡ʂtɛrˈd͡ʑɛɕ.t͡ɕi",
            "odjeżdżać": "ɔdˈjɛʐ.d͡ʐat͡ɕ",
            "widzi": "ˈvi.d͡ʑi",
            "dzielnica": "d͡ʑɛlˈɲi.t͡sa",
            "tańczyć": "ˈtaɲ.t͡ʂɨt͡ɕ",
            "styczeń": "ˈstɨ.t͡ʂɛɲ",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])

    def test_nasales(self):
        mots = {
            "więzienie": "vjɛɲˈʑɛ.ɲɛ",
            "mężczyzna": "mɛ̃ʂˈt͡ʂɨz.na",
            "mąż": "ˈmɔ̃ʂ",
            "cię": "ˈt͡ɕɛ",
            "oglądam": "ɔɡˈlɔn.dam",
            "pomiędzy": "pɔˈmjɛn.d͡zɨ",
            "sędziwy": "sɛɲˈd͡ʑi.vɨ",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])

    def test_desonorization(self):
        mots = {
            "wkładamy": "fkwaˈdamɨ",
            "krzesło": "ˈkʂɛs.wɔ",
            "przyjeżdżam": "pʂɨˈjɛʐ.d͡ʐam",
            "potrzebować": "pɔt.ʂɛˈbɔ.vat͡ɕ",
            "pisarz": "ˈpi.saʂ",
            "walizka": "vaˈlis.ka",
            "pojazd": "ˈpɔ.jast",
            "kierowca": "kjɛˈrɔf.t͡sa",
            "chwilę": "ˈxfi.lɛ",
            "swoje": "ˈsfɔ.jɛ",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])

    def test_jod(self):
        mots = {
            "kolacja": "kɔˈlat͡s.ja",
            "zwierzęta": "zvjɛˈʐɛn.ta",
            "pamiętasz": "paˈmjɛn.taʂ",
            "zwiedzam": "ˈzvjɛ.d͡zam",
            "sukienkę": "suˈkjɛŋ.kɛ",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])

    def test_ortho(self):
        mots = {
            "złe": "ˈzwɛ",
            "rysować": "rɨˈsɔ.vat͡ɕ",
            "zachód": "ˈza.xut",
            "wschód": "ˈfsxut",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])

    def test_hiatus(self):
        mots = {
            "rozmaity": "rɔz.maˈi.tɨ",
        }

        calc = [phonétiser(accentuer(régexiser(mot), majuscule=False)) for mot in mots.keys()]
        self.assertListEqual(calc, [mot.replace(".", "") for mot in mots.values()])
