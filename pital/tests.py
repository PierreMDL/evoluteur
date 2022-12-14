from unittest import TestCase
from .transcription import runiser


class TestRunes(TestCase):
    def test_loifirtato(self):
        mot_conv = "loifirtato"
        mot_runes = "๐๐๐๐๐๐๐๐๐๐"
        rรฉsultat = runiser(mot_conv)
        self.assertEqual(mot_runes, rรฉsultat)

    def test_cuando(self):
        mot_conv = "cuando"
        mot_runes = "๐๐๐๐๐๐"
        rรฉsultat = runiser(mot_conv)
        self.assertEqual(mot_runes, rรฉsultat)

    def test_macistratu(self):
        mot_conv = "macistratu"
        mot_runes = "๐๐๐๐๐๐๐๐๐๐"
        rรฉsultat = runiser(mot_conv)
        self.assertEqual(mot_runes, rรฉsultat)

    def test_urnela(self):
        mot_conv = "urnela"
        mot_runes = "๐๐๐๐๐๐"
        rรฉsultat = runiser(mot_conv)
        self.assertEqual(mot_runes, rรฉsultat)

    def test_duumuir(self):
        mot_conv = "duumuir"
        mot_runes = "๐๐๐๐๐๐๐"
        rรฉsultat = runiser(mot_conv)
        self.assertEqual(mot_runes, rรฉsultat)

    def test_salueto(self):
        mot_conv = "salueto"
        mot_runes = "๐๐๐๐๐๐๐"
        rรฉsultat = runiser(mot_conv)
        self.assertEqual(mot_runes, rรฉsultat)

    def test_clipeaio(self):
        mot_conv = "clipeaio"
        mot_runes = "๐๐๐๐๐๐๐๐"
        rรฉsultat = runiser(mot_conv)
        self.assertEqual(mot_runes, rรฉsultat)

    def test_arcentelom(self):
        mot_conv = "arcentelom"
        mot_runes = "๐๐๐๐๐๐๐๐๐๐"
        rรฉsultat = runiser(mot_conv)
        self.assertEqual(mot_runes, rรฉsultat)
