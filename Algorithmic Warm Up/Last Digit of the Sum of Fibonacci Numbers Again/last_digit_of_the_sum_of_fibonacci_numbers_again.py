# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10

def fibsum_lastdigit(m):
    pisano = 60

    if m < 0:
        return 0

    if m < 2:
         return m

    m = m % pisano
    prev = 1
    curr = 1

    for i in range(m):
        prev, curr = curr, ((prev+curr) %10)

    return (curr - 1) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18


    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    sumto = fibsum_lastdigit(to_index)
    sumfrom = fibsum_lastdigit(from_index-1)

    # if from_index < 2:
    #     sumfrom = from_index
    #
    # if to_index < 2:
    #     sumto = to_index

    return x[sumto - sumfrom]

    # pisano = 60
    #
    # if to_index < 2:
    #     sumto = to_index
    #
    # to_index = to_index % pisano
    # prev = 1
    # curr = 1
    #
    # for i in range(to_index):
    #     prev, curr = curr, ((prev+curr) %10)
    #
    # sumto = (curr - 1) % 10
    #
    #
    # if from_index < 2:
    #     sumto = to_index
    #
    # to_index = to_index % pisano
    # prev = 1
    # curr = 1
    #
    # for i in range(to_index):
    #     prev, curr = curr, ((prev+curr) %10)
    #
    # sumto = (curr - 1) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
