# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    pperlb = []

    backpack = [0] * len(weights)
    value = 0

    for i in range(len(prices)):
        pperlb.append(prices[i]/weights[i])

    #print(pperlb)

    while capacity > 0 and len(weights) > 0:

        if len(pperlb) > 1:
            idx = pperlb.index(max(pperlb))
        else:
            idx = 0
        #print(value, weights[idx], pperlb[idx])

        if weights[idx] <= capacity:
            value += weights[idx] * pperlb[idx]
            addwt = weights[idx]
        else:
            value += capacity * pperlb[idx]
            addwt = capacity

        capacity = capacity - addwt
        pperlb.pop(idx)
        weights.pop(idx)

    return value





if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    # n, input_capacity = map(int, input().split())
    # input_prices = list(map(int, input().split()))
    # input_weights = list(map(int, input().split()))
    #print(n, input_capacity, input_weights, input_prices)
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
