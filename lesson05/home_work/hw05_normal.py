import os
import hw05_easy as myFunc
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

dirrectory = os.getcwd()
while True:
    print('Текущая дирректория: ', dirrectory)
    userAnswer = input('''Привет пользователь!
    Выбери действие:
    1. Перейти в папку
    2. Просмотреть содержимое текущей папки
    3. Удалить папку
    4. Создать папку
    5. Вернуться в корневую папку
    q - завершить программу''')
    if userAnswer == '1':
        dirList = myFunc.dirInThisDIR(dirrectory)
        userAnswer = input(f'В дирректории доступны папки для перехода: {dirList}')
        if userAnswer in dirList:
            dirrectory = dirrectory + f'\{userAnswer}'
            print(f'Переход в папку {userAnswer} успешно выполнен')
        else:
            print('Ошибка! Не верное имя папки, повторите ввод')
    elif userAnswer == '2':
        print('В текущей дирректории содержатся файлы и папки:', myFunc.filesInThisDIR(dirrectory))
    elif userAnswer == '3':
        dirList = myFunc.dirInThisDIR(dirrectory)
        userAnswer = input(f'В дирректории доступны папки для удаления: {dirList}')
        myFunc.deleteDIR(dirrectory, userAnswer)
    elif userAnswer == '4':
        userAnswer = input('Введите название папки: ')
        myFunc.createDIR(dirrectory, userAnswer)
    elif userAnswer == '5':
        dirrectory = os.getcwd()
    elif userAnswer == 'q':
        print('Программа завершена.')
        break
    else:
        print('Неизвестная команда, повторите ввод')