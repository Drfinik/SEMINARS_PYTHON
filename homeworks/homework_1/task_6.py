# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# Вариант № 1.
# s = int(input('Введите номер билета: '))
# f = s % 10
# #print(f)
# e1 = (s // 10)
# e = (e1 % 10)
# #print(e)
# d1 = e1 // 10
# d = (d1 % 10)
# #print(d)
# c1 = d1 // 10
# c = (c1 % 10)
# #print(c)
# b1 = c1 // 10
# b = (b1 % 10)
# #print(b)
# a = b1 // 10
# #print(a)
# sum_last = f + e + d
# #print("Сумма цифр числа:", sum_last)
# sum_first = a + b + c
# #print("Сумма цифр числа:", sum_first)
# if sum_first == sum_last:
#     print("Этот билет счастливый!")
# else:
#     print("К сожалению, этот билет не счастливый")


# Вариант № 2.
# s = input("Введите номер билета: ")
# sum_first = int(s[0]) + int(s[1]) + int(s[2])
# sum_last = int(s[3]) + int(s[4]) + int(s[5])
# if sum_first == sum_last:
#     print("Этот билет счастливый!")
# else:
#     print("К сожалению, этот билет не счастливый")