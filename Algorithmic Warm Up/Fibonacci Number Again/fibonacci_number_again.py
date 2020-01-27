# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    # Find length of pisano period of m
    prev = 0
    curr = 1

    for i in range(0,m*m):
        prev, curr = curr, (prev+curr) % m

        if (prev==0) and (curr==1):
            pisano_period = i + 1

    # Find n % m using the pisano period

    num = n % pisano_period

    if num == 0:
        return 0

    prev = 0
    curr = 1

    for i in range(num -1):
        prev, curr = curr, (prev+curr)

    return curr % m




if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
