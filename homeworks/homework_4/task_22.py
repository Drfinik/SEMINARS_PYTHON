# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


# n = int(input("Количество элементов первого множества: "))
# m = int(input("Количество элементов второго множества: "))

# set1 = set()
# set2 = set()

# print("Введите элементы первого множества: ")
# for i in range(n):
#  set1.add(int(input()))

# print("Введите элементы второго множества: ")
# for i in range(m):
#  set2.add(int(input()))

# common_set = set1 & set2

# print("Общие элементы:", sorted(common_set))