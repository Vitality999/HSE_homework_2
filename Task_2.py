# Напишите аналогичную программу, но для полученного списка найдите минимум и максимум.

from Task_1 import number_list
import numpy

max_number_list = numpy.max(number_list)
min_number_list = numpy.min(number_list)
print('\n Минимальное значение списка = ', min_number_list, '\n',\
      'Максимальное значение списка = ', max_number_list)
