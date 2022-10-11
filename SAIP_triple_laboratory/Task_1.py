import time
from termcolor import colored, cprint

'Функция подсчёта гласных и согласных букв в строке'


def Find_leters(my_string):
    vowl_list = ['А', 'а', 'И', 'и', 'О', 'о', 'У', 'у', 'Ы', 'ы', 'Э', 'э', 'Е', 'е', 'Ё', 'ё', 'Ю', 'ю', 'Я', 'я']
    vowl_leters = 0
    consanent_leters = 0
    for i in range(0, len(my_string)):
        for a in range(0, len(vowl_list)):
            if my_string[i] == vowl_list[a]:
                vowl_leters += 1
                break
        else:
            if my_string[i] != ' ':
                consanent_leters += 1
    return vowl_leters, consanent_leters


print("\n\n\t\t\t\t\t\t\t    TASK NUMBER 1 \n")
print("\t (Вводите поэтапно строки, для завершения ввода оставьте строку пустой)")
print("\t\t  ( Или нажмите Enter, вместо ввода строки )\n\n")
count_of_str = 1
str_list = []
while True:
    print("\t\t  }==)>  Введите", count_of_str, "строку   <)=={ ")
    print("\t\t\t\t\t|")
    line = input("\t\t  >>> ")
    print("\n")
    if not line:
        break
    else:
        str_list.append(line + "\n")
        count_of_str += 1

print("\n\n\t // Реализация задания и перезаписи в файлах //")
count_of_seconds = 3
while True:
    print("\t\t\t\t", count_of_seconds, ". . .\n")
    time.sleep(1)
    count_of_seconds -= 1
    if count_of_seconds == 0: break

with open("F1", "w") as file:
    file.writelines(str_list)

new_str_list = []
with open("F1") as file:
    for line in file:
        new_str_list.append(line)
correct_list = []

for i in range(0, len(new_str_list)):
    my_string = new_str_list[i]
    correct_string = " ".join(my_string.split())
    list_of_string = correct_string.split()
    if len(list_of_string) == 1:
        correct_list.append(new_str_list[i])
    else:
        for j in range(1, len(list_of_string)):
            if list_of_string[0] == list_of_string[j]: break
            if j == len(list_of_string) - 1:
                correct_list.append(new_str_list[i])
print("\n\t\t //          В задаании указано, сохранить ввод данных пользователя -- в файл F1                 //")
print("\t\t // Из этого файла найти строки в которых первое слово не повторяеться в течении всей программы   //")
print("\t\t // После перезаписать их в файл F2 и подсчитать кол-во гласных и согласных в первой строке файла //\n\n")

print("\t // СПИСОК ВВОДИМЫХ СТРОК //\n ")
for i in range(0, len(str_list)):
    print(i + 1, ". Вводимая строка ==> ", colored(str_list[i], 'red'))

print("\n\n\t // СПИСОК СТРОК КОРРЕКТНЫХ УСЛОВИЮ //\n")
for i in range(0, len(correct_list)):
    print(i + 1, ". Строка готового списка ==> ", colored(correct_list[i], 'red'))

print("\n\t\t\t 1 СТРОКА СПИСКА С ВЕРНЫМИ ЗНАЧЕНИЯМИ }==)>  ", colored(correct_list[0], 'red'))

print("\t\t\t  ( строка имеет следующие параметры )")

my_string = correct_list[0]
print("\t\t }==)>  Колличество гласных в строке   ---", colored(Find_leters(my_string)[0], 'red'))
print("\t\t }==)>  Колличество coгласных в строке ---", colored(Find_leters(my_string)[1] - 1, 'red'))
with open("F2", "w") as file:
    file.writelines(correct_list)