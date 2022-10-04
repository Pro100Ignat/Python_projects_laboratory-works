my_tuple = (1, 4, -4, 6, -7, -5, 4, -6, -3, 5, 2, -35, 34, 23, 5, 3, -54, 34, -6, 5, 54)
count = 0
while True:
    count = int(input("\n\t\t Сколько цифр вы хотите увидеть в вашем кортеже ==>  "))
    if len(my_tuple) > count:
        break
    else:
        print("\n\t\tВведное значение выходит за предел заданного кортежа, нажмите любую клавишу и повторите попытку . . .")
        input()
print("\n")
print("Кортеж чисел, состоящий из", count, "эллементов")
print("\t\t\t\t\t\t|")
print("\t\t\t\t\t\t|")
sum = 0
for i in range(0, count):
    print("\t\t[", i, "]", "Эллемет кортежа ==> ", my_tuple[i])
    if my_tuple[i] > 0:
        sum += my_tuple[i]
print("\n\t\t\t Сумма положительных эллементов заданного кортежа ==>", sum)