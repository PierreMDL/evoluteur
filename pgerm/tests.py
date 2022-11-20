from unittest import TestCase
from .transcription import régexiser, accentuer, phonétiser


class TestIPA(TestCase):
    def test_skurtijo(self):
        mot_conv = "skurtijǭ"
        mot_ipa = "ˈskur.ti.jɔ̃ː"
        résultat = phonétiser(accentuer(régexiser(mot_conv), majuscule=False))
        self.assertEqual(mot_ipa.replace(".", ""), résultat)

    def test_gebana(self):
        mot_conv = "gebaną"
        mot_ipa = "ˈɣe.βɑ.nɑ̃"
        résultat = phonétiser(accentuer(régexiser(mot_conv), majuscule=False))
        self.assertEqual(mot_ipa.replace(".", ""), résultat)

    def test_thanhtaz(self):
        mot_conv = "þanhtaz"
        mot_ipa = "ˈθɑ̃ːx.tɑz"
        résultat = phonétiser(accentuer(régexiser(mot_conv), majuscule=False))
        self.assertEqual(mot_ipa.replace(".", ""), résultat)

    def test_deuza(self):
        mot_conv = "deuzą"
        mot_ipa = "ˈdeu̯.zɑ̃"
        résultat = phonétiser(accentuer(régexiser(mot_conv), majuscule=False))
        self.assertEqual(mot_ipa.replace(".", ""), résultat)

    def test_augooo(self):
        mot_conv = "augô"
        mot_ipa = "ˈɑu̯.ɣɔːː"
        résultat = phonétiser(accentuer(régexiser(mot_conv), majuscule=False))
        self.assertEqual(mot_ipa.replace(".", ""), résultat)

    def test_fimf(self):
        mot_conv = "fimf"
        mot_ipa = "ˈɸimɸ"
        résultat = phonétiser(accentuer(régexiser(mot_conv), majuscule=False))
        self.assertEqual(mot_ipa.replace(".", ""), résultat)

    def test_jeera(self):
        mot_conv = "jērą"
        mot_ipa = "ˈjɛː.rɑ̃"
        résultat = phonétiser(accentuer(régexiser(mot_conv), majuscule=False))
        self.assertEqual(mot_ipa.replace(".", ""), résultat)

    def test_frijoondz(self):
        mot_conv = "frijōndz"
        mot_ipa = "ˈɸri.jɔːndz"
        résultat = phonétiser(accentuer(régexiser(mot_conv), majuscule=False))
        self.assertEqual(mot_ipa.replace(".", ""), résultat)

    def test_habjana(self):
        mot_conv = "habjaną"
        mot_ipa = "ˈxɑβ.jɑ.nɑ̃"
        résultat = phonétiser(accentuer(régexiser(mot_conv), majuscule=False))
        self.assertEqual(mot_ipa.replace(".", ""), résultat)
