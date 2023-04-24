# Задача №13.
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# import random
# today_temp =[]
# day = int(input("Ввести колличество дней: "))
# for i in range(day):
#         today_temp.append(random.randint(-3,3))
# print(today_temp)
# for i in x:
#         ifx[i]>0:
#             temp.append(x)
#     Output.append(temp)


# import random
# i = 1
# x = int(random.randint(1, 1000))
# y = int(random.randint(1, 1000))
# s = int(random.randint(1, 1000))
# # p = int(random.randint(1, 1000))
# while  s!=x+y :
#     if s!=x+y :
#         i += 1
#         x = int(random.randint(1, 1000))
#         y = int(random.randint(1, 1000))
#         s = int(random.randint(1, 1000))
#         # p = int(random.randint(1, 1000))
#         continue
# else:
#     p = x*y
#     print("Колличество циклов: ", i)
#     print(x, y)    
#     print(s, p)



# i = 1
x = int(input(2))
y = int(input(2))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)