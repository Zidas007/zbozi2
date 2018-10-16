from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime,Float

from ..database import db
from ..mixins import CRUDModel

class Zbozi(CRUDModel):
    __tablename__ = 'Zbozi'
    id = Column(Integer, primary_key=True )
    nazev = Column(String(64), nullable=False, unique=True, index=True, doc="Uzivateluv nazev vyrobku.")
    ks = Column(Integer, nullable=False, index=True)
    cena = Column(Float, nullable=False,default=0)

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    @staticmethod
    def find_by_nazev(nazev):
        return db.session.query(Zbozi).filter_by(nazev=nazev).scalar()