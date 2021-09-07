from time import sleep

class TrafficLight:
    color = ("красный","желтый","зеленый")
    time_out=(7,2,5)

    def __init__(self):
        self.__color = 'зеленый'
    def running(self):
        while True:
            for i in self.color:
                self.__color = i
                print(self.__color)
                sleep(self.time_out[self.color.index(self.__color)])

trafic_light=TrafficLight()
trafic_light.running()


