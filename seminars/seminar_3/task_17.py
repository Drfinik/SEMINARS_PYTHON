# Задача №17. 
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# list = [1, 1, 2, 0, -1, 3, 4, 4]
# unique_numbers = set(list)
# print("Количество различных чисел в списке:", len(unique_numbers))


# Задача №19. 
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


# my_list = [i for i in range(10)]

# print(my_list)
# shift = int(input("На сколько сдвигаем список: "))

# for _ in range(shift):
#     my_list.insert(0, my_list.pop())
# print(my_list)


# Задача №21.
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# unique_values = set()
# for element in list:
#     for value in element.values():
#         unique_values.add(value)
# print(unique_values)


# Задача №23. 
# Дан список, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# list = [0, -1, 5, 2, 3]
# result = sum(x > y for x, y in zip(list[1:], list))
# print(result)

