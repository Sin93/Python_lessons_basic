import os
import sys
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def createDIR(dirrectory, name):
    try:
        path = f'{dirrectory}\{name}'
        os.mkdir(path)
        print(f'Дирректория {name} создана')
        return True
    except Exception as e:
        print(f'Создать дирректорию {name} не вышло, ошибка: ', e)
        return False

def deleteDIR(name):
    try:
        os.rmdir(os.path.join(os.getcwd(), name))
        print(f'Дирректория {name} удалена')
        return True
    except Exception as e:
        print(f'Удалить дирректорию {name} не вышло, ошибка: ', e)
        return False

# i = 1
# while i <= 9:
#     nameDir = (f'dir_{i}')
#     a = createDIR(nameDir)
#     i += 1
#
# userAnswer = input('Хотите удалить дирректории dir_1 - dir_9? (y/n)')
# if userAnswer == 'y':
#     i = 1
#     while i <= 9:
#         nameDir = (f'dir_{i}')
#         a = deleteDIR(nameDir)
#         i += 1


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def dirInThisDIR(dir):
    try:
        a = []
        [a.append(itm) for itm in os.listdir(dir) if os.path.isdir(f'{dir}\{itm}')]
        return a
    except Exception as e:
        return e

def filesInThisDIR(dir):
    try:
        a = []
        [a.append(f) for f in os.listdir(dir)]
        return a
    except Exception as e:
        return e

# dirInThisDIR(os.getcwd())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copyFile(fileName):
    with open(os.path.join(os.getcwd(), fileName), 'br') as f:
        reed_data = f.read()
    with open(os.path.join(os.getcwd(), f'copy-{fileName}'), 'bw') as f:
        f.write(reed_data)

# copyFile(os.path.basename(sys.argv[0]))

