# Exercise_1

def division(*args):
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    if b == 0:
        return ('На ноль делить нельзя!')
    else:
        return(a/b)


print(division())

# Exercise_2

def people_data(*kwargs):
    data = {'Имя' : input('Введите имя: '),
            'Фамилия' : input('Введите фамилию: '),
            'Год рождения' : input('Введите год рождения: '),
            'Город проживания' : input('Введите город проживания: '),
            'email' : input('Введите email: '),
            'Телефон' : input('Введите телефон: ')
    }

    return str(data)

# Exercise_3

def my_func():
    list = [
        int(input('Введите 3 числа: ')),
        int(input('Осталось 2 числа: ')),
        int(input('Введите последнее число: '))
    ]
    list.sort()
    list.pop(0)
    answer = list[0] + list[1]
    return(answer)

# Exercise_4

def my_func(x, y):
    return x**y


def my_func_1(x, y):
    result = 1
    for i in range(y, 0):
        result = result / x
    return result

# Exercise_5

def numbres_sum():
    item = 0
    sum_num = 0
    while item != 'q':
        numbers_list = input('Введите числа через пробел. Если хотите выйти нажмите q ').split(' ')
        for item in numbers_list:
            if item == 'q':
                print(sum_num)
                return
            else:
                sum_num = sum_num + int(item)
        print(sum_num)


# Exercise_6

def int_func():
    text = input('Введите несколько слов с маленькой буквы: ').split(' ')
    new_text = []
    for item in text:
        new_text.append(item.capitalize())
    return (new_text)