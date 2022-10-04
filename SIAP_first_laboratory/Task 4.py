import random

dict = {}
count = int(input("\n\t\t Введите количество ключей, которое будет содержать ваш словарь ==>  "))
print("Случайно сгенерированный словарь чисел, состоящий из", count, " целочисленных пар")
print("\t\t\t\t\t\t|")
print("\t\t\t\t\t\t|")
for i in range(count):
    dict[i] = random.randint(0, 100)
print("\t\t\t", dict, "\n")

soted_dict = {}
sorted_keys = sorted(dict, key=dict.get)
print("Отсортированный по возрастанию словарь чисел  ")
print("\t\t\t\t\t\t|")
print("\t\t\t\t\t\t|")
for a in sorted_keys:
    soted_dict[a] = dict[a]
print("\t\t\t", soted_dict, "\n")
items = list(soted_dict.items())
un_sorted_dict = {k: v for k, v in reversed(items)}
print("Отсортированный по убыванию словарь чисел  ")
print("\t\t\t\t\t\t|")
print("\t\t\t\t\t\t|")
print("\t\t\t", un_sorted_dict, "\n")
