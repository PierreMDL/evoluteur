from transcription import transcrire, régexiser, phonétiser, runiser, syllabifier


class Mot:
    """Mot naïf, où la forme REGEX est la forme conventionnelle entrée"""
    évolution = []

    def __init__(self, entrée: str, depuis_regex: bool = False):
        self._entrée = entrée
        self._depuis_regex = depuis_regex
        self._conv = entrée if not depuis_regex else ""
        self._regex = entrée if depuis_regex else ""
        self._ipa = ""
        self._runes = ""
        self._syllabes = []

    @staticmethod
    def _transcrire(valeur: str) -> str:
        return transcrire(valeur)

    @staticmethod
    def _régexiser(valeur: str) -> str:
        return régexiser(valeur)

    @staticmethod
    def _phonétiser(valeur: str) -> str:
        return phonétiser(valeur)

    @staticmethod
    def _runiser(valeur: str) -> str:
        return runiser(valeur)

    # @staticmethod
    # def _accentuer(cls, valeur):
    #     return accentuer(valeur, )

    @staticmethod
    def _syllabifier(valeur: str) -> list[dict]:
        return syllabifier(valeur, list("aeiouyǭ"))  # TODO - quels sont les noyaux par défaut ?

    @property
    def conv(self) -> str:
        if not self._conv:
            self._conv = self._transcrire(self.regex)
        return self._conv

    @property
    def regex(self) -> str:
        if not self._regex:
            self._regex = self._régexiser(self._entrée)
        return self._regex

    @property
    def ipa(self) -> str:
        if not self._ipa:
            self._ipa = self._phonétiser(self.regex)
        return self._ipa

    @property
    def runes(self) -> str:
        if not self._runes:
            self._runes = self._runiser(self.conv)
        return self._runes

    @property
    def syllabes(self) -> list[dict]:
        if not self._syllabes:
            self._syllabes = self._syllabifier(self.regex)
        return self._syllabes

    def __str__(self) -> str:
        return self.conv

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.__str__()}>"

    def évoluer(self, mot_cible):
        évolution = mot_cible.évolution
        étape = self.regex

        for innovation in évolution:
            étape = innovation().appliquer(étape)

        return mot_cible(étape, depuis_regex=True)


class Langue:
    nom = ""
    abréviation = ""
    abréviation_parent = None
    mot = Mot
    grammaire = {}


__all__ = (
    "Mot",
    "Langue",
    "transcrire",
    "régexiser",
    "phonétiser",
    "runiser",
    "syllabifier",
)