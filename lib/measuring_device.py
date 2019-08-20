from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self, file):
        self.file = file
        self.csv = None
        super().__init__()

    @abstractmethod
    def make_csv(self):
        pass