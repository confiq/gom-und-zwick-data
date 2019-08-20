from lib.measuring_device import Device


class Gom(Device):
    def __init__(self, file):
        super().__init__(file)

    def _clear(self):
        """
        Function that clears the garbage from text so we can make proper CSV from it
        :return:
        """
        pass

    def make_csv(self):

        pass
