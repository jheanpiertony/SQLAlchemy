from project.adapters.database_repository_adapter import\
     DataBaseRepositoryAdapter


class Repository(DataBaseRepositoryAdapter):

    __database_session__ = None
    __model__ = None

    def __init__(self, database_session, model):
        self.__model__ = model
        self.__database_session__ = database_session

    def add(self, *parameters):
        entity = self.__model__(*parameters)
        self.__database_session__.add(entity)

    def delete(self, entity):
        self.__database_session__.delete(entity)

    def get(self):
        result = []

        entities =\
            self.__database_session__.query(
                self.__model__)

        for entity in entities:
            result.append(entity)

        self.__database_session__.commit()

        return result

    def update(self, entity):
        self.__database_session__.add(entity)
