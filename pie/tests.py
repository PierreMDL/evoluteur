from unittest import TestCase
from .transcription import régexiser, syllabifier


class TestSyllabes(TestCase):
    def test_mEEh1ns(self):
        mot_regex = régexiser("mḗh₁n̥s")
        syllabes = [
            {"attaque": "m", "noyau": "Ē", "coda": ""},
            {"attaque": "h₁", "noyau": "ṇ", "coda": "s"},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)

    def test_dnghuh2mOs(self):
        mot_regex = régexiser("dn̥ǵʰuh₂mós")
        syllabes = [
            {"attaque": "d", "noyau": "ṇ", "coda": ""},
            {"attaque": "ǵʰ", "noyau": "u", "coda": "h₂"},
            {"attaque": "m", "noyau": "O", "coda": "s"},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)

    def test_dhoh0nEh2(self):
        mot_regex = régexiser("dʰoh₀néh₂")
        syllabes = [
            {"attaque": "dʰ", "noyau": "o", "coda": "h₀"},
            {"attaque": "n", "noyau": "E", "coda": "h₂"},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)

    def test_ph2tErs(self):
        mot_regex = régexiser("ph₂térs")
        syllabes = [
            {"attaque": "p", "noyau": "h₂", "coda": ""},
            {"attaque": "t", "noyau": "E", "coda": "rs"},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)

    def test_uksnbhI(self):
        mot_regex = régexiser("uksn̥bʰí")
        syllabes = [
            {"attaque": "", "noyau": "u", "coda": "k"},
            {"attaque": "s", "noyau": "ṇ", "coda": ""},
            {"attaque": "bʰ", "noyau": "I", "coda": ""},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)
            
    def test_nEbhesey(self):
        mot_regex = régexiser("nébʰesey")
        syllabes = [
            {"attaque": "n", "noyau": "E", "coda": ""},
            {"attaque": "bʰ", "noyau": "e", "coda": ""},
            {"attaque": "s", "noyau": "ej", "coda": ""},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)

    def test_nOkwts(self):
        mot_regex = régexiser("nókʷts")
        syllabes = [
            {"attaque": "n", "noyau": "O", "coda": "kʷts"},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)

    def test_gwEEn(self):
        mot_regex = régexiser("gʷḗn")
        syllabes = [
            {"attaque": "gʷ", "noyau": "Ē", "coda": "n"},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)

    def test_pOOds(self):
        mot_regex = régexiser("pṓds")
        syllabes = [
            {"attaque": "p", "noyau": "Ō", "coda": "ds"},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)

    def test_lEymonm(self):
        mot_regex = régexiser("léymonm̥")
        syllabes = [
            {"attaque": "l", "noyau": "Ej", "coda": ""},
            {"attaque": "m", "noyau": "o", "coda": ""},
            {"attaque": "n", "noyau": "ṃ", "coda": ""},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)

    def test_wErgom(self):
        mot_regex = régexiser("wérǵom")
        syllabes = [
            {"attaque": "", "noyau": "wE", "coda": "r"},
            {"attaque": "ǵ", "noyau": "o", "coda": "m"},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)

    def test_nisdOs(self):
        mot_regex = régexiser("nisdós")
        syllabes = [
            {"attaque": "n", "noyau": "i", "coda": "s"},
            {"attaque": "d", "noyau": "O", "coda": "s"},
        ]
        résultat = syllabifier(mot_regex)
        self.assertListEqual(résultat, syllabes)
