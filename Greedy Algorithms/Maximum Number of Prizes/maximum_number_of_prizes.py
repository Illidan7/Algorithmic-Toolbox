# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    x = 0
    tot = n

    while n > 0:
        x = x + 1
        summands.append(x)
        n = n - x
        #print(n)
        if n <= x :
            summands.pop()
            lastnum = tot - sum(summands)
            summands.append(lastnum)
            break

    #summands.pop()
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
