# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

import random


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f"The {self.color} {self.name} started to drive")

    def stop(self):
        print(f"The {self.color} {self.name} stopped to drive")

    def turn(self):
        print(
            f"The {self.color} {self.name} turn " + random.choice(["to the left", "to the right", "on 180", "on 360"]))

    def show_speed(self):
        print(f"The {self.color} {self.name} is going {self.speed} kilometers an hour.")


# 60 (TownCar) и 40 (WorkCar)
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"The {self.color} {self.name} exceeded the speed limit")
        else:
            print(f"The {self.color} {self.name} is going {self.speed} kilometers an hour.")


class SportCar(Car):
    def show_speed(self):
        if self.speed < 200:
            print("Why buy a cool car and drive like a pensioner?")
        else:
            print("The brakes were invented by cowards")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"The {self.color} {self.name} exceeded the speed limit")
        else:
            print(f"The {self.color} {self.name} is going {self.speed} kilometers an hour.")


class PoliceCar(Car):
    def good_man(self):
        if self.is_police is True:
            if self.speed < 60:
                print("Nice shift, quiet, calm")
            else:
                print("Again this crazy guy on SportCar")
        else:
            print("Get another car")


a = Car(100, "green", "Mazda")
a.go()
a.stop()
a.turn()
a.show_speed()

a = TownCar(50, "red", "Suzuki")
a.show_speed()

a = WorkCar(70, "white", "Toyota")
a.show_speed()

a = SportCar(200, "black", "Porsche")
a.show_speed()

a = PoliceCar(200, "black and white", "Ford", True)
a.good_man()
