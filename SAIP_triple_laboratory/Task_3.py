# -*- coding: utf-8 -*-

from My_fuctions import value_eror
from My_fuctions import timer

def menu():
    print("\n\n\t\t\t\t<< ГЛАВНОЕ МЕНЮ УНИВЕРСИТЕТА >>\n")
    print("\t 1 -- Добавть в файл << University >> информацию о предмете ")
    print("\t 2 -- Вывести на экран все предметы и кол-во часов ")
    print("\t 3 -- Выход из системы << Университета >>")

def check(count_of_lesons, list):
    if not count_of_lesons:
        list.append(" ")
        return False
    else: return True


def find_name_of_subject(list):
    list_of_subjects = []
    for i in range(0, len(list)):
        subject = ""
        for j in range(0, len(list[i])):
            if list[i][j] == ':':
                break
            else:
                subject += list[i][j]
        list_of_subjects.append(subject)
    return list_of_subjects

def find_hours_of_subject(list):
    list_hours_of_subjects = []
    for i in range(0, len(list)):
        sum = 0
        str_hours = ""
        for j in range(0, len(list[i])):
            if list[i][j].isdigit() == True:
                str_hours += list[i][j]
            else:
                if str_hours != "":
                    sum += int(str_hours)
                str_hours = ''
        list_hours_of_subjects.append(sum)
    return list_hours_of_subjects

def output_info():
    list = []
    with open("University") as f_obj:
        for line in f_obj:
            list.append(line)
    return list

while True:
    menu()
    user_choise = value_eror()
    if user_choise == 1:
        info_list = []
        print("\n\n\t\t\t // ДОБАВЛЕНИЕ ПРЕДМЕТА В ФАЙЛ << University >> //")
        print("\t (Ели по какому-то из видов предметов отсутствуют занятия нажмите ENTER )")
        name_of_subject = input("\n\n\t # Введите название предмета }==)>                 ")
        info_list.append( name_of_subject + ": ")
        count_of_lectures = input("\t # Введите количество лекционных занятий }==)>      ")
        if check(count_of_lectures, info_list) == True:
            info_list.append(count_of_lectures + "(л) ")
        count_of_practik= input("\t # Введите количество практических занятий }==)>    ")
        if check(count_of_practik, info_list) == True:
            info_list.append( count_of_practik + "(пр) ")
        count_of_labs = input("\t # Введите количество лабораторных занятий }==)>    ")
        if check(count_of_labs, info_list) == True:
            info_list.append(count_of_labs + "(лaб) " + '\n')
        with open("University", "a") as file:
            file.writelines(info_list)
        print("\n\n\t // Запись данных в файл //")
        timer()
        print("\t Данные успешно записаны ...")
    elif user_choise == 2:
        dict_of_info = {}
        full_list = output_info()
        list_of_subjects = find_name_of_subject(full_list)
        hours_of_subjects = find_hours_of_subject(full_list)
        for i in range(0, len(full_list)):
            dict_of_info[list_of_subjects[i]] = hours_of_subjects[i]
        print("\n\n\t // Генерация словаря  //")
        timer()
        print("\n\t\t\t\t // СОЗДАННЫЙ СЛОВРЬ // \n   (ключ - название предмета, значение - кол-во всех занятий )\n")
        print("\t\t", dict_of_info)
    elif user_choise == 3:
        break