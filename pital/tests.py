from unittest import TestCase
from .transcription import runiser


class TestRunes(TestCase):
    def test_loifirtato(self):
        mot_conv = "loifirtato"
        mot_runes = "𐌋𐌏𐌉𐌚𐌉𐌓𐌕𐌀𐌕𐌏"
        résultat = runiser(mot_conv)
        self.assertEqual(mot_runes, résultat)

    def test_cuando(self):
        mot_conv = "cuando"
        mot_runes = "𐌂𐌖𐌀𐌍𐌃𐌏"
        résultat = runiser(mot_conv)
        self.assertEqual(mot_runes, résultat)

    def test_macistratu(self):
        mot_conv = "macistratu"
        mot_runes = "𐌌𐌀𐌂𐌉𐌔𐌕𐌓𐌀𐌕𐌖"
        résultat = runiser(mot_conv)
        self.assertEqual(mot_runes, résultat)

    def test_urnela(self):
        mot_conv = "urnela"
        mot_runes = "𐌖𐌓𐌍𐌄𐌋𐌀"
        résultat = runiser(mot_conv)
        self.assertEqual(mot_runes, résultat)

    def test_duumuir(self):
        mot_conv = "duumuir"
        mot_runes = "𐌃𐌖𐌖𐌌𐌖𐌉𐌓"
        résultat = runiser(mot_conv)
        self.assertEqual(mot_runes, résultat)

    def test_salueto(self):
        mot_conv = "salueto"
        mot_runes = "𐌔𐌀𐌋𐌖𐌄𐌕𐌏"
        résultat = runiser(mot_conv)
        self.assertEqual(mot_runes, résultat)

    def test_clipeaio(self):
        mot_conv = "clipeaio"
        mot_runes = "𐌂𐌋𐌉𐌐𐌄𐌀𐌉𐌏"
        résultat = runiser(mot_conv)
        self.assertEqual(mot_runes, résultat)

    def test_arcentelom(self):
        mot_conv = "arcentelom"
        mot_runes = "𐌀𐌓𐌂𐌄𐌍𐌕𐌄𐌋𐌏𐌌"
        résultat = runiser(mot_conv)
        self.assertEqual(mot_runes, résultat)
