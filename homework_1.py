# Exercise_1

first_var = 11
second_var = 'some text'
print(first_var)
print(second_var)

user_first_var = input('Введите любой текст: ')
user_second_var = input('Введите любое число: ')
print(user_first_var)
print(user_second_var)

# Exercise_2

seconds = int(input('Введите количество секунд: '))
hours = seconds//3600
minutes = (seconds%3600)//60
secods_left = seconds%60
print(f'{hours} часов, {minutes} минут, {secods_left} секунд')

# Exercise_3

number = input('Введите число: ')
print(int(number) + int(number*2) + int(number*3))

# Exercise_4

number = input('Введите целое положительное число: ')
length = len(number)
i = 1
max_el = number[0]
while i < length:
    if number[i] > max_el:
        max_el = number[i]
    i +=1
print(max_el)

# Exercise_5

earn = int(input('Введите сколько вы заработали: '))
spend = int(input('Введите сколько вы потратили: '))
result = earn - spend
if result > 0:
    print(f'Поздравлю, вы в плюсе! Вы заработали {result}')
    staf = int(input('Сколько у вас сотрудников? '))
    per_person = result/staf
    print(f'Прибыль фирмы в рассчете на сотрудника составляет {per_person} ')
else:
    print(f'Ваши убытки составляют {-result}')

# Exercise_6

distance = int(input('Введите сколько спортсмен пробедал за первый день? '))
req_result = int(input('Введите желаемый результат: '))
count = 1

while distance < req_result:
    distance = distance + (distance * 0.1)
    count += 1

print(f'Через {count} дней спорсмен пробежит не менее {req_result} киллометров.')