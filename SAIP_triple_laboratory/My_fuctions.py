# -*- coding: utf-8 -*-
import time
def value_eror():
    while True:
        try:
            number = int(input("\n\t Поле ввода значений ==> "))
            break
        except:
            print("\t  Проверьте вводимые данные и повторите попытку . . .")
    return number

def timer():
    count_of_seconds = 3
    while True:
        print("\t\t\t\t", count_of_seconds, ". . .\n")
        time.sleep(1)
        count_of_seconds -= 1
        if count_of_seconds == 0: break

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