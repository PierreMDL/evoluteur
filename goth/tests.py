from unittest import TestCase
from .transcription import runiser


class TestRunes(TestCase):
    def test_bairith(self):
        mot_conv = "bairiþ"
        mot_runes = "𐌱𐌰𐌹𐍂𐌹𐌸"
        résultat = runiser(mot_conv)
        self.assertEqual(mot_runes, résultat)

    def test_waurd(self):
        mot_conv = "waurd"
        mot_runes = "𐍅𐌰𐌿𐍂𐌳"
        résultat = runiser(mot_conv)
        self.assertEqual(mot_runes, résultat)

