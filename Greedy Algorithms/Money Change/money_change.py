# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    n_coins = 0

    n_coins = money//10
    money = money - (money//10) * 10

    n_coins = n_coins + money//5
    money = money - (money//5) * 5

    n_coins = n_coins + money//1

    return n_coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
