
# import random

# def filter_list(array1, array2):
#     res_array = []
#     for i in array1:
#         if i not in array2:
#             res_array.append(i)
#     return res_array

# def create_random_list(number):
#     return [random.randint(-10,10) for _ in range(number+1)]


# number_1 = int(input("Введите количество первого массива: "))
# number_2 = int(input("Введите количество второго массива: "))

# int_array_1 = create_random_list(number_1)
# print(int_array_1)
# int_array_2 = create_random_list(number_2)
# print(int_array_2)

# print(filter_list(int_array_1, int_array_2))

# "CTR + /" позваляет сразу закомментировать весь код

# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# def find_num(list_1, max_number, min_number):
#     indices = []
#     for i in range(len(list_1)):
#         if min_number < list_1[i] <= max_number:
#             indices.append(i)
#     return indices
# result = find_num (list_1, min_number, max_number)
# print(result)



# Заполните массив элементами арифметической прогрессии.
# Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
a_1 = 2
d = 3
n = 4     

progression = []

for i in range(n):
    element = a_1 + i * d
    progression.append(element)

for i in progression:
    print(i)
