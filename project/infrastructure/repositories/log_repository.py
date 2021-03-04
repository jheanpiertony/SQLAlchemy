from project.infrastructure.repositories.repository import Repository
from project.models.models import LogModel


class LogRepository(Repository):

    __database_session__ = None

    def __init__(self, database_session):
        self.__database_session__ = database_session
        super().__init__(
            database_session=database_session,
            model=LogModel)

    def add(self, log: LogModel):
        self.__database_session__.add(log)
