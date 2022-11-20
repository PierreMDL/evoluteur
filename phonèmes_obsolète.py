class Voyelle:
    def __init__(self, regex, phono, position, hauteur, ipa=None, longueur="courte", fosse="orale", arrondie=False):
        self.longueur = longueur
        self.position = position
        self.hauteur = hauteur
        self.fosse = fosse
        self.arrondie = arrondie
        self.regex = regex
        self.phono = phono
        self.ipa = ipa or phono

    def __repr__(self):
        return self.phono


class Consonne:
    def __init__(self, regex, phono, ipa=None, mode_articulation="", lieu_articulation="", phonation="", modificateur=""):
        self.mode_articulation = mode_articulation
        self.lieu_articulation = lieu_articulation
        self.phonation = phonation
        self.modificateur = modificateur
        self.regex = regex
        self.phono = phono
        self.ipa = ipa or phono

    def __repr__(self):
        return self.phono


e = Voyelle(regex="e", phono="e", longueur="courte", position="antérieure", hauteur="mi-fermée")
ee = Voyelle(regex="ē", phono="ē", ipa="eː", longueur="longue", position="antérieure", hauteur="mi-fermée")
eee = Voyelle(regex="ê", phono="ê", ipa="eːː", longueur="surlongue", position="antérieure", hauteur="mi-fermée")
emiouv = Voyelle(regex="ė", phono="ɛ", longueur="courte", position="antérieure", hauteur="mi-ouverte")
eemiouv = Voyelle(regex="ẹ", phono="ɛ̄", ipa="ɛː", longueur="longue", position="antérieure", hauteur="mi-ouverte")
eeemiouv = Voyelle(regex="ệ", phono="ɛ̂", ipa="ɛːː", longueur="surlongue", position="antérieure", hauteur="mi-ouverte")
o = Voyelle(regex="o", phono="o", longueur="courte", position="postérieure", hauteur="mi-fermée")
oo = Voyelle(regex="ō", phono="ō", longueur="longue", ipa="oː", position="postérieure", hauteur="mi-fermée")
ooo = Voyelle(regex="ô", phono="ô", longueur="surlongue", ipa="oːː", position="postérieure", hauteur="mi-fermée")
omiouv = Voyelle(regex ="ȯ", phono="ɔ", longueur="courte", position="postérieure", hauteur="mi-ouverte")
oomiouv = Voyelle(regex ="ọ", phono="ɔ̄", ipa="ɔː", longueur="longue", position="postérieure", hauteur="mi-ouverte")
ooomiouv = Voyelle(regex ="ộ", phono="ɔ̂", ipa="ɔːː", longueur="surlongue", position="postérieure", hauteur="mi-ouverte")
a = Voyelle(regex="a", phono="a", longueur="courte", position="antérieure", hauteur="ouverte")
aa = Voyelle(regex="ā", phono="ā", ipa="aː", longueur="longue", position="antérieure", hauteur="ouverte")
aaa = Voyelle(regex="â", phono="â", ipa="aːː", longueur="surlongue", position="antérieure", hauteur="ouverte")
apost = Voyelle(regex="ȧ", phono="ɑ", longueur="courte", position="postérieure", hauteur="ouverte")
aapost = Voyelle(regex="ạ", phono="ɑ̄", ipa="ɑː", longueur="longue", position="postérieure", hauteur="ouverte")
aaapost = Voyelle(regex="ậ", phono="ɑ̂", ipa="ɑːː", longueur="surlongue", position="postérieure", hauteur="ouverte")
i = Voyelle(regex="i", phono="i", longueur="courte", position="antérieure", hauteur="fermée")
ii = Voyelle(regex="ī", phono="ī", ipa="iː", longueur="longue", position="antérieure", hauteur="fermée")
iii = Voyelle(regex="î", phono="î", ipa="iːː", longueur="surlongue", position="antérieure", hauteur="fermée")
ipréf = Voyelle(regex="ɪ", phono="ɪ", ipa="ɪ", longueur="courte", position="antérieure", hauteur="mi-fermée")
icent = Voyelle(regex="ɨ", phono="ɨ", ipa="ɨ", longueur="courte", position="centrale", hauteur="fermée")
u = Voyelle(regex="u", phono="u", longueur="courte", position="postérieure", hauteur="fermée", arrondie=True)
uu = Voyelle(regex="ū", phono="ū", ipa="uː", longueur="longue", position="postérieure", hauteur="fermée", arrondie=True)
uuu = Voyelle(regex="û", phono="û", ipa="uːː", longueur="surlongue", position="postérieure", hauteur="fermée", arrondie=True)
upréf = Voyelle(regex="ʊ", phono="ʊ", ipa="ʊ", longueur="courte", position="postérieure", hauteur="pré-fermée", arrondie=True)
ucent = Voyelle(regex="ʉ", phono="ʉ", ipa="ʉ", longueur="courte", position="centrale", hauteur="fermée", arrondie=True)
y = Voyelle(regex="y", phono="y", longueur="courte", position="antérieure", hauteur="fermée", arrondie=True)
yy = Voyelle(regex="ȳ", phono="ȳ", ipa="yː", longueur="longue", position="antérieure", hauteur="fermée", arrondie=True)
earr = Voyelle(regex="ø", phono="ø", longueur="courte", position="antérieure", hauteur="mi-fermée", arrondie=True)
eearr = Voyelle(regex="ǿ", phono="ø̄", ipa="øː", longueur="longue", position="antérieure", hauteur="mi-fermée", arrondie=True)
emiouvarr = Voyelle(regex="œ", phono="œ", longueur="courte", position="antérieure", hauteur="mi-ouverte", arrondie=True)
schwa = Voyelle(regex="ə", phono="ə", longueur="courte", position="centrale", hauteur="moyenne")

enas = Voyelle(regex="ę", phono="ę", ipa="ẽ", longueur="courte", position="antérieure", hauteur="mi-fermée", fosse="nasale")
eenas = Voyelle(regex="ẽ", phono="ę̄", ipa="ẽː", longueur="longue", position="antérieure", hauteur="mi-fermée", fosse="nasale")
eeenas = Voyelle(regex="ë", phono="ę̂", ipa="ẽːː", longueur="surlongue", position="antérieure", hauteur="mi-fermée", fosse="nasale")
emiouvnas = Voyelle(regex="ẻ", phono="ɛ̨", ipa="ɛ̃", longueur="courte", position="antérieure", hauteur="mi-ouverte", fosse="nasale")
eemiouvnas = Voyelle(regex="è", phono="ɛ̨̃", ipa="ɛ̃ː", longueur="longue", position="antérieure", hauteur="mi-ouverte", fosse="nasale")
onas = Voyelle(regex="ǫ", phono="ǫ", ipa="õ", longueur="courte", position="postérieure", hauteur="mi-fermée", fosse="nasale")
oonas = Voyelle(regex="õ", phono="ǭ", ipa="õː", longueur="longue", position="postérieure", hauteur="mi-fermée", fosse="nasale")
ooonas = Voyelle(regex="ö", phono="ǫ̂", ipa="õːː", longueur="surlongue", position="postérieure", hauteur="mi-fermée", fosse="nasale")
omiouvnas = Voyelle(regex="ỏ", phono="ɔ̨", ipa="ɔ̃", longueur="courte", position="postérieure", hauteur="mi-ouverte", fosse="nasale")
oomiouvnas = Voyelle(regex="ò", phono="ɔ̨̄", ipa="ɔ̃ː", longueur="longue", position="postérieure", hauteur="mi-ouverte", fosse="nasale")
ooomiouvnas = Voyelle(regex="ȍ", phono="ɔ̨̂", ipa="ɔ̃ːː", longueur="surlongue", position="postérieure", hauteur="mi-ouverte", fosse="nasale")
apostnas = Voyelle(regex="ả", phono="ɑ̨", ipa="ɑ̃", longueur="courte", position="postérieure", hauteur="ouverte", fosse="nasale")
aapostnas = Voyelle(regex="à", phono="ɑ̨̄", ipa="ɑ̃ː", longueur="longue", position="postérieure", hauteur="ouverte", fosse="nasale")
aaapostnas = Voyelle(regex="ȁ", phono="ɑ̨̂", ipa="ɑ̃ːː", longueur="surlongue", position="postérieure", hauteur="ouverte", fosse="nasale")
inas = Voyelle(regex="į", phono="į", ipa="ĩ", longueur="courte", position="antérieure", hauteur="fermée", fosse="nasale")
iinas = Voyelle(regex="ĩ", phono="į̄", ipa="ĩː", longueur="longue", position="antérieure", hauteur="fermée", fosse="nasale")
unas = Voyelle(regex="ũ", phono="ų", ipa="ũ", longueur="courte", position="postérieure", hauteur="fermée", fosse="nasale", arrondie=True)
uunas = Voyelle(regex="ü", phono="ų̄", ipa="ũː", longueur="longue", position="postérieure", hauteur="fermée", fosse="nasale", arrondie=True)
ynas = Voyelle(regex="ỷ", phono="y̨", ipa="ỹ", longueur="courte", position="antérieure", hauteur="fermée", fosse="nasale", arrondie=True)
yynas = Voyelle(regex="ỳ", phono="ȳ̨", ipa="ỹː", longueur="longue", position="antérieure", hauteur="fermée", fosse="nasale", arrondie=True)
earrnas = Voyelle(regex="ở", phono="ø̨", ipa="ø̃", longueur="courte", position="antérieure", hauteur="mi-fermée", fosse="nasale", arrondie=True)
eearrnas = Voyelle(regex="ờ", phono="ø̨̄", ipa="ø̃ː", longueur="longue", position="antérieure", hauteur="mi-fermée", fosse="nasale", arrondie=True)
emiouvarrnas = Voyelle(regex="ꭁ", phono="œ̨", ipa="œ̃", longueur="courte", position="antérieure", hauteur="mi-ouverte", fosse="nasale", arrondie=True)
voyelles = {a, aa, aaa, apost, aapost, aaapost, e, ee, eee, emiouv, eemiouv, eeemiouv, i, ii, iii, o, oo, ooo, omiouv,
            oomiouv, ooomiouv, u, uu, uuu, y, yy, earr, eearr, emiouvarr, schwa,
            apostnas, aapostnas, aaapostnas, enas, eenas, eeenas, emiouvnas, eemiouvnas, inas, iinas, onas, oonas, ooonas, omiouvnas,
            oomiouvnas, ooomiouvnas, unas, uunas, ynas, yynas, earrnas, eearrnas, emiouvarrnas}


m = Consonne(regex="m", phono="m", mode_articulation="nasale", lieu_articulation="bilabiale")
n = Consonne(regex="n", phono="n", mode_articulation="nasale", lieu_articulation="alvéolaire")
p = Consonne(regex="p", phono="p", mode_articulation="occlusive", lieu_articulation="bilabiale", phonation="sourde")
t = Consonne(regex="t", phono="t", mode_articulation="occlusive", lieu_articulation="alvéolaire", phonation="sourde")
kj = Consonne(regex="ḱ", phono="ḱ", ipa="c", mode_articulation="occlusive", lieu_articulation="palato-vélaire", phonation="sourde")
k = Consonne(regex="k", phono="k", mode_articulation="occlusive", lieu_articulation="vélaire pure", phonation="sourde")
kw = Consonne(regex="kʷ", phono="kʷ", mode_articulation="occlusive", lieu_articulation="labio-vélaire", phonation="sourde")
b = Consonne(regex="b", phono="b", mode_articulation="occlusive", lieu_articulation="bilabiale", phonation="sonore")
d = Consonne(regex="d", phono="d", mode_articulation="occlusive", lieu_articulation="alvéolaire", phonation="sonore")
gj = Consonne(regex="ǵ", phono="ǵ", ipa="ɟ", mode_articulation="occlusive", lieu_articulation="palato-vélaire", phonation="sonore")
g = Consonne(regex="g", phono="g", mode_articulation="occlusive", lieu_articulation="vélaire pure", phonation="sonore")
gw = Consonne(regex="gʷ", phono="gʷ", mode_articulation="occlusive", lieu_articulation="labio-vélaire", phonation="sonore")
ph = Consonne(regex="pʰ", phono="pʰ", mode_articulation="occlusive", lieu_articulation="bilabiale", phonation="sourde",
              modificateur="aspirée")
th = Consonne(regex="tʰ", phono="tʰ", mode_articulation="occlusive", lieu_articulation="alvéolaire", phonation="sourde",
              modificateur="aspirée")
kh = Consonne(regex="kʰ", phono="kʰ", mode_articulation="occlusive", lieu_articulation="vélaire pure", phonation="sourde",
              modificateur="aspirée")
kwh = Consonne(regex="kʷʰ", phono="kʷʰ", mode_articulation="occlusive", lieu_articulation="labio-vélaire", phonation="sourde",
               modificateur="aspirée")
bh = Consonne(regex="bʰ", phono="bʰ", mode_articulation="occlusive", lieu_articulation="bilabiale", phonation="sonore",
              modificateur="aspirée")
dh = Consonne(regex="dʰ", phono="dʰ", mode_articulation="occlusive", lieu_articulation="alvéolaire", phonation="sonore",
              modificateur="aspirée")
gjh = Consonne(regex="ǵʰ", phono="ǵʰ", mode_articulation="occlusive", lieu_articulation="palato-vélaire", phonation="sonore",
               modificateur="aspirée")
gh = Consonne(regex="gʰ", phono="gʰ", mode_articulation="occlusive", lieu_articulation="vélaire pure", phonation="sonore",
              modificateur="aspirée")
gwh = Consonne(regex="gʷʰ", phono="gʷʰ", mode_articulation="occlusive", lieu_articulation="labio-vélaire", phonation="sonore",
               modificateur="aspirée")
s = Consonne(regex="s", phono="s", mode_articulation="fricative", lieu_articulation="alvéolaire", phonation="sourde")
phi = Consonne(regex="ꝑ", phono="ɸ", mode_articulation="fricative", lieu_articulation="bilabiale", phonation="sourde")
theta = Consonne(regex="ŧ", phono="θ", mode_articulation="fricative", lieu_articulation="alvéolaire", phonation="sourde")
kha = Consonne(regex="ꝁ", phono="x", mode_articulation="fricative", lieu_articulation="vélaire pure", phonation="sourde")
khaw = Consonne(regex="ꝁʷ", phono="xʷ", mode_articulation="fricative", lieu_articulation="labio-vélaire", phonation="sourde")
beta = Consonne(regex="ƀ", phono="β", mode_articulation="fricative", lieu_articulation="bilabiale", phonation="sonore")
edh = Consonne(regex="đ", phono="ð", mode_articulation="fricative", lieu_articulation="alvéolaire", phonation="sonore")
gamma = Consonne(regex="ǥ", phono="ɣ", mode_articulation="fricative", lieu_articulation="vélaire pure", phonation="sonore")
gammaw = Consonne(regex="ǥʷ", phono="ɣʷ", mode_articulation="fricative", lieu_articulation="labio-vélaire", phonation="sonore")
h = Consonne(regex="h", phono="h", mode_articulation="fricative", lieu_articulation="glottale", phonation="sourde")
hson = Consonne(regex="ɦ", phono="ɦ", mode_articulation="fricative", lieu_articulation="glottale", phonation="sonore")
f = Consonne(regex="f", phono="f", mode_articulation="fricative", lieu_articulation="labio-dentale", phonation="sourde")
v = Consonne(regex="v", phono="v", mode_articulation="fricative", lieu_articulation="labio-dentale", phonation="sonore")
z = Consonne(regex="z", phono="z", mode_articulation="fricative", lieu_articulation="alvéolaire", phonation="sonore")
h1 = Consonne(regex="h₁", phono="h₁", mode_articulation="fricative", lieu_articulation="laryngale")
h2 = Consonne(regex="h₂", phono="h₂", mode_articulation="fricative", lieu_articulation="laryngale")
h3 = Consonne(regex="h₃", phono="h₃", mode_articulation="fricative", lieu_articulation="laryngale")
r = Consonne(regex="r", phono="r", mode_articulation="roulée", lieu_articulation="alvéolaire", phonation="sonore")
l = Consonne(regex="l", phono="l", mode_articulation="spirante", lieu_articulation="alvéolaire", phonation="sonore")
lping = Consonne(regex="ɫ", phono="ɫ", mode_articulation="spirante", lieu_articulation="alvéo-vélaire", phonation="sonore")

w = Consonne(regex="w", phono="w", mode_articulation="approximante", lieu_articulation="labio-vélaire", phonation="sonore")
j = Consonne(regex="j", phono="j", mode_articulation="approximante", lieu_articulation="palatale", phonation="sonore")

