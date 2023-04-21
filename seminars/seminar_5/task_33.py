# Задача 33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# import random
# marks = [random.randint(1, 5) for i in range(10)]
# print(marks)
# max_marks = max(marks)
# min_marks = min(marks)
# for i in range (len(marks)):
#     if marks[i] ==max_marks: marks[i] = min_marks
# print(marks)