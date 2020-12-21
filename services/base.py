from abc import ABC, abstractmethod

class dbBase(ABC):

    @abstractmethod
    def open_connection(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self):
        pass

    @abstractmethod
    def get_by_criteria(self):
        pass

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def delete_all(self):
        pass

    @abstractmethod
    def delete_by_id(self):
        pass