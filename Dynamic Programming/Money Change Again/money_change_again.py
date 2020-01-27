# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    MinNumCoins = {0 : 0}

    for m in range(1,money+1):
        MinNumCoins[m] = float("inf")
        for coin in [1,3,4]:
            if m >= coin:
                NumCoins = MinNumCoins[m - coin] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins

    return MinNumCoins[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
