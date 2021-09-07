class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police

    def go(self):
        print("60!")

    def stop(self):
        print("Stop")

    def turn(self, direction):
        print(f"Автомобиль повернул {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.speed}")

class TownCar (Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышена скорость 60 км/ч")

class SportCar(Car):
    pass

class WorkCar (Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышена скорость 40 км/ч")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

town = TownCar(90, "green", "Town")
sport = SportCar(120, "red", "Sport")
work = WorkCar(41, "yellow", "Work")
police = PoliceCar(100, "blue", "Police")

town.show_speed()
work.show_speed()

work.speed = 30
work.show_speed()

police.turn("налево")

