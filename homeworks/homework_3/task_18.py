# Задача 18: 
## Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.


# import random
# n = int(input("Ввести количество элементов в массиве: "))  # вводим количество элементов в массиве.
# random_list = [random.randint(1, 10) for i in range(n)] # создаем список с количеством элементов (n), элементами заполняем рандомно.
# x = int(input("Введите число для поиска: "))  # вводим число X.
# min_diff = x - random_list[0]
# closest = random_list[0]

# for i in range(1, n):
#     diff = x - random_list[i]
# if diff < min_diff:
#     min_diff = diff
# closest = random_list[i]
# print(random_list)
# print(closest)