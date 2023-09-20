from abc import ABCMeta
from abc import abstractmethod


class BaseService(metaclass=ABCMeta):
    @staticmethod
    def create():
        raise NotImplemented

    @staticmethod
    def bulk_create():
        raise NotImplemented

    @staticmethod
    def get():
        raise NotImplemented

    @staticmethod
    def filter():
        raise NotImplemented

    @staticmethod
    def update():
        raise NotImplemented

    @staticmethod
    def delete():
        raise NotImplemented
