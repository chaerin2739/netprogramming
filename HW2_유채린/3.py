from random import randint


def coin_game() :
    total_money = 50

    while 0 < total_money < 100:
        coin = randint(1,2)
        g = randint(1,2)
        if coin == g:
            total_money += 9
        else :
            total_money -= 10
        print(total_money)


coin_game()