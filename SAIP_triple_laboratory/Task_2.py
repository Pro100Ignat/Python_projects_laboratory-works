# -*- coding: utf-8 -*-
from termcolor import colored, cprint

from My_fuctions import value_eror
from My_fuctions import timer

def check(count_of_lesons, list):
    if not count_of_lesons:
        list.append(" ")
        return False
    else: return True

def create_new_list(list):
    new_list = []
    for i in range(0, len(list)):
        string_of_enum = list[i]
        for j in range(0, len(string_of_enum)):
            words = string_of_enum.split()
        new_list.append(words)
    return new_list

def menu():
    print("\n\n\t\t\t    << ГЛАВНОЕ МЕНЮ КИНОТЕАТРА >>\n")
    print("\t 1 -- Добавть в файл << Cinema >> информацию о сеансе                  ")
    print("\t 2 -- Вывести на экран все фильмы, за указанную вами стоимость         ")
    print("\t 3 -- Вывести на экран все фильмы за определенную дату                 ")
    print("\t 4 -- Вывести на экран все фильмы доступные в файле << Cinema >>       ")
    print("\t 5 -- Выход из системы << Кинотеатра >>                                ")
    print("\t Ваш выбор . . .                                                     ")

def output_info():
    list = []
    with open("Cinema") as f_obj:
        for line in f_obj:
            list.append(line)
    return list

while True:
    menu()
    user_choise = value_eror()
    if user_choise == 1:
        info_list = []
        print("\n\n\t\t // ДОБАВЛЕНИЕ ФИЛЬМА В ФАЙЛ << Cinema >> //")
        name_of_film = input("\n\n\t # Введите название фильма }==)> ")
        info_list.append(name_of_film + " ")
        film_data = input("\t # Введите дату сеанса // пример ввода: 12.06.2004 //  }==)> ")
        info_list.append(film_data + " ")
        prise_of_film = input("\t # Введите цену билета }==)> ")
        info_list.append(prise_of_film + '\n')
        with open("Cinema", "a") as file:
            file.writelines(info_list)
        print("\n\n\t // Запись данных в файл //")
        timer()
        print("\t Данные успешно записаны ...")

    elif user_choise == 2:
        full_list = output_info()
        new_list = create_new_list(full_list)
        count_of_films = 0
        print("\n\t\t  // Введите начальное значение ценовой категории фильмов, которые хотите посмотреть //")
        my_price = value_eror()
        print("\n\n\t\t // Поиск сеансов, с заданной ценовой котегорией //")
        timer()
        print("\n\n\t\t // ВАШЕМУ ВНИМАНИЮ ПРЕДОСТОВЛЯЮТЬСЯ СЛЕДУЮЩИЕ ФИЛЬМЫ //")
        for i in range(0, len(full_list)):
            if int(new_list[i][2]) > my_price:
                print("\n\t Фильм №", colored(i + 1, 'red'), " ==> //   Название  // --- ",
                      colored(new_list[i][0], 'green'))
                print("\t\t\t\t    // Дата сеанса // --- ", colored(new_list[i][1], 'green'))
                print("\t\t\t\t    // Цена билета // --- ", colored(new_list[i][2], 'green'))
                count_of_films += 1
        if count_of_films == 0:
            print(" \n\t Фильмов с заданной ценовой категорией нет в файле << Cinema >>")

    elif user_choise == 3:
        full_list = output_info()
        new_list = create_new_list(full_list)
        count_of_films = 0
        print("\n\t\t // Введите точную дату просмотра фильма //")
        my_price = input("\n\t Поле ввода значений ==> ")
        print("\n\n\t\t // Поиск сеансов, по дате показа фильма //")
        timer()
        print("\n\n\t\t ВАШЕМУ ВНИМАНИЮ ПРЕДОСТОВЛЯЮТЬСЯ СЛЕДУЮЩИЕ ФИЛЬМЫ ")
        for i in range(0, len(full_list)):
            if new_list[i][1] == my_price:
                print("\n\t Фильм №", colored(i + 1, 'red'), " ==> //   Название  // --- ",
                      colored(new_list[i][0], 'green'))
                print("\t\t\t\t    // Дата сеанса // --- ", colored(new_list[i][1], 'green'))
                print("\t\t\t\t    // Цена билета // --- ", colored(new_list[i][2], 'green'))
                count_of_films += 1
        if count_of_films == 0:
            print(" \n\t\t Фильмов с заданной ценовой категорией нет в файле << Cinema >>")

    elif user_choise == 4:
        full_list = output_info()
        new_list = create_new_list(full_list)
        print("\n\n\t\t // ПОЛНЫЙ СПИСОК ФИЛЬМОВ, ДОСТУПНЫХ ДЛЯ ПРОСМОТРА // ")
        for i in range(0, len(full_list)):
            print("\n\t Фильм №", colored(i + 1, 'red'), " ==> //   Название  // --- ",
                  colored(new_list[i][0], 'green'))
            print("\t\t\t\t    // Дата сеанса // --- ", colored(new_list[i][1], 'green'))
            print("\t\t\t\t    // Цена билета // --- ", colored(new_list[i][2], 'green'))
    elif user_choise == 5:
        break