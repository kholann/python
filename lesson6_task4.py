# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn(self, direction):
        return f'{self.name} is turned {direction}'

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}')
        if self.speed > 60:
            return f'Speed of {self.name} is higher 60 !!!'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}')
        if self.speed > 40:
            return f'Speed of {self.name} is higher 40 !!!'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

tc = TownCar(70, 'Red', 'TownCar', False)
sc = SportCar(120, 'Black', 'SportCar', False)
wc = WorkCar(50, 'Green', 'WorkCar', False)
pc = PoliceCar(100, 'Black',  'PoliceCar', True)

print(tc.go())
print(tc.turn('right'))
print(tc.show_speed())
print(tc.stop())

print(sc.go())
print(sc.turn('left'))
print(sc.show_speed())
print(sc.stop())

print(wc.go())
print(wc.turn('right'))
print(wc.show_speed())
print(wc.stop())

print(pc.go())
print(pc.turn('left'))
print(pc.show_speed())
print(pc.stop())