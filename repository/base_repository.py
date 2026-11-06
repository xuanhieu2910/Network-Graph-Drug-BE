from typing import Any, Optional, TypeVar, Generic
from abc import ABC, abstractmethod
from pydantic import BaseModel
T = TypeVar('T', bound=BaseModel)

class BaseRepository(Generic[T]):

    def __init__(self, connection, model: type[T]):
        self.connection = connection
        self.model = model

    @abstractmethod
    def get_by_id(self, id: str) -> T:
        pass

    @abstractmethod
    def get_all(self) -> list[T]:
        pass

    @abstractmethod
    def create(self, obj: T) -> T:
        pass

    @abstractmethod
    def delete(self, obj: T) -> None:
        pass

    def _query_one(self, 
                   sql: str,
                   params: Optional[dict[str, Any]] = None) -> T:
        
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            row = cursor.fetchone()

        if row is None:
            return None

        return self.model.model_validate(row)

    def _query_all(
        self,
        sql: str,
        params: Optional[dict[str, Any]] = None
    ) -> list[T]:

        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            rows = cursor.fetchall()
        return [
            self.model.model_validate(row)
            for row in rows
        ]

    def _execute(
        self,
        sql: str,
        params: Optional[dict[str, Any]]  = None
    ) -> None:

        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
    