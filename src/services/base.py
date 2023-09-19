from abc import ABCMeta, abstractmethod


class BaseService(metaclass=ABCMeta):

    @abstractmethod
    def create(self):
        raise NotImplemented

    @abstractmethod
    def bulk_create(self):
        raise NotImplemented

    @abstractmethod
    def get(self):
        raise NotImplemented

    @abstractmethod
    def filter(self):
        raise NotImplemented

    @abstractmethod
    def update(self):
        raise NotImplemented

    @abstractmethod
    def delete(self):
        raise NotImplemented
