from random import randint
import random

def value_eror():
    while True:
        try:
           number = int(input("\n\tВвод данных ==>"))
           break
        except:
            print("\t  Проверьте вводимые данные и повторите попытку . . .")
    return number


def menu():
    print("\n\n\t\t << Меню выбора функции >>"
          "\n\t1 -- Генерация словаря с заданной хеш функцией "
          "\n\t2 -- Генерация случайного списка               "
          "\n\t3 -- Генерация случайного числа                "
          "\n\t4 -- Генерация случайной строки                "
          "\n\t5 -- Выход из программы ==> Exit               "
          "\n\t Ваш выбор . . .                             ")

def first_function():
    print("\n\n\t Введите количество ключей в вашем словаре . . .")
    count_of_dictionary = value_eror()
    dictionary = {}
    dictionary = {a: 9 - a ** 2 for a in range(count_of_dictionary)}
    print("\t Случайно сгенерированный словарь ==> ", dictionary)
    mas_of_max = []
    mas_of_max = sorted(dictionary, key=dictionary.get)[-3:]
    print("\n\t Массив трёх ключей словаря имеющих максимальные значения == >", mas_of_max)
    print("\t [1] эллемент массива ==> ключ со значением", mas_of_max[0], "-- третье место по величине значения")
    print("\t [2] эллемент массива ==> ключ со значением", mas_of_max[1], "-- второе место по величине значения")
    print("\t [3] эллемент массива ==> ключ со значением", mas_of_max[2], "-- первое место по величине значения")

def second_function():
    my_list = []
    print("\n\t\t Сколько символов вы хотите увидеть в вашем списке . . .")
    count = value_eror()
    for i in range(0, count):
        my_list.append(randint(-10, 10))
    print("\t Случайно сгенерированный список ==> ", my_list)
    count_of_even = 0
    for i in range(0, count):
        if my_list[i] % 2 == 0:
            count_of_even += 1
    new_list = sorted(set(my_list), key=lambda d: my_list.index(d))
    print("\n\tИтоговый список, состоящий только из уникальных эллементов ==>", new_list)
    print("\tВ случайно сгенерированном списке, чётных элеементов ==>  ", count_of_even)

def triple_function():
    my_number = randint(0, 100000)
    print("\t Случайно сгенерированное число ==> ", my_number)
    suma = 0
    while my_number > 0:
        digit = my_number % 10
        suma = suma + digit
        my_number = my_number // 10
    print("\t Сумма цифр случайно сгенерированного числа ==>", suma)

def fourth_function():
    my_string = " "
    list = [" Каша "," Солнце "," Месяц ","    ","   Луна"," камень"," вторая "," лаба "," Учим "," Python "," (-_-) "]
    for i in range(5):
        my_string = my_string + random.choice(list)
    print("\n\t\t  Случайно сгенерированная строка из массива слов ==>  ",my_string)
    correct_string = " ".join(my_string.split())
    print("\n\t\t  Отредактированная строка без лишних пробелов ==> ",correct_string)
    count_of_words = correct_string.count(' ') + 1
    print("\t Количество слов в строке ==>  ",count_of_words)

while True:
    menu()
    choise = value_eror()
    if choise == 1:
        first_function()
    elif choise == 2:
        second_function()
    elif choise == 3:
        triple_function()
    elif choise == 4:
        fourth_function()
    elif choise == 5:
        break