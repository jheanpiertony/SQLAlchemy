from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from project.configuration_manager import ConfigurationManager
from project.resources.decorators.singleton_decorator import singleton
from project.resources.utils.generals_utils import GeneralsUtils


@singleton
class PostgreSqlContext():

    __session__ = None

    def __init__(self, database_connection_name, database_api="pg8000"):
        database_connection_parameters =\
            ConfigurationManager.get_config(database_connection_name)
        password = GeneralsUtils.decode(
            database_connection_parameters['PASSWORD'])

        database_connection_string = f"postgresql+{database_api}://" +\
            f"{database_connection_parameters['USER']}:" +\
            f"{password}" +\
            f"@{database_connection_parameters['HOST']}" +\
            f":{database_connection_parameters['PORT']}" +\
            f"/{database_connection_parameters['NAME']}"

        engine = create_engine(database_connection_string)

        self.__session__ = scoped_session(sessionmaker(bind=engine))

    def get_session(self):
        return self.__session__

    def commit(self):
        try:
            yield self.__session__
            self.__session__.commit()

        except Exception as error:
            self.__session__.rollback()
            raise error

        finally:
            self.__session__.close()
            self.__session__.bind.dispose()
