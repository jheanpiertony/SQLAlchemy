import abc


class DataBaseRepositoryAdapter():

    @abc.abstractmethod
    def add(self):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self):
        raise NotImplementedError
