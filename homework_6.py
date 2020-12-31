# Exercise_1

from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(4)

traf = TrafficLight()
print(traf.running())


# Exercise_2

class Road:
    weight = 25  # масса одного квадратного метра толщиной в 1 см
    thick = 5  # стандартная толщина полотна

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self):
        return self._length * self._width * self.weight * self.thick


a = Road(4,5)
print(a.massa())


# Exercise_3

class Worker:
    def __init__(self, name, surname, position, income, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income
        self._money = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'


    def get_total_income(self):
        summa = self._money['bonus'] + self._money['wage']
        return f'Общий доход составляет: {summa}'



w = Position('Иван', 'Васильевич', 'менеджер', 2, 10, 4)
print(w.get_full_name())
print(w.get_total_income())
print(w.position)
print(w.income)
# Иван Васильевич меняет профессию
w.position = 'царь'
print(w.position)


# Exercise_4

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала!'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        return f'Машина повернула {direction}'

    def show_speed(self):
        return f'Скорость автомобиля: {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, is_police):
        name = 'car_for_mommy'
        super().__init__(speed, color, name,  is_police)


    def show_speed(self):
        if self.speed >= 60:
            return 'Нарушать не хорошо! Сбавьте скорость!'
        else:
            return f'Скорость автомобиля: {self.speed}'

class SportCar(Car):
    def __init__(self, speed, name, is_police):
        color = 'RED'
        super().__init__(speed ,color, name, is_police)

    def show_speed(self):
        if self.speed < 100:
            return 'Это же спортивная машина! Прибавь.'
        else:
            return f'Скорость автомобиля: {self.speed}'

class WorkCar(Car):
    def __init__(self, speed, color, is_police):
        name = 'cleaner_car'
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'Нарушать не хорошо! Сбавьте скорость!'
        else:
            return f'Скорость автомобиля: {self.speed}'

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        is_police = True
        super().__init__(speed, color,name, is_police)

    def police(self):
        if self.is_police:
            return 'Полиция!'


volvo = TownCar(65, 'white', False)
print(volvo.show_speed())
print(volvo.name)
print(volvo.turn('left'))

audi = SportCar(95, 'audi', False)
print(audi.show_speed())
print(audi.color)
print(audi.turn('right'))

niva = WorkCar(40, 'blue', False)
print(niva.turn('в никуда'))
print(niva.show_speed())
print(niva.name)

skoda = PoliceCar(70, 'white', 'skoda')
print(skoda.is_police)
print(skoda.police())
print(skoda.color)
print(skoda.name)
print(skoda.show_speed())


# Exercise_5

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):

    def draw(self):
        return 'Пишу ручкой'

class Pencil(Stationery):

    def draw(self):
        return 'Делаю эскиз карандашом'

class Handle(Stationery):

    def draw(self):
        return 'Выделяю маркером'

s = Stationery('paints')
print(s.draw())

p = Pen('pen')
print(p.draw())

pn = Pencil('Pencil')
print(pn.draw())

h = Handle('handle')
print(h.draw())