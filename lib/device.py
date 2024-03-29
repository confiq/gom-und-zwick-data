from abc import ABC, abstractmethod
import logging
from io import StringIO
import csv
import locale

class Device(ABC):
    ENCODING = 'UTF-8'

    def __init__(self, file):
        super().__init__()
        logging.debug(f"Loading {self.__class__.__name__} object ...")
        self.file_name = file
        self.csv = []
        self.fcontent = self.file_get_contents(file)  #bad, but we don't care about memory/speed for now


    @abstractmethod
    def _clear(self):
        pass

    def file_get_contents(self, filename):
        logging.debug(f'opening file {filename} with {self.ENCODING}')
        with open(filename, encoding=self.ENCODING) as f:
            return f.read()

    def load_csv(self, delimiter=";"):
        logging.debug(f'Loading CSV for file {self.file_name}')
        f = StringIO(self.fcontent)
        for idx, row in enumerate(csv.reader(f, delimiter=delimiter)):
            try:
                converted_row = list(map(locale.atof, row))
            except ValueError as e:
                logging.warning(f'Could not convert a row in file {self.file_name}:{idx} with values {row} to float.'
                                f'The message is: {e}. - Ignoring the row')
                continue
            self.csv.append(converted_row)

    def get_max_row(self, column_number):
        max_value = (0, 0)
        for idx, row in enumerate(self.csv):
            if max_value[1] <= row[column_number]:
                max_value = (idx, row[column_number])
        logging.debug(f"max value for {self.__class__.__name__} is {max_value[1]} at row number {max_value[0]}")
        return max_value
