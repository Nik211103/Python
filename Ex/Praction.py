#Написать программу, которая просит пользователя ввести число и выводит на экран его квадрат.
# x = int(input("Введите число: "))
# result = x**2
# print (result)

# 1. Print "Привет, мир!" - Это классический первый программа, который вводит вас в основной синтаксис Python.
# 2. Запросите у пользователя имя и выведите приветствие - Это задача помогает вам научиться использовать переменные и основные операции ввода-вывода в Python.
# 3. Напишите программу, которая рассчитает площадь прямоугольника - Эта задача вводит вас в основные математические операции и типы данных в Python.
# 4. Создайте программу, которая преобразует градусы Цельсия в градусы Фаренгейта - Эта задача помогает вам научиться использовать функции и преобразовать типы данных в Python.
# 5. Напишите программу, которая рассчитает среднее значение списка чисел - Эта задача вводит вас в списки и основные статистические операции в Python.
# 6. Создайте программу, которая выведет список чисел в заданном порядке - Эта задача помогает вам научиться использовать индексирование и вырезку в Python.
# 7. Напишите программу, которая рассчитает факторIAL числа - Эта задача вводит вас в рекурсивные функции в Python.
# 8. Создайте программу, которая моделирует простой банковской системе - Эта задача помогает вам научиться использовать условные операторы и циклы в Python.
# 9. Напишите программу, которая генерирует случайный число от 1 до 10 - Эта задача вводит вас в случайные числа в Python.
# 10. Создайте программу, которая рассчитает сумму двух чисел - Эта задача помогает вам научиться использовать функции и основные арифметические операции в Python.

#1
# print('Helo, World!')

#2
# name = input("Введите свое имя: ")
# print(f"Привет, {name}!")

#3
# lenght = int(input("Введите длину прямоугольника: " ))
# width = int(input("Введите ширину прямоугольника: "))
# result = lenght * width
# print(f"Площадь прямоугольгика равна: {result}")


#4
# temp_c = int(input("Введите температуру в Цельсиях: "))

# def Temp_F(temp_c):
#     F = int
#     F = (temp_c * 9/5) + 32
#     return F
# result = Temp_F(temp_c)
# print(result)

#5
# list_1 = input("Введите список через пробел: ").split()
# list_result = []

# for i in list_1:
#     list_result.append(int(i))

# sum = 0
# for i in list_result:
#     sum += i
# result = float(sum / len(list_result))
# print(f"Среднее арифметическое равно: {result}")


#9
# import random
# number_lenght = int(input("Введите размер массива: "))

# def create_random_list(number_lenght):
#     return [random.randint(1,10) for _ in range(number_lenght+1)]

# numbers = create_random_list(number_lenght)
# print(numbers)

#11
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# result_list = []

# for i in a:
#     if i >= 5:
#         result_list.append(int(i)) 

# print(result_list)

# Даны списки:
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result_list = []
# for i in a:
#     if i in b:
#         result_list.append(i)
# print(result_list)

# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         header = ' '.join([str(i) for i in range(1, num_columns + 1)])
#         print(header)
#         for i in range(2, num_rows + 1):
#             row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
#             print(' '.join(row))
# print_operation_table(lambda x, y: x + y, 4, 4)

# Задача 2: Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
# a = 5; b = 7 -> max = 7
# a = 2 b = 10 -> max = 10
# a = -9 b = -3 -> max = -3
# first_num = int (input("Введите первое число: "))
# second_num = int (input("Введите второе число: "))
# if first_num == second_num:
#     print("Числа равны.")
# else:    
#     if first_num > second_num:
#         print(f"Число {first_num} больше {second_num}.")
#     else:
#      print(f"Число {first_num} меньше {second_num}.")

# Задача 4: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
# 2, 3, 7 -> 7
# 44 5 78 -> 78
# 22 3 9 -> 22

# first_num = int (input("Введите первое число: "))
# second_num = int (input("Введите второе число: "))
# therd_num = int (input("Введите третье число: "))
# if first_num == second_num == therd_num:
#     print("Числа равны.")
# else:    
#     if first_num > second_num and first_num > therd_num:
#         print(f"Число {first_num} самое большое.")
#     if second_num > first_num and second_num > therd_num:
#         print(f"Число {second_num} самое большое.")
#     if therd_num > first_num and therd_num > second_num:
#         print(f"Число {therd_num} самое большое.") 
# Задача 6: Напишите программу, которая на вход принимает число и выдаёт, является ли число чётным (делится ли оно на два без остатка).
# 4 -> да
# -3 -> нет
# 7 -> нет

# num = int(input("Введите число: "))
# if num % 2 == 0:
#     print(f"Число {num} четное.")
# else:
#     print(f"Число {num} не четное.")

# Задача 8: Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

# num = int(input("Введите число: "))
# i = 2
# res = []
# while i <= num:
#     if i % 2 == 0:
#         res.append(int(i))
#         i += 1
#     else:
#         i += 1

# while i <= num:
#     res.append(int(i))
#     i += 2
# print(res)

# Задача 10: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.
# 456 -> 5
# 782 -> 8
# 918 -> 1

# num = int(input("Введите трехзначное число: "))
# res = int(num / 10) % 10
# print(res)


# Задача 13: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
# 645 -> 5
# 78 -> третьей цифры нет
# 32679 -> 6
num = int(input("Введите число: "))
temp = int(num / 100)
if temp == 0:
    print(f"Число {num} не имеет третьей цифры.")
else:
    if num > 999:
        res = temp % 10 #где-то здесь не работает 

    elif num > 99999:
        num / num / 1000
        res = int(num % 10)
    
    else:
        num = num / 100
        res = int(num % 10)
    print(res)
