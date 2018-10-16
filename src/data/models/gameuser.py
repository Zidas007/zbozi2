from flask_login import UserMixin
from sqlalchemy.schema import Column
from sqlalchemy.types import Boolean, Integer, String, Date

from ..database import db
from ..mixins import CRUDModel
from ..util import generate_random_token
from ...settings import app_config
from ...extensions import bcrypt

class GameUser(CRUDModel):
    __tablename__ = 'gameusers'

    id = Column(Integer, primary_key=True)
    email = Column(String(64), nullable=False, unique=True, index=True, doc="The user's email address.")
    username = Column(String(64), nullable=False, unique=True, index=True, doc="The user's username.")
    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    @staticmethod
    def find_by_email(email):
        return db.session.query(GameUser).filter_by(email=email).scalar()

    @staticmethod
    def find_by_username(username):
        return db.session.query(GameUser).filter_by(username=username).scalar()