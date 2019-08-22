from abc import ABC, abstractmethod
import logging
from io import StringIO
import csv
import locale

class Device(ABC):
    def __init__(self, file):
        logging.info(f"Loading {self.__class__.__name__} object ...")
        self.file_name = file
        self.csv = []
        super().__init__()
        self.fcontent = self.file_get_contents(file)  #bad, but we don't care about memory/speed for now


    @abstractmethod
    def _clear(self):
        pass

    def file_get_contents(self, filename):
        logging.debug(f'opening file {filename} with {self.encoding}')
        with open(filename, encoding=self.encoding) as f:
            return f.read()

    def load_csv(self, delimiter=";"):
        f = StringIO(self.fcontent)
        for row in csv.reader(f, delimiter=delimiter):
            self.csv.append(list(map(locale.atof, row)))

    def get_max_row(self, column_number):
        max_value = (0, 0)
        for idx, row in enumerate(self.csv):
            if max_value[1] <= row[column_number]:
                max_value = (idx, row[column_number])
        return max_value