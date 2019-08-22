from lib.measuring_device import Device

class Zwick(Device):
    def __init__(self, file):
        self.encoding = 'ISO-8859-1'  # who in 21 century don't use unicode anymore?
        super().__init__(file)
        self._clear()

    def _clear(self):
        """
        Function that clears the garbage from text so we can make proper CSV from it.
        :return:
        """
        self.fcontent = self.fcontent.split("\n", 4)[4]
