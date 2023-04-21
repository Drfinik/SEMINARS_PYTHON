# Задача 18: 
## Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.


import random
n = int(input("Ввести количество элементов в массиве: "))  
random_list = [random.randint(1, 10) for _ in range(n)] 
x = int(input("Введите число для поиска: "))  
count_num = random_list.count(x)
closest = random_list[0]
if count_num == 0:
    for num in random_list:
        if abs(x - num) < abs(x - closest):
            closest = num
print(f"В списке {random_list} ближайщее к числу {x} число {closest}")