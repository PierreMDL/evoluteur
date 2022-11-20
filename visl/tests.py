from unittest import TestCase
from .transcription import syllabifier


class TestSyllabes(TestCase):
    def test_kjolr(self):
        mot_regex_visl = "kjȯlr"
        syllabes = [
            {'attaque': 'kj', 'noyau': 'ȯ', 'coda': 'lr'},
        ]
        résultat = syllabifier(mot_regex_visl)
        self.assertListEqual(syllabes, résultat)

    def test_berging(self):
        mot_regex_visl = "bergiŋ"
        syllabes = [
            {'attaque': 'b', 'noyau': 'e', 'coda': 'r'},
            {'attaque': 'g', 'noyau': 'i', 'coda': 'ŋ'},
        ]
        résultat = syllabifier(mot_regex_visl)
        self.assertListEqual(syllabes, résultat)

