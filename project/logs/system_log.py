from datetime import datetime

from project.adapters.database_repository_adapter import\
    DataBaseRepositoryAdapter
from project.infrastructure.repositories.log_repository import LogRepository
from project.models.models import LogModel


class SystemLog():

    __database_session__ = None
    __log_repository__ = None
    logs = []

    def __init__(
            self,
            database_session: DataBaseRepositoryAdapter):
        self.__database_session__ = database_session
        self.__log_repository__ = LogRepository(self.__database_session__)

    def add(self, message, level="Error", to_save=True):
        log = {
            "message": message,
            "level": level,
            "date_stamp": datetime.utcnow()
        }

        print(message)

        self.logs.append(log)

        if to_save:
            self.__log_repository__.add(LogModel(**log))
            self.__database_session__.commit()
