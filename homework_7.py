# Exercise_1

class Matrix:
    def __init__(self, list1):
        self.matriks = list1

    def __str__(self):
        return '\n'.join(str(el).strip('[]').replace(',', ' ') for el in self.matriks )

    def __add__(self, other):
        try:
            rows_count = len(self.matriks)
            columns_count = len(self.matriks[0])
            result = []
            for i in range(0, rows_count):
                temp = []
                for j in range(columns_count):
                    temp.append(self.matriks[i][j] + other.matriks[i][j])
                result.append(temp)
            return Matrix(result)
        except IndexError:
            return 'Матрицы разного размера'

a = Matrix([[1,3,4],[6,7,8]])
b = Matrix([[1,1,1],[1,1,1]])
print(a + b)

# Exercise_2

from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def fabric_req(self):
        pass


class Coat(Clothes):

    def __init__(self, H):
        self.height = H

    @property
    def fabric_req(self):
        return f'На пальто потребуется {round(self.height/6.5 + 0.5)} квадратный метров ткани'

class Suite(Clothes):

    def __init__(self, V):
        self.size = V

    @property
    def fabric_req(self):
        return f'На костюм потребуется {self.size*2 + 0.3} квадратный метров ткани'

class All_Fabric(Clothes):
    def __init__(self, V, H):
        self.size = H
        self.height = V


    def fabric_req(self):
        return f'Общее количество ткани составит {round((self.size*2 + 0.3) + (self.height/6.5 + 0.5))}' \
               f' квадратных метров ткани'



my_coat = Coat(170)
print(my_coat.fabric_req)
my_suite = Suite(40)
print(my_suite.fabric_req)
all_fab = All_Fabric(170, 40)
print(all_fab.fabric_req())


# Exercise_3

class Cell:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            return 'Разница количества ячеек меньше нуля'

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, other, amount):
        a = other.num // amount
        b = other.num % amount
        if b == 0:
            return ('*' * amount + '\n') * a
        else:
            return ('*' * amount + '\n') * a + ('*' * b)


c = Cell(10)
a = Cell(12)
print(c.num)
print(c + a)
print(c - a)
print(a - c)
print(a * c)
print(c / a)
print(c.make_order(a, 5))