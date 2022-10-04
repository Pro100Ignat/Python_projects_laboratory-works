import random

def value_eror():
    while True:
        try:
           number = int(input("\n\tВедите количество слов в вашей строке ==> "))
           break
        except:
            print("\t  Проверьте вводимые данные и повторите попытку . . .")
    return number

def Find_leters(my_string):
    vowl_leters = 0
    consanent_leters = 0
    for i in range(0,len(my_string)):
        for a in range(0, len(vowl_list)):
            if my_string[i] == vowl_list[a]:
                vowl_leters += 1
                break
        else:
            if my_string[i] != ' ':
                consanent_leters += 1
    return vowl_leters, consanent_leters


print("\n\n\t\t << Меню генерации строки >>")
while True:
    my_string = " "
    list = [" Окно"," дверь"," плинтус"," карман"," Луна"," камень"," бассейн"," куча"," хип"," стек"," массив"]
    count_of_words = value_eror()
    for i in range(count_of_words): my_string = my_string + random.choice(list)
    print("\n\t\t  Случайно сгенерированная строка из массива слов ==>",my_string)
    vowl_list = ['А', 'а', 'И', 'и', 'О', 'о', 'У', 'у', 'Ы', 'ы', 'Э', 'э', 'Е', 'е', 'Ё', 'ё', 'Ю', 'ю', 'Я', 'я']
    print("   Колличество гласных в строке :",Find_leters(my_string)[0])
    print("   Колличество coгласных в строке :",Find_leters(my_string)[1])