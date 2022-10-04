import math
string = input("\n\t\t\t Введите строку: ")
result = string.split()
i=0
count =0
while i<len(string.split()):
    if len(result[i])%2==0:
        count+=1
    i+=1
print("\t\t В строке ", count, " слова c чётным количеством букв.")
print("\t\t", max(result, key = len), "- Самое длинное слово в строке. ")