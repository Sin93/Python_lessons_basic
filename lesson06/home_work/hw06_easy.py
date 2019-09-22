import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, ax, ay, bx, by, cx, cy, ab=None, bc=None, ac=None):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.ab = round(math.sqrt((self.bx - self.ax) ** 2 + (self.by - self.ay) ** 2), 2)
        self.bc = round(math.sqrt((self.cx - self.bx) ** 2 + (self.cy - self.by) ** 2), 2)
        self.ac = round(math.sqrt((self.cx - self.ax) ** 2 + (self.cy - self.ay) ** 2), 2)

    def perim(self):
        self.perimetr = round(float(self.ab + self.bc + self.ac), 2)
        self.pp = self.perimetr / 2
        return self.perimetr

    def area(self):
        self.s = round(math.sqrt(self.pp * (self.pp - self.ab) * (self.pp - self.bc) * (self.pp - self.ac)), 2)
        return self.s

    def height(self):
        if self.ay > self.by and self.ay > self.cy:
            self.h = round(2 * self.s / self.bc, 2)
        elif self.by > self.ay and self.by > self.cy:
            self.h = round(2 * self.s / self.ac, 2)
        else:
            self.h = round(2 * self.s / self.ab, 2)

        return self.h


# if __name__ == '__main__':
#     first = Triangle(1, 1, 6, 2, 4, 5)
#     print('Сторона ab:', first.ab, '\nСтрона bc', first.bc, '\nСторона aс:', first.ac)
#     print('Периметр введенного треугольника: ', first.perim())
#     print('Площадь треугольника', first.area())
#     print('Высота треугольника, опущенная из самой высокой точки (по оси y):', first.height())


# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# Внимание! Методы не будут правильно отрабатывать если вводить точки не в том порядке, который я задумал.
# Можно было бы заморочиться и накрутить проверки, но я боюсь, что ещё пару часов на это уйдёт, а ещё много всего надо накодить.
# Порядок который я задумал (x;y):
# 1. Нижняя левая
# 2. Нижняя правая
# 3. Верхняя правая
# 4. Верхняя левая

class Trapeze:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy

    def lenghtSide(self):
        self.ab = round(math.sqrt((self.bx - self.ax) ** 2 + (self.by - self.ay) ** 2), 2)
        self.bc = round(math.sqrt((self.cx - self.bx) ** 2 + (self.cy - self.by) ** 2), 2)
        self.cd = round(math.sqrt((self.cx - self.dx) ** 2 + (self.cy - self.dy) ** 2), 2)
        self.ad = round(math.sqrt((self.dx - self.ax) ** 2 + (self.dy - self.ay) ** 2), 2)

    def check(self):
        if (self.bc == self.ad) and (self.ay - self.by == 0) and (self.cy - self.dy == 0) and (abs(self.ax - self.dx) == abs(self.bx - self.cx)) and (self.ab != self.cd):
            return True
        else:
            return False

    def perim(self):
        self.perimetr = round(float(self.ab + self.bc + self.cd + self.ad), 2)
        return self.perimetr

    def area(self):
        if self.ab > self.cd:
            self.s = (self.dy - self.ay) * (self.dx - self.ax) + self.cd * (self.dy - self.ay)
        else:
            self.s = (self.dy - self.ay) * (self.ax - self.dx) + self.ab * (self.dy - self.ay)
        return self.s


# if __name__ == '__main__':
#     second = Trapeze(0, 0, 5, 0, 4, 4, 1, 4)
#     second.lenghtSide()
#     if second.check() == False:
#         print("\nВведенные точки не соответствуют равнобокой трапеции")
#     else:
#         print('\nВведены точки, которые соответствуют равнобокой трапеции')
#         print('Сторона ab:', second.ab, '\nСторона bc:', second.bc, '\nСторона cd:', second.cd, '\nСторона ad:', second.ad)
#         print('Периметр трапеции:', second.perim())
#         print('Площадь трапеции:', second.area())