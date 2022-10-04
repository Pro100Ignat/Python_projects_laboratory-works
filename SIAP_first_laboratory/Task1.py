import math

MyNum = int(input("Введите число: \n"))
i = 1
count = 0
print("Список делителей числа:")
while i < MyNum:
    if MyNum % i == 0:
        print(i)
        count+=1
    i+=1
print("Колличество делителей: ", count)