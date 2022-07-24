from abc import ABC, abstractmethod
from collections import UserDict

class SomeBook(ABC, UserDict):
    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass
    
    @abstractmethod
    def add_record(self, record): 
        pass

    @abstractmethod
    def delete_record(self, name):
        pass

    @abstractmethod
    def update_record(self, name, value):
        pass

    @abstractmethod
    def to_find(self, name):
        pass

class Record(ABC):
    @abstractmethod
    def add_address(self):
        pass

    @abstractmethod
    def add_birthday(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class NoteBookRecord(ABC):
    @abstractmethod
    def add_teg(self):
        pass

    @abstractmethod
    def del_teg(self):
        pass
    
    @abstractmethod
    def __repr__(self):
        pass

class Field(ABC):
    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    @abstractmethod 
    def value(self, value):
        pass

if __name__=="__main__":
    pass
