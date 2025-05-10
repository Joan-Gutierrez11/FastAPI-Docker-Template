from src.utils import get_current_datetime
from .config import BaseModel as DeclarativeBaseModel

import sqlalchemy as sa

class BaseModel(DeclarativeBaseModel):
    """
    Declaration of base model.
    """
    __tablename__: str = None

class PrimaryKeyIdMixin:
    """
    Add id field of primary key.
    """
    id = sa.Column(sa.BigInteger, autoincrement=True, primary_key=True)

class TimestampsMixin:
    """
    Mixin for add timestamps columns in table
    """
    created_at = sa.Column(sa.types.TIMESTAMP, default=get_current_datetime)
    updated_at = sa.Column(sa.types.TIMESTAMP, onupdate=get_current_datetime, default=None)

class Model(BaseModel, PrimaryKeyIdMixin):
    """
    Declaration of model class. This class contains id field for use like primary key
    """
    ...
