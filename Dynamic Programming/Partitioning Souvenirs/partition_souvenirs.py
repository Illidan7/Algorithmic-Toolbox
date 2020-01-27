# python3

from itertools import product
from sys import stdin


def partition3chk(arr, N):

    if (N < 3):
        return False

    sum = 0
    for i in range(N):
        sum += arr[i]
    if (sum % 3 != 0):
        return False

    expSum = sum // 3
    partSum = [0] * 3
    taken = [False] * N

    partSum[0] = arr[N - 1]
    taken[N - 1] = True

    # call recursive method to check
    # K-substitution condition
    return partition3(arr, partSum, taken,
                                   expSum, N, 0, N - 1)


def partition3(arr, partSum, taken, expSum, N, curIdx, limitIdx):
    # assert 1 <= len(values) <= 20
    # assert all(1 <= v <= 30 for v in values)

    if partSum[curIdx] == expSum:

        if (curIdx == 1):
            return True

        # recursive call for next subset
        return partition3(arr, partSum, taken, expSum, N, curIdx + 1, limitIdx)

    for i in range(limitIdx, -1, -1):

        # if already taken, continue
        if (taken[i]):
            continue
        tmp = partSum[curIdx] + arr[i]

        if (tmp <= expSum):

            taken[i] = True
            partSum[curIdx] += arr[i]
            nxt = partition3(arr, partSum, taken, expSum, N, curIdx, i - 1)

            taken[i] = False
            partSum[curIdx] -= arr[i]
            if (nxt):
                return True
    return False


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)

    if (partition3chk(input_values, input_n)):
        print(1)
    else:
        print(0)
