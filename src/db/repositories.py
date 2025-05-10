from typing import Any, Generic, TypeVar, List, get_args
from abc import ABC, ABCMeta, abstractmethod

from src.db.config import SessionDependency

import sqlalchemy as sa

from src.db.models import BaseModel

T = TypeVar("T", bound=BaseModel)

class AbstractRepository(ABC, Generic[T], metaclass=ABCMeta):

    def __init__(self, db: SessionDependency):
        self.db = db

    def __init_subclass__(cls):
        cls._model_type = get_args(cls.__orig_bases__[1])[0]
        return super().__init_subclass__()

    @abstractmethod
    def get_by_id(self, id: Any) -> T:
        """ Get model instance by id """
        ...
    @abstractmethod
    def all(self) -> List[T]:
        """ Get all model instances """
        ...

class BaseModelRepository(AbstractRepository[T]):
    
    def get_by_id(self, id):
        return self.db.query(self._model_type)\
            .filter(id=id).first()

    def all(self):
        return self.db.query(self._model_type).all()