def value_eror():
    while True:
        try:
            number = int(input("\n\tВвод данных ==>"))
            break
        except:
            print("\t  Проверьте вводимые данные и повторите попытку . . .")
    return number


def first_task():
    while True:
        try:
            number = int(input("\n\t Работа блока try, здесь происходит ввод данных ==>"))
            break
        except:
            print(
                "\n\t Отработал блок Except, так как вы ввели не корректное значение, вы видете это сообщение которое оповестит вас об ошибке . . .")
        finally:
            print(
                "\n\t Уууууупс, блок finally, выводящий сообщение в любом случае, назависимо от параметров ввода . . .")


def second_task():
    while True:
        try:
            constant_number = 100
            print("\n\t Введите ноль, для проверки работы исключения . . .")
            zero = value_eror()
            с = constant_number / zero
            if zero != 0: print("\t Конечно не ноль, но так уж и быть, я поделю ==> ", с)
        except ZeroDivisionError:
            print("\n\t Деление на ноль запрещено, иди учи математику, а потом Python . . .")
            break
    return


def menu():
    print("\n\n\t\t << Меню выбора проверок >>"
          "\n\t1 -- Проверка на целочисленный ввод            "
          "\n\t2 -- Проверка деления на ноль                  "
          "\n\t5 -- Выход из программы ==> Exit               "
          "\n\t Ваш выбор . . .                               ")


while True:
    while True:
        menu()
        choise = value_eror()
        if choise == 1:
            print("\n\n\t Введите число, но для проверки работы try/except можете ввести любое значение . . .")
            first_task()
        elif choise == 2:
            second_task()
        elif choise == 5:
            break