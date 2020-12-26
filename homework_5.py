# Exercise_1

with open('my_file.txt', 'w') as file:
    content = True
    while content != '':
        content = input('Введите строку ')
        file.writelines(content + '\n')

# Exercise_2

with open('my_file.txt') as file:
    print(len(file.readlines()))
    file.seek(0)
    for line in file.readlines():
        i = 0
        for word in line.split():
            i += 1
        print(i)

# Exercise_3

averege = 0
i = 0
with open('my_file.txt') as file:
    data = dict((line.split(' ')) for line in file.readlines())
    for num in data.values():
        averege += int(num)
        i +=1
    print('Средняя зарплата:', averege/i)
    for fam, num in data.items():
        if int(num) >= 20000:
            print(fam)

# Exercise_4

with open('number.txt') as num:
    for line in num.readlines():
        if 'One' in line:
            new_line = line.replace('One', 'Один')
            with open('new_numbew.txt', 'w') as new:
                new.write(new_line)
        elif 'Two' in line:
            new_line = line.replace('Two', 'Два')
            with open('new_numbew.txt', 'a') as new:
                new.write(new_line)
        elif 'Three' in line:
            new_line = line.replace('Three', 'Три')
            with open('new_numbew.txt', 'a') as new:
                new.write(new_line)
        elif 'Four' in line:
            new_line = line.replace('Four', 'Четыре')
            with open('new_numbew.txt', 'a') as new:
                new.write(new_line)


# Exercise_5

with open('my_file.txt', 'w+') as file:
    numbers = input('Введите числа через пробел: ')
    file.write(numbers)
    new_numb = numbers.split(' ')
    sum = 0
    for i in new_numb:
        sum = sum + int(i)
    print(sum)


# Exercise_6

import re


my_dict = {}
with open('my_file.txt') as file:
    for line in file.readlines():
        hours = re.findall('\d+', line)
        hours_sum = 0
        for num in hours:
            hours_sum = hours_sum + int(num)
        name = re.findall('\D+\:', line)
        dict = {name[0]:hours_sum}
        my_dict.update(dict)
    print(my_dict)


# Exercise_7

import json


my_dict = {}
my_list = []
with open('my_file.txt') as file:
    for line in file.readlines():
        name, ownership, profit, cost = line.split(' ')
        dict = {name : (int(profit)-int(cost))}
        my_dict.update(dict)
    my_list.append(my_dict)
    sum = 0
    i = 0
    for value in my_dict.values():
        if value > 0:
            sum = sum + value
            i +=1
    dict = {'average_profit':(sum/i)}
    my_list.append(dict)
    print(my_list)

with open('my_file.json', 'w') as file:
    json.dump(my_list, file)