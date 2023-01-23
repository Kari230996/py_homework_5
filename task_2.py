# 2.a) Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока
#      в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет.
#      Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

'''
Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

В качестве дополнительного усложнения можно:
        a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

        b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет
           необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )
'''
from random import randint
from random import choice


player_1 = "Fifi"   #input("Имя 1-го игрока: ")
player_2  = "Bubu"    #input("Имя 2-го игрока: ")

candies = 221
candies_ = 221
players = [player_1, player_2]

player_1_amount = 0
player_2_amount = 0

turn = players[0]

first_turn = choice(players)
choice_first_player = input("Бросайте жеребёвку: ")
print(f'Первый игрок: {first_turn}')




if first_turn == turn:

    dice_1 = randint(1, 28)
    candies = candies_
    candies_ -= dice_1
    player_1_amount += dice_1

    print(f'{player_1} получил {dice_1} конфет. Всего у него: {player_1_amount}')

    turn = players[1]

else:
    dice_2 = randint(1, 28)
    candies_ -= dice_2
    player_2_amount += dice_2

    print(f'{player_2} получил {dice_2} конфет. Всего у него: {player_2_amount}')

    turn = players[0]

while candies_ > 0:

    if turn == players[0]:
        pick = input(f"Ваш ход, {player_1}: ")
        dice_3 = randint(1, 28)
        candies_ -= dice_3
        player_1_amount += dice_3

        print(f'{player_1} получил {dice_3} конфет. Всего у него: {player_1_amount}')

        turn = players[1]
    else:
        pick = input(f"Ваш ход, {player_2}: ")
        dice_4 = randint(1, 28)
        candies_ -= dice_4
        player_2_amount += dice_4

        print(f'{player_2} получил {dice_4} конфет. Всего у него: {player_2_amount}')

        turn = players[0]
print()

if turn == players[0]:
    print(f"""  ***Победил игрок {player_1} c {player_1_amount} конфетами. {player_2} должен ему {candies - player_1_amount} конфет***  """)
else:
    print(f"""  ***Победил игрок {player_2} c {player_2_amount} конфетами. {player_1} должен ему {candies - player_2_amount} конфет***  """)












