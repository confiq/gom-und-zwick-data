from lib.measuring_device import Device
from io import StringIO
import csv

class Gom(Device):
    def __init__(self, file):
        super().__init__(file)

    def _clear(self):
        """
        Function that clears the garbage from text so we can make proper CSV from it.
        we just remove first 3 lines
        :return:
        """
        return self.fcontent.split("\n", 3)[3]

    def make_csv(self):

        pass
