from lib.device import Device


class Zwick(Device):
    ENCODING = 'ISO-8859-1'  # who on the earth use this 💩 anymore?

    def __init__(self, file):
        super().__init__(file)
        self._clear()

    def _clear(self):
        """
        Function that clears the garbage from text so we can make proper CSV from it.
        :return:
        """
        self.fcontent = self.fcontent.split("\n", 4)[4]
