# -*- coding: utf-8 -*-
import json

from My_fuctions import timer
from My_fuctions import value_eror


def menu():
    print("\n\n\t\t\t\t<< ГЛАВНОЕ МЕНЮ КОМПАНИИ >>\n")
    print("\t 1 -- Добавть в файл << Company >> информацию о компании ")
    print("\t 2 -- Вывести на экран информацию о доходности компании  ")
    print("\t 3 -- Сохраннить информации в виде json-объекта          ")
    print("\t 4 -- Выход из системы << Университета >>                ")

def output_info():
    list = []
    with open("Company") as f_obj:
        for line in f_obj:
            list.append(line)
    return list

def create_new_list(list):
    new_list = []
    for i in range(0, len(list)):
        string_of_enum = list[i]
        for j in range(0, len(string_of_enum)):
            words = string_of_enum.split()
        new_list.append(words)
    return new_list


while True:
    menu()
    user_choise = value_eror()
    if user_choise == 1:
        info_list = []
        print("\n\n\t\t\t // ДОБАВЛЕНИЕ КОМПАНИИ В ФАЙЛ << Company >> //\n")
        name_of_company = input("\n\n\t # Введите название компании }==)>                 ")
        info_list.append(name_of_company + " ")
        form_of_ownership = input("\t # Введите форму собственности компании }==)>      ")
        info_list.append(form_of_ownership + " ")
        count_of_income = input("\t # Введите доходы компании в денежном эквиваленте }==)>    ")
        info_list.append(count_of_income + " ")
        count_of_losses = input("\t # Введите убытки компании в денежном эквиваленте }==)>    ")
        info_list.append(count_of_losses + '\n')
        with open("Company", "a") as file:
            file.writelines(info_list)
        print("\n\n\t // Запись данных в файл //")
        timer()
        print("\t Данные успешно записаны ...")
    elif user_choise == 2:
        full_list = output_info()
        new_list = create_new_list(full_list)
        dict_of_income = {}
        dict_of_avarage_price = {}
        count_of_profit_company = 0
        my_list =[]
        lict_of_name = []
        list_of_income = []
        for i in range(0, len(full_list)):
            profit = int(new_list[i][2]) - int(new_list[i][3])
            if profit > 0:
                lict_of_name.append(new_list[i][0])
                list_of_income.append(profit)
                count_of_profit_company += 1
        for i in range(0, len(lict_of_name)):
            dict_of_income[lict_of_name[i]] = list_of_income[i]
        dict_of_avarage_price["average_profit"] = sum(list_of_income)/count_of_profit_company
        my_list.append(dict_of_income)
        my_list.append(dict_of_avarage_price)
        print("\n\n\t // АНАЛИЗ ДОХОДНОСТИ КОМПАНИИ И РЕАЛИЗАЦИЯ СПИСКА //")
        timer()
        print("\n\t // СПИСОК СОСТОЯЩИЙ ИЗ СЛОВАРЯ КОМПАНИЙ С ПОЛОЖИТЕЛЬНОЙ ДОХОДНОСТЬЮ И ИХ СРЕДНЯЯ ПРИБЫЛЬ //\n")
        print("\t\t", my_list)
    elif user_choise == 3:
        print("\n\n\t // Запись данных в my_file.json //")
        with open("my_file.json", "w") as write_f:
            json.dump(my_list, write_f)
        timer()
        print("\t Данные успешно записаны в my_file.json ...")
    elif user_choise == 4:
        break