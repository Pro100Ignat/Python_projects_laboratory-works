from random import randint

numbers = []
count = int(input("\n\t\t Сколько символов вы хотите увидеть в вашем списке ==>  "))
print("\n")
print("Случайно сгенерированный массив чисел, состоящий из", count, "эллементов")
print("\t\t\t\t\t\t|")
print("\t\t\t\t\t\t|")
for i in range(count):
    numbers.append(randint(-100, 100))
print("\t\t\t",numbers,"\n")
print("Отсортированный по убыванию массив чисел  ")
print("\t\t\t\t\t\t|")
print("\t\t\t\t\t\t|")
numbers.sort(reverse=True)
print("\t\t\t" ,numbers, "\n")

i = 0
while i<len(numbers):
    if numbers[i] > 0 and numbers[i]%2==0:
        print(numbers[i], "-- В этом списке, это наибольший положительный эллемент")
        break
    if numbers[i] < 0:
        print("\t\tПоложительных, чётных эллементов в данном списке не найдено, поэтому по ТЗ выводим 1 эллемент в списке: ",numbers[0])
        break
    i+=1