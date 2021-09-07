class Road:
    def __init__(self, dlina, shirina):
     self._dlina = dlina
     self._shirina = shirina

    def massa(self, ydel_massa, tolchina):
         return self._dlina*self._shirina*ydel_massa*tolchina/1000


r = Road(20,5000)
print(r.massa(25,5))
