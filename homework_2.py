# Exercise_1

my_list = [42, 'name', [1,2,3], 5.6, {1,3,5}, (2,5,7)]

for item in my_list:
    print(type(item))

# Exercise_2

my_list = []
count = int(input('Вам надо будет вводить числа. Сколько чисел вы введете? '))
while count != 0:
    item = input('Введите число: ')
    my_list.append(item)
    count -= 1

print(my_list)
i = 0
for element in range(int(len(my_list)/2)):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i += 2

print(my_list)

# Exercise_3

my_dict = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}

month = int(input('Введите номер месяца от 1 до 12: '))
print('Вы выбрали {}'.format(my_dict.get(month)))

my_list = [
    'Январь',
    'Февраль',
    'Март',
    'Апрель',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
    'Декабрь'
]

month = int(input('Введите номер месяца от 1 до 12: '))
print('Вы выбрали {}'.format(my_list[month-1]))

# Exercise_4

my_string = input('Введите несколько слов через пробел и какое то очень длинное: ')

my_list = my_string.split(' ')
print(my_list)
count = 1
for item in my_list:
    if len(item) >10:
        item = item[:10]
    print('{}: {}'.format(count, item))
    count +=1

# Exercise_5

my_list = [7, 5, 3, 3, 2]
number = int(input('Введите целое число: '))
was_add = False
for item in my_list:
    if number > item:
        my_list.insert(my_list.index(item), number)
        was_add = True
        break
if was_add == False:
    my_list.append(number)


print(my_list)

# Exercise_66

my_list = []
my_dict = {}
count = 1
analitica = {}
list_name=[]
list_price=[]
list_amount=[]
list_unit = []
while True:
    my_dict = dict()
    name_item = input('Введите название товара: ')
    my_dict['Название'] = name_item
    list_name.append(name_item)
    price_item = input('Введите цену товара: ')
    my_dict['Цена'] = price_item
    list_price.append(price_item)
    amount_item = input('Введите количество товара: ')
    my_dict['Количество'] = amount_item
    list_amount.append(amount_item)
    unit_item = input('Введите в чем измеряется количество товара: ')
    my_dict['Единица измерения'] = unit_item
    if unit_item in list_unit:
        pass
    else:
        list_unit.append(unit_item)
    my_list.append((count, my_dict))
    add = input('Вы хотите ввести еще один товар? Да/Нет ')
    if add == str.lower('Нет'):
        break
    count +=1
print(my_list)
analitica = {'Название': list_name, 'Цена': list_price, 'Количество': list_amount, 'Единица измерения': list_unit}
print(analitica)