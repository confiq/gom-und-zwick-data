from lib.measuring_device import Device


class Gom(Device):
    def __init__(self, file):
        self.encoding = 'UTF-8'
        super().__init__(file)
        self._clear()

    def _clear(self):
        """
        Function that clears the garbage from text so we can make proper CSV from it.
        we just remove first 3 lines
        :return:
        """
        self.fcontent = self.fcontent.split("\n", 3)[3]
