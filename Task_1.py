# 1. (3 балла)
# Напишите программу, в которой пользователь вводит числа по одному, пока не введет слово "done".
#  Для полученного списка чисел найдите среднее арифметическое. Для ввода используйте встроенную функцию input().

import numpy

number_list = []

while True:
    try:
        number = (input('Введите значение\n'))
        if number != 'done':
            number = float(number)
            number_list.append(round(number, 5))
        elif number == 'done':
            break
    except ValueError:
        print('Введено некорректное значение')
print('Список чисел:', number_list)

avg_number_list = numpy.mean(number_list)
print('Среднее арифметическое = ', round(avg_number_list, 2))