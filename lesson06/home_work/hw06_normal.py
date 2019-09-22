# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import random

class Human:

    def __init__(self, name, surname=None, father=None, mother=None):
        """
        Базовый класс описывающий человека, обязательно передать Имя
        :param name: str
        :param surname: str
        :param father: Human
        :param mother: Human
        """
        self.name = name
        if father:
            self.surname = father.surname
            self.patr_name = father.name
        else:
            self.surname = surname or 'Неизвестна'
            self.patr_name = 'Иван'
        self.father = father
        self.mother = mother

    def __str__(self):
        return f'{self.surname} {self.name[0]}.{self.patr_name[0]}'

class Subject:

    def __init__(self, name):
        self.name = name


class Teacher(Human):
    sh_class = []

    def __init__(self, **kwargs):
        self.subject = kwargs['subject']
        kwargs.pop('subject')
        Human.__init__(self, **kwargs)


class Student(Human):
    sh_class = None

    def __init__(self, **kwargs):
        Human.__init__(self, **kwargs)

    def __str__(self):
        return f'{self.surname} {self.name[0].upper()}. {self.father.name[0].upper()}.'

    @property
    def get_subjects(self):
        return [techer.subject for techer in self.sh_class.teachers]

    def get_parrents(self):
        return list(map(str, (self.father, self.mother)))

class SchoolClass:


class School:

if __name__ == '__main__':
    names = ['Иван', 'Филипп', 'Анатолий', 'Анна', 'Мария', 'Тамара']
    surnames = ['Сидоров', 'Антуанет', 'Питонов', 'Иванов', 'Джобс']
    subjects_lst = ['математика', 'геометрия', 'Ин-яз', 'Физ-ра', 'Информатика']
    humans = [Human(name=random.choice(names), surname=random.choice(surnames))]

    students = []

    for _ in range(5):
        fat = random.choice(humans)
        mather = random.choice(humans)
        student = Student(name=random.choice(names), father=fat, mother=mather)
        students.append(student)

    teachers = []

    for _ in range(50):
        fat = random.choice(humans)
        mather = random.choice(humans)
        teacher = Teacher(name=random.choice(names), father=fat, mother=mather, subject=random.choice(subjects_lst))
        teachers.append(teacher)


