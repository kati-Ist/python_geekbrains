from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def textile(self):
        pass


class Сoat(Clothes):
    @property
    def textile(self):
        print(f"Расход ткани на пальто {round(self.size / 6.5 + 0.5, 2)}")


class Suit(Clothes):
    @property
    def textile(self):
        print(f"Расход ткани на костюм {round(2 * self.size + 0.3, 2)}")


mc = Сoat(10)
mc.textile

mc = Suit(5)
mc.textile
