from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine, select, update
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_mptt.mixins import BaseNestedSets

from langue import Langue as Lg, Mot as Mt


Base = declarative_base()


# FIXME - conflit avec langue.Langue
class Langue(Base, BaseNestedSets):
    __tablename__ = "langues"
    sqlalchemy_mptt_pk_name = "abréviation"

    abréviation = Column("abréviation", String(10), primary_key=True)
    nom = Column("nom", String(100), unique=True)

    lexique = relationship("Mot")
    segments = relationship("Segment")

    def __repr__(self):
        return "<Langue: {}>".format(self.__str__())

    def __str__(self):
        return self.nom or "---"


class Flexion(Base):
    __tablename__ = "flexions"

    abréviation = Column("abréviation", String(10), primary_key=True)
    nom = Column("nom", String(100), unique=True)

    def __repr__(self):
        return "<Flexion: {}>".format(self.__str__())

    def __str__(self):
        return self.nom


class Segment(Base):
    __tablename__ = "segments"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    abréviation_langue = Column("abréviation_langue", String(10), ForeignKey("langues.abréviation", ondelete="RESTRICT"))
    forme = Column("forme", String(100))
    type = Column("type", String(20))
    commentaire = Column("commentaires", Text, nullable=True)

    langue = relationship("Langue", back_populates="segments")
    dérivés = relationship("Mot")

    def __repr__(self):
        return "<Segment: {}>".format(self.__str__())

    def __str__(self):
        return self.forme


# FIXME - conflit avec langue.Mot
# racine : la racine originelle (ou les racines, M2M?) (CK SEGMENT.type = "racine" ?)
# segments : les segments qui composent ce mot (ordonnés?)
class Mot(Base, BaseNestedSets):
    __tablename__ = "mots"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    forme = Column("forme", String(100))
    # id_parent = Column("id_parent", Integer, ForeignKey("mots.id"), nullable=True)
    abréviation_langue = Column("abréviation_langue", String(10), ForeignKey("langues.abréviation", ondelete="RESTRICT"))
    id_racine = Column("id_racine", Integer, ForeignKey("segments.id"), nullable=True)
    commentaire = Column("commentaires", Text, nullable=True)

    flexions = relationship("Flexion", secondary="formes_flexions")
    segments = relationship("Segment", secondary="formes_segments")

    langue = relationship("Langue", back_populates="lexique")
    racine = relationship("Segment", back_populates="dérivés")

    def __repr__(self):
        return "<Mot: {}>".format(self.__str__())

    def __str__(self):
        return self.forme or "---"


# TODO - renommer en MotFlexion
class FormeFlexion(Base):
    __tablename__ = "formes_flexions"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_mot = Column("id_mot", Integer, ForeignKey("mots.id"))
    abréviation_flexion = Column("abréviation_flexion", String(10), ForeignKey("flexions.abréviation"))


# TODO - renommer en MotSegment
class FormeSegment(Base):
    __tablename__ = "formes_segments"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_mot = Column("id_mot", Integer, ForeignKey("mots.id"))
    id_segment = Column("id_segment", String(10), ForeignKey("segments.id"))


"""
Schéma Langue / Mot / Segment / Flexion avec MPTT
Bon points :
- Permet de tenir une liste de racines pour une langue données :
    SELECT forme FROM segment WHERE type='racine' AND langue='PIE';
- Permet de récupérer les mots dérivant d'une racine :
    SELECT forme FROM mot INNER JOIN segment ON mot.racine = segment.id WHERE segment.forme = 'wergom';
- Limite les jointures en utilisant les abréviations comme PK :
    SELECT forme, langue, type FROM segment WHERE forme LIKE %al%;
- Ajout facile par les paquets de langue :
    merge(VHA), merge(VOC) éventuellement
- Ajout facile de mots:
    INSERT INTO mot (parent, forme, langue, racine, commentaire) VALUES (%s, %s, %s, %s, %s);
    INSERT INTO mot_flexion (mot, flexion) VALUES (%s, %s);
    INSERT INTO mot_segment (mot, segment) VALUES (%s, %s);
- Tous les outils relatifs aux arbres :
    Mot.drilldown_tree()
    Langue.is_ancestor_of(Langue)

Mauvais points :
- Inclusion des éléments d'un arbre par MPTT exclusivement
"""


def obtenir_moteur():
    engine = create_engine("sqlite:///bdd.sqlite3")
    return engine


def créer_bdd():
    engine = obtenir_moteur()
    Base.metadata.create_all(engine)


def obtenir_session():
    engine = obtenir_moteur()
    Session = sessionmaker()
    session = Session(bind=engine)
    return session


# TODO - trouver comment garantir un nœud sans compromettre l'arbre
def garantir(langue: Lg) -> None:
    # with obtenir_session() as session:
    #     bdd_langue = Langue(
    #         abréviation=langue.abréviation,
    #         abréviation_parent=langue.abréviation_parent,
    #         nom=langue.nom,
    #     )
    #     session.merge(bdd_langue)
    #     session.commit()
    return


def obtenir_mot(mot: Mt, langue: Lg) -> Mot:
    with obtenir_session() as session:
        stmt = select(Mot).where(Mot.abréviation_langue == langue.abréviation, Mot.forme == mot.conv)
        mot = session.execute(stmt).scalar_one_or_none()
    return mot


# TODO - mapper les résultats sur des langue.Mot ?
def obtenir_descendants(mot: Mt, langue: Lg) -> list[dict[str: Mot, str: list]]:
    with obtenir_session() as session:
        stmt = select(Mot).where(Mot.abréviation_langue == langue.abréviation, Mot.forme == mot.conv)
        mot = session.execute(stmt).scalar_one_or_none()
        if mot:
            return mot.drilldown_tree()
        else:
            return []


def obtenir_lexique(langue: Lg) -> list[Mot]:
    with obtenir_session() as session:
        stmt = select(Langue).where(Langue.abréviation == langue.abréviation)
        langue = session.execute(stmt).scalar_one()
        return langue.lexique


def ajouter_flexions(mot: Mot, flexions: list[str]) -> None:
    with obtenir_session() as session:
        for flexion in flexions:
            session.add(FormeFlexion(id_mot=mot.id, abréviation_flexion=flexion))
        session.commit()
