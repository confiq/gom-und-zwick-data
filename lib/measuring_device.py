from abc import ABC, abstractmethod
import logging

class Device(ABC):
    def __init__(self, file):
        logging.debug(f"Loading {self.__class__.__name__} object ...")
        self.file_name = file
        self.fcontent = self.file_get_contents(file)  #bad, but we don't care about memory/speed for now
        self.csv = None
        super().__init__()

    @abstractmethod
    def make_csv(self):
        pass

    @staticmethod
    def file_get_contents(filename):
        with open(filename) as f:
            return f.read()
