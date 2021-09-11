from abc import ABC, abstractmethod

class clothes(ABC):

    @abstractmethod
    def consumption(self):
        pass

class coat(clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        consumption_coat = self.v / 6.5 + 0.5
        return round(consumption_coat,2)

class costume(clothes):
    def __init__(self, h):
        self.h = h
    @property
    def consumption(self):
        consumption_costume = self.h * 2 + 0.3
        return round(consumption_costume,2)

a = coat(5)
b = costume(2)
print(f'{a.consumption} расход ткани на пальто')
print(f'{b.consumption} расход ткани на костюм')










