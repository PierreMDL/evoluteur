import numpy as np

ipa_voyelles = np.array(
    [
        [
            [
                [
                    ['i', '',  'ɨ', '',  'ɯ'],
                    ['',  'ɪ', '',  'ɯ̽', ''],
                    ['e', '',  'ɘ', '',  'ɤ'],
                    ['',  '',  'ə', '',  ''],
                    ['ɛ', '',  'ɜ', '',  'ʌ'],
                    ['',  'æ', 'ɐ', '',  ''],
                    ['a', '',  'ä', '',  'ɑ'],
                ], [
                    ['y', '',  'ʉ', '',  'u'],
                    ['',  'ʏ', '',  'ʊ', ''],
                    ['ø', '',  'ɵ', '',  'o'],
                    ['',  '',  '',  '',  'o̞'],
                    ['œ', '',  'ɞ', '',  'ɔ'],
                    ['',  '',  '',  '',  ''],
                    ['Œ', '',  '',  '',  'ɒ'],
                ],
            ], [
                [
                    ['ĩ', '',  '̃ɨ', '',  '̃ɯ'],
                    ['',  '̃ɪ', '',  '̃ɯ̽', ''],
                    ['̃e', '',  '̃ɘ', '',  '̃ɤ'],
                    ['',  '',  '̃ə', '',  ''],
                    ['̃ɛ', '',  '̃ɜ', '',  '̃ʌ'],
                    ['',  '̃æ', '̃ɐ', '',  ''],
                    ['̃a', '',  '̃ä', '',  '̃ɑ'],
                ], [
                    ['̃y', '',  '̃ʉ', '',  '̃u'],
                    ['',  '̃ʏ', '',  '̃ʊ', ''],
                    ['̃ø', '',  '̃ɵ', '',  '̃o'],
                    ['',  '',  '',  '',  '̃o̞'],
                    ['̃œ', '',  '̃ɞ', '',  '̃ɔ'],
                    ['',  '',  '',  '',  ''],
                    ['̃Œ', '',  '',  '',  '̃ɒ'],
                ],
            ],
        ], [
            [
                [
                    ['iː', '',   'ɨː', '',   'ɯː'],
                    ['',   'ɪː', '',   'ɯː', ''],
                    ['eː', '',   'ɘː', '',   'ɤː'],
                    ['',   '',   'əː', '',   ''],
                    ['ɛː', '',   'ɜː', '',   'ʌː'],
                    ['',   'æː', 'ɐː', '',   ''],
                    ['aː', '',   'äː', '',   'ɑː'],
                ], [
                    ['yː', '',   'ʉː', '',   'uː'],
                    ['',   'ʏː', '',   'ʊː', ''],
                    ['øː', '',   'ɵː', '',   'oː'],
                    ['',   '',   '',   '',   'o̞ː'],
                    ['œː', '',   'ɞː', '',   'ɔː'],
                    ['',   '',   '',   '',   ''],
                    ['Œː', '',   '',   '',   'ɒː'],
                ],
            ], [
                [
                    ['ĩː', '',   '̃ɨː', '',   '̃ɯː'],
                    ['',   '̃ɪː', '',   '̃ɯ̽ː', ''],
                    ['̃eː', '',   '̃ɘː', '',   '̃ɤː'],
                    ['',   '',   '̃əː', '',   ''],
                    ['̃ɛː', '',   '̃ɜː', '',   '̃ʌː'],
                    ['',   '̃æː', '̃ɐː', '',   ''],
                    ['̃aː', '',   '̃äː', '',   '̃ɑː'],
                ], [
                    ['̃yː', '',   '̃ʉː', '',   '̃uː'],
                    ['',   '̃ʏː', '',   '̃ʊː', ''],
                    ['̃øː', '',   '̃ɵː', '',   '̃oː'],
                    ['',   '',   '',   '',   '̃o̞ː'],
                    ['̃œː', '',   '̃ɞː', '',   '̃ɔː'],
                    ['',   '',   '',   '',   ''],
                    ['̃Œː', '',   '',   '',   '̃ɒː'],
                ],
            ],
        ],
    ],
)

regex_voyelles = {'è': 'ɛ̃ː', 'ẻ': 'ɛ̃', 'ë': 'ẽːː', 'ẽ': 'ẽː', 'ę': 'ẽ', 'ə': 'ə', 'œ': 'œ', 'ǿ': 'øː', 'ø': 'ø', 'ȳ': 'yː', 'y': 'y', 'û': 'uːː', 'ū': 'uː', 'u': 'u', 'î': 'iːː', 'ī': 'iː', 'i': 'i', 'ậ': 'ɑːː', 'ạ': 'ɑː', 'ȧ': 'ɑ', 'â': 'aːː', 'ꭁ': 'œ̃', 'ā': 'aː', 'ờ': 'ø̃ː', 'a': 'a', 'ở': 'ø̃', 'ộ': 'ɔːː', 'ỳ': 'ỹː', 'ọ': 'ɔː', 'ỷ': 'ỹ', 'ȯ': 'ɔ', 'ü': 'ũː', 'ô': 'oːː', 'ũ': 'ũ', 'ō': 'oː', 'ĩ': 'ĩː', 'o': 'o', 'į': 'ĩ', 'ệ': 'ɛːː', 'ȁ': 'ɑ̃ːː', 'ẹ': 'ɛː', 'à': 'ɑ̃ː', 'ė': 'ɛ', 'ả': 'ɑ̃', 'ê': 'eːː', 'ȍ': 'ɔ̃ːː', 'ē': 'eː', 'ò': 'ɔ̃ː', 'e': 'e', 'ỏ': '̃ɔ', 'ö': 'õːː', 'õ': 'õː', 'ǫ': 'õ'}

ipa_consonnes = np.array(
    [
        [
            [
                ['m', '', '', 'n', '', '', '', '', 'ɲ', 'ŋ', 'ŋʷ', '', '', ''],
                ['b', '', '', 'd', '', '', '', '', 'ɟ', 'g', 'gʷ', '', 'ʡ', 'ʔ'],
                ['', 'b͡v', 'd͡ð', 'd͡z', 'd͡ʒ', 'ɖ͡ʐ', 'd͡ʑ', '', '', '', '', '', '', ''],
                ['β', 'v', 'ð', 'z', 'ʒ', 'ʐ', 'ʑ', '', 'ʝ', 'ɣ', 'ɣʷ', 'ʕ', 'ʢ', 'ɦ'],
                ['', '', '', 'ɹ', '', '', '', '', 'j', '', 'w', '', '', ''],
                ['', '', '', 'r', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', 'l', '', '', '', 'ɫ', 'ʎ', '', '', '', '', ''],
            ], [
                ['m̥', '', '', 'n̥', '', '', '', '', '', '', '', '', '', ''],
                ['p', '', '', 't', '', '', '', '', 'c', 'k', 'kʷ', '', '', ''],
                ['', 'p͡f', 't͡θ', 't͡s', 't͡ʃ', 'ʈ͡ʂ', 't͡ɕ', '', '', '', '', '', '', ''],
                ['ɸ', 'f', 'θ', 's', 'ʃ', 'ʂ', 'ɕ', 'ɧ', 'ç', 'x', 'xʷ', 'ħ', 'ʜ', 'h'],
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', 'r̥', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', 'l̥', '', '', '', '', '', '', '', '', '', ''],
            ],
        ],
        [
            [
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                ['bʰ', '', '', 'dʰ', '', '', '', '', '', 'gʰ', 'gʷʰ', '', '', ''],
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ], [
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                ['pʰ', '', '', 'tʰ', '', '', '', '', 'cʰ', 'kʰ', 'kʷʰ', '', '', ''],
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            ],
        ],
    ],
)

regex_consonnes = {'ŧ': 'θ', 'ꝑ': 'ɸ', 's': 's', 'gʷʰ': 'gʷʰ', 'gʰ': 'gʰ', 'ǵʰ': 'ǵʰ', 'dʰ': 'dʰ', 'bʰ': 'bʰ', 'kʷʰ': 'kʷʰ', 'ḱʰ': 'cʰ', 'kʰ': 'kʰ', 'tʰ': 'tʰ', 'pʰ': 'pʰ', 'gʷ': 'gʷ', 'g': 'g', 'ǵ': 'ɟ', 'd': 'd', 'b': 'b', 'kʷ': 'kʷ', 'k': 'k', 'ḱ': 'c', 't': 't', 'p': 'p', 'n': 'n', 'm': 'm', 'j': 'j', 'w': 'w', 'ɫ': 'ɫ', 'l': 'l', 'r': 'r', 'h₃': 'h₃', 'h₂': 'h₂', 'h₁': 'h₁', 'z': 'z', 'v': 'v', 'f': 'f', 'ɦ': 'ɦ', 'h': 'h', 'ǥʷ': 'ɣʷ', 'ǥ': 'ɣ', 'đ': 'ð', 'ƀ': 'β', 'ꝁʷ': 'xʷ', 'ꝁ': 'x', "ʣ": "d͡z", "ʥ": "d͡ʑ", "ɖ": "d͡ʐ", "ʤ": "d͡ʒ", "ʦ": "t͡s", "ʨ": "t͡ɕ", "ʈ": "t͡ʂ", "ʧ": "t͡ʃ", "ɕ": "ɕ", "ʑ": "ʑ", "ʂ": "ʂ",}



class CARACTÈRE:
    degré = 1
    nom = "caractère"

    def __init__(self, degré=1):
        self.degré = degré

class HAUTEUR(CARACTÈRE):
    nom = "hauteur"

class LONGUEUR(CARACTÈRE):
    nom = "longueur"

class FOSSE(CARACTÈRE):
    nom = "fosse"

class ARRONDIE(CARACTÈRE):
    nom = "arrondie"

class POSITION(CARACTÈRE):
    nom = "position"

class MODE(CARACTÈRE):
    nom = "mode"

class LIEU(CARACTÈRE):
    nom = "lieu"

class PHONATION(CARACTÈRE):
    nom = "phonation"

class ASPIRATION(CARACTÈRE):
    nom = "aspiration"


class Phonème:
    regex = "?"
    ipa = "?"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__str__()}>"

    def __str__(self):
        return self.ipa

    def __add__(self, other):
        return trouver_phonème(self, lambda c, d: c - d, other)

    def __sub__(self, other):
        return trouver_phonème(self, lambda c, d: c + d, other)


def trouver_phonème(phonème: Phonème, opération, caractère: CARACTÈRE) -> str:
    if not isinstance(caractère, CARACTÈRE) and not (isinstance(caractère, type) and issubclass(caractère, CARACTÈRE)):
        raise TypeError
    if not hasattr(phonème, caractère.nom):
        return phonème.ipa

    if isinstance(phonème, Voyelle):
        caractères = {
            "longueur": phonème.longueur[0],
            "fosse": phonème.fosse[0],
            "arrondie": phonème.arrondie[0],
            "hauteur": phonème.hauteur[0],
            "position": phonème.position[0],
        }
        chercher_ipa = lambda: ipa_voyelles[
            caractères["longueur"],
            caractères["fosse"],
            caractères["arrondie"],
            caractères["hauteur"],
            caractères["position"],
        ]

    elif isinstance(phonème, Consonne):
        caractères = {
            "mode": phonème.mode[0],
            "lieu": phonème.lieu[0],
            "phonation": phonème.phonation[0],
            "aspiration": phonème.aspiration[0],
        }
        chercher_ipa = lambda: ipa_consonnes[
            caractères["aspiration"],
            caractères["phonation"],
            caractères["mode"],
            caractères["lieu"],
        ]
    else:
        raise TypeError

    ipa = phonème.ipa
    try:
        offset = caractère.degré
        while offset > 0:
            index = opération(caractères[caractère.nom], 1)
            if index < 0:
                raise IndexError  # on évite l'index -1...
            caractères[caractère.nom] = index
            ipa = chercher_ipa()
            if ipa != '':
                offset -= 1
        return ipa
    except IndexError:
        return ipa


class Voyelle(Phonème):
    def __init__(self, regex, ipa):
        self.regex = regex
        self.ipa = ipa
        self.longueur, self.fosse, self.arrondie, self.hauteur, self.position = np.where(ipa_voyelles == self.ipa)


voyelles = {regex: Voyelle(regex=regex, ipa=ipa) for regex, ipa in regex_voyelles.items()}


class Consonne(Phonème):
    def __init__(self, regex, ipa):
        self.regex = regex
        self.ipa = ipa
        self.aspiration, self.phonation, self.mode, self.lieu = np.where(ipa_consonnes == self.ipa)


consonnes = {regex: Consonne(regex=regex, ipa=ipa) for regex, ipa in regex_consonnes.items()}


class Mot:
    def __init__(self, mot_regex):
        phonèmes = []
        for phonème in mot_regex:
            if voyelle := voyelles.get(phonème, None):
                phonèmes.append(voyelle)
            elif consonne := consonnes.get(phonème, None):
                phonèmes.append(consonne)
            else:
                phonèmes.append(Phonème())
        self.phonèmes = phonèmes

    @property
    def ipa(self):
        return "".join([phonème.ipa for phonème in self.phonèmes])

    @property
    def regex(self):
        return "".join([phonème.regex for phonème in self.phonèmes])

    def __str__(self):
        return self.ipa

    def __repr__(self):
        return f"Mot: {self.__str__()}"
