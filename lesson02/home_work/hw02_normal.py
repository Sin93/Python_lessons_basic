
__author__ = 'Зиновьев Максим Игоревич'

import math
import numpy as np

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

list = [2, -5, 8, 9, -25, 25, 4, 81, -64, 15]
newList = []
for number in list:
    if number < 0:
        pass
    elif (math.sqrt(number) * 10) % 10 != 0:
        pass
    else:
        newList.append(math.sqrt(number))
print(newList)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

dd = int(input('Введите день '))
mm = int(input('Введите месяц '))
yyyy = int(input('Введите год '))
days = {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвертое', 5: 'пятое', 6: 'шестое', 7: 'седьмое', 8: 'восьмое',
        9: 'девятое', 10: 'десятое', 11: 'одиннадцатое', 12: 'двеннадцатое', 13: 'триннадцатое', 14: 'четырнадцатое',
        15: 'пятнадцатое', 16: 'шестнадцатое', 17: 'семнадцатое', 18: 'восемнадцатое', 19: 'девятнадцатое',
        20: 'двадцатое', 21: 'двадцать первое', 22: 'двадцать второе', 23: 'двадцать третье', 24: 'двадцать четвертное',
        25: 'двадцать пятое', 26: 'двадцать шестое', 27: 'двадцать седьмое', 28: 'двадцать восьмое',
        29: 'двадцать девятое', 30: 'тридцатое', 31: 'тридцать первое'}
month = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
        9: 'сертября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
print('{} {}'.format(days[dd], month[mm]), yyyy, 'года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

n = int(input("Введите количество элементов списка: "))
list2 = np.random.randint(-100, 100, n)
print(list2)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

list3 = np.random.randint(0, 10, 10)
list3 = list3.tolist()
print(list3)
newList2 = []
for number in list3:
    if newList2.count(number) > 1:
        pass
    elif newList2.count(number) < 1:
        newList2.append(number)
newList2 = sorted(newList2)
print(newList2)

newList3 = []
for number in list3:
    if list3.count(number) == 1:
        newList3.append(number)
newList3 = sorted(newList3)
print(newList3)