# Exercise_1

from sys import argv

script, sal, hour, bonus = argv
print((float(hour) * float(sal)) + float(bonus))

# Exercise_2

list_n = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list_n[i+1] for i in range(len(list_n)-1) if list_n[i+1] > list_n[i]]
print(new_list)

# Exercise_3

my_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(my_list)

# Exercise_4

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

# Exercise_5

from functools import reduce

my_list = [el for el in range(99, 1001) if el % 2 == 0]

def my_func(prev_el, el):
    return prev_el*el

print(reduce(my_func, my_list))

# Exercise_6

from itertools import count, cycle

start = int(input('Введите начальное число: '))
end = int(input('Введите конечное число: '))

for el in count(start):
    if el > end:
        break
    else:
        print(el)

repeat_count = int(input('Введите количество повторений: '))
count = 1

for el in cycle('Happy new year'):
    if count > repeat_count:
        break
    else:
        print(el)
        count +=1


# Exercise_7

from math import factorial


def fact(num):
    for i in range(1, num + 1):
        yield factorial(i)

count = int(input('Введите количество чисел: '))
print([el for el in fact(count)])