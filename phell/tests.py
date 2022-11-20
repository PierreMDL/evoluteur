from unittest import TestCase
from .innovations import évoluer


class TestEvolution(TestCase):
    def test_mEgh2yoos(self):
        mot_regex_pie = "mEǵh₂jōs"
        mot_regex_phell = "mEďďōn"
        résultat = évoluer(mot_regex_pie)
        self.assertEqual(mot_regex_phell, résultat)

    def test_mrEghus(self):
        mot_regex_pie = "mrEǵʰus"
        mot_regex_phell = "brəkʰUs"
        résultat = évoluer(mot_regex_pie)
        self.assertEqual(mot_regex_phell, résultat)

    def test_supnOs(self):
        mot_regex_pie = "supnOs"
        mot_regex_phell = "hUpnos"
        résultat = évoluer(mot_regex_pie)
        self.assertEqual(mot_regex_phell, résultat)

    def test_tErmn(self):
        mot_regex_pie = "tErmṇ"
        mot_regex_phell = "tErmə"
        résultat = évoluer(mot_regex_pie)
        self.assertEqual(mot_regex_phell, résultat)

    def test_Udteros(self):
        mot_regex_pie = "Udteros"
        mot_regex_phell = "Usteros"
        résultat = évoluer(mot_regex_pie)
        self.assertEqual(mot_regex_phell, résultat)

    def test_yEwgos(self):
        mot_regex_pie = "yEwgos"
        mot_regex_phell = "dzEwgos"
        résultat = évoluer(mot_regex_pie)
        self.assertEqual(mot_regex_phell, résultat)
