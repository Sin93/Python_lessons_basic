import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# это первый вариант решения, который у меня вышел, он сначала формирует ВСЮ последовательность, а потом отсекает лишнее
# опасаясь за оперативку на больших числах сделал второй вариант
# def fibonacci(n, m):
#     fibonacciList = [1, 1]
#     while len(fibonacciList) < m:
#         fibonacciList.append(fibonacciList[-1] + fibonacciList[-2])
#     return fibonacciList[n-1:]

def fibonacci(n, m):
    i = 1
    fibonacciList = [1, 1]
    while len(fibonacciList) < m and i != n:
        fibonacciList.append(fibonacciList[-1] + fibonacciList[-2])
        fibonacciList.pop(0)
        i += 1
    else:
        while len(fibonacciList) < m + 1 - n:
            fibonacciList.append(fibonacciList[-1] + fibonacciList[-2])
    return fibonacciList

print(fibonacci(5, 8))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    lenghtList = len(origin_list)
    for i in range(lenghtList - 1):
        for n in range(lenghtList - i - 1):
            if origin_list[n] > origin_list[n + 1]:
                origin_list[n], origin_list[n + 1] = origin_list[n + 1], origin_list[n]
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def newFilter(funct, arg):
    list = []
    for itm in arg:
        if funct(itm) == True:
            list.append(itm)
    return list

list2 = newFilter(lambda x: x < 20, [1, 5, 8, 15, 16, 7, 46, 5])
print(list2)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def check(n, m):
    deltaX = n[0] - m[0]
    deltaY = n[1] - m[1]
    zN = math.sqrt(deltaX ** 2 + deltaY ** 2)
    return zN

a1x = int(input('a1x: '))
a1y = int(input('a1y: '))
a2x = int(input('a2x: '))
a2y = int(input('a2y: '))
a3x = int(input('a3x: '))
a3y = int(input('a3y: '))
a4x = int(input('a4x: '))
a4y = int(input('a4y: '))

a = [
    [a1x, a1y],
    [a2x, a2y],
    [a3x, a3y],
    [a4x, a4y]
]
z = [check(a[0], a[1]),
    check(a[0], a[2]),
    check(a[0], a[3]),
    check(a[1], a[2]),
    check(a[1], a[3]),
    check(a[2], a[3]),
]

i = 0
for w in range(len(z) - 1):
    for q in range(len(z) - w - 1):
        if z[w] == z[q + w + 1]:
            i += 1
if i == 2:
    print('введенные точки являются вершинами паралелограмма')
elif i == 3:
    print('введенные точки являются частным случаем паралелограмма - прямоугольником')
elif i == 6:
    print('введенные точки являются частным случаем паралелограмма - ромбом')
elif i == 7:
    print('введенные точки являются частным случаем паралелограмма - квадратом')
else:
    print('введенные точки НЕявляются вершинами паралелограмма')

# примеры фигур:
# ромб
# a1x = 1
# a1y = 4
# a2x = 3
# a2y = 7
# a3x = 5
# a3y = 4
# a4x = 3
# a4y = 1
#
# квадрат
# a1x = 1
# a1y = 1
# a2x = 1
# a2y = 4
# a3x = 4
# a3y = 4
# a4x = 4
# a4y = 1
#
# прямоугольник
# a1x = 1
# a1y = 1
# a2x = 1
# a2y = 4
# a3x = 5
# a3y = 4
# a4x = 5
# a4y = 1
#
# паралелограмм
# a1x = 3
# a1y = 2
# a2x = 1
# a2y = 5
# a3x = 5
# a3y = 6
# a4x = 7
# a4y = 3