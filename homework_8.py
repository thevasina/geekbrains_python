# Exercise_1

class Data:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year


    @classmethod
    def new_data(cls, data):
        day, month, year = map(int, data.split('-'))
        return day, month, year

    @staticmethod
    def valid_numbers(day, month, year):
        if int(day) not in range(1,32):
            return 'Неверное число дня'
        if int(month) not in range(1,13):
            return 'Неверное число месяца'
        if year not in range(1500, 3001):
            return 'Неверное число года'
        else:
            return 'Все верно'


date1 = Data.new_data('2-13-2020')
print(date1)
date2 = Data.valid_numbers(2, 13, 2020)
print(date2)
date3 = Data.valid_numbers(0, 11, 2020)
print(date3)
date4 = Data.valid_numbers(2, 10, 3001)
print(date4)
date5 = Data.valid_numbers(2, 12, 2020)
print(date5)


# Exercise_2

import sys


class ZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = int(input('Введите делимое: '))
except ValueError:
    print('Надо ввести число! Попробуйте запустить програаму заново')
    sys.exit('Попробуйте еще раз')
try:
    b = int(input('Введите делитель: '))
    if b == 0:
        raise ZeroDivision('На ноль делить нельзя!')
except ZeroDivision as arr:
        print(arr)

except ValueError:
    print('Надо ввести число! Попробуйте запустить програаму заново')
    sys.exit('Попробуйте еще раз')
else:
    print(a/b)

# Exercise_3

class NotAnInt(Exception):
    def __init__(self, text):
        self.text = text


    @classmethod
    def check_type(cls, num):
        try:
            int(num)
        except ValueError:
            raise cls('Вы ввели не число')


numbers = []
while True:
    num = input('Введите число: ')
    if num == 'stop':
        break
    try:
        NotAnInt.check_type(num)
    except NotAnInt as err:
        print(err)
    else:
        numbers.append(num)
print(numbers)


# Exercise_4

class Storage:
    def __init__(self, adress, capacity):
        self.adress = adress
        self.capacity = capacity
        self.list_of_equipment = {}

    def add_equipment(self, item, count):
        try:
            int(count)
        except ValueError:
            print('Количество должно быть числом!')
            return
        else:
            self.list_of_equipment[item] = count

    def leave_equioment(self, item, count):
        amount = self.list_of_equipment[item]
        if count > amount:
            print('Недостаточно техники на складе')
        elif count == amount:
            self.list_of_equipment.pop(item)
            print('Вы забрали все!')
        else:
            self.list_of_equipment[item] = amount-count
            print(f'Вы забрали {count}, на складе осталось {amount-count}')

class Equipment:
    def __init__(self, year, firm, type):
        self.year = year
        self.firm = firm
        self.type = type
        self.department = None


class Printer(Equipment):
    def __init__(self, year, firm):
        type = 'Printer'
        super().__init__(year, firm, type)


class Scanner(Equipment):
    def __init__(self, year, firm):
        type = 'Scanner'
        super().__init__(year, firm, type)


class Xerox(Equipment):
    def __init__(self, year, firm):
        type = 'Xerox'
        super().__init__(year, firm, type)


s = Storage('adress', 20)
pr = Printer(2000, 'hp')

s.add_equipment(pr, 20)
s.leave_equioment(pr, 40)
s.leave_equioment(pr, 15)
s.leave_equioment(pr, 5)

xer = Xerox(2020, 'Xerox')
s.add_equipment(xer, 'sdsd')


# Exercise_5

class Complex():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return  f'{self.num1 + other.num1} + {self.num2 + other.num2}i'

    def __mul__(self, other):
        return f'{(self.num1 * other.num1) - (self.num2 * other.num2)} +' \
               f' {(self.num2 * other.num1) + (self.num1 * other.num2)}i'

    def __str__(self):
        return f'{self.num1} + {self.num2}i'


a1 = Complex(4,55)
a2 = Complex(6,22)
print(a1 + a2)
print(a1 * a2)
print(a1)
print(a2)

