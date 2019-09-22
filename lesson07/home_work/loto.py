#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

class Plaer:

    def __init__(self, name):
        self.name = name
        self.card = [
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--']
        ]
        self.gen_card()

    def gen_card(self):
        numbersForCard = []
        for itm in range(1, 91):
            numbersForCard.append(itm)
        random.shuffle(numbersForCard)

        i = 0
        while i < 3:
            position = [itm for itm in range(0, 9)]
            random.shuffle(position)
            pos = [position.pop(0) for _ in range(5)]
            pos.sort()
            numbersLine = [numbersForCard.pop(0) for _ in range(5)]
            numbersLine.sort()
            for j in pos:
                self.card[i][j] = str(numbersLine.pop(0))
            i += 1
        newCard = ''
        for i in range(3):
            for j in range(9):
                newCard = newCard + str(self.card[i][j]) + '  '
            newCard = newCard + '\n'
        self.plaerCard = f'Карточка игрока: {self.name}\n{newCard}'
        return self.plaerCard

class Game:
    def __init__(self, number):
        self.number = number
        self.gen_bag()
        self.PlayGame()

    def gen_bag(self):
        self.bag = []
        for itm in range(1, 91):
            self.bag.append(str(itm))
        random.shuffle(self.bag)
        return self.bag

    def PlayGame(self):
        print(plaer.plaerCard)
        print(plaer2.plaerCard)

        for num in self.bag:
            # спрашиваем игрока и проверяем его карточку
            plaerAnswer = input(f'Выпало число: {num}, зачеркнуть?(д/н)\n')
            numberInCard = None

            # Проверяем ответ Да
            if plaerAnswer == 'д':
                for i in range(0, 3):
                    numberInCard = num in plaer.card[i]
                    if numberInCard == True:
                        plaer.card[i][plaer.card[i].index(num)] = f'\{num}/'
                        print(self.GenStrCard(plaer))
                        print(self.GenStrCard(plaer2))
                        break
            if numberInCard == False:
                print('В вашей карте нет выпавшего числа. Вы проиграли!')
                break

            # Проверяем ответ Нет
            numberInCard = None
            if plaerAnswer == 'н':
                for i in range(0, 3):
                    numberInCard = num in plaer.card[i]
                    if numberInCard == True:
                        print('В вашей карте есть выпавшее число. Вы проиграли!')
                        break
            if numberInCard == True:
                break
            else:
                print(self.GenStrCard(plaer))
                print(self.GenStrCard(plaer2))

            # Компьютер сам проверяет свою карточку и отмечает выпавшее число
            for i in range(0, 3):
                numberInCard2 = num in plaer2.card[i]
                if numberInCard2 == True:
                    plaer2.card[i][plaer2.card[i].index(num)] = f'\{num}/'
                    print(self.GenStrCard(plaer))
                    print(self.GenStrCard(plaer2))
                    break
                else:
                    continue

            # Надо завершить игру если все числа в одной из карточек отмечены
            check = 0
            check2 = 0
            for itm in range(1, 91):
                for i in range(0, 3):
                    if str(itm) in plaer.card[i]:
                        check = 1
                    if str(itm) in plaer2.card[i]:
                        check2 = 1
            if check == 0:
                print(f'Игрок {plaer.name} победил!')
                break
            elif check2 == 0:
                print(f'Игрок {plaer2.name} победил!')
                break


    def GenStrCard(self, plaerName):
        self.newCard = ''
        for i in range(3):
            for j in range(9):
                self.newCard = self.newCard + str(plaerName.card[i][j]) + '  '
            self.newCard = self.newCard + '\n'
        return f'Карточка игрока: {plaerName.name}\n{self.newCard}'


if __name__ == '__main__':
    n = 1
    name = input('Введите имя игрока ')
    plaer = Plaer(name)
    plaer2 = Plaer('Компьютер')
    Game(n)
    while True:
        playMore = input('Хотите сыграть ещё раз?(д/н)')
        if playMore == 'д':
            plaer = Plaer(name)
            plaer2 = Plaer('Компьютер')
            Game(n+1)
        else:
            print('\nДо свидания!')
            break