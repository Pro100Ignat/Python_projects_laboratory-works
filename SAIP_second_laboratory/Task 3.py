from random import randint


def is_number(string):
    try:
        int(string)
        if int(string) != 0:
            print("\n\tЧисло введено не корректно, повторите попытку ввода")
            return True
    except ValueError:
        print("\n\tЧисло введено не корректно, повторите попытку ввода")
        return False


def transpose(matrix_list):
    res = []
    n = len(matrix_list)
    m = len(matrix_list[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matrix_list[i][j]]
        res = res + [tmp]
    return res

while True:
    lines_count = input("\n\n\t  Введите количество строк вашей матрицы ==> ")
    columns_count = input("\t  Введите количество столбцов в вашей матрице ==> ")
    if is_number(lines_count) and is_number(columns_count) == True:
        break
matrix_list = [[randint(0, 2) for j in range(int(columns_count))] for i in range(int(lines_count))]
print("\n\t\tСлучайно сгенерированная матрица чисел")
print("\t\t\t\t\t   |")
print("\t\t\t\t\t   |")
for i in matrix_list: print("\t\t\t\t", i)
print("\n\t\tТранспонированная матрица чисел")
print("\t\t\t\t\t   |")
print("\t\t\t\t\t   |")
transp_matrix_list = transpose(matrix_list)
for i in transp_matrix_list: print("\t\t\t\t", i)

count_of_zero_in_columns = 0
for j in range(0, int(columns_count)):
    count_of_zero_in_columns += 1
    for i in range(0, int(lines_count)):
        if matrix_list[i][j] == 0:
            count_of_zero_in_columns -= 1
            break
print("Количество столбцов исходной матрицы не имеющих '0' ==> ", count_of_zero_in_columns)