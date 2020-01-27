# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def first_digit_2(nums):
    x = []
    for n in nums:
        x.append(n //10)

    return x

def first_digit_3(nums):
    x = []
    for n in nums:
        x.append(n //100)

    return x

def largest_number(numbers):
    # numbers = list(map(int, numbers))
    # nums = []
    # for num in numbers:
    #     nums.extend(list(map(int, str(num))))

    salary = ''

    numbers_info = {}

    for num in numbers:
        numbers_info

    numbers.sort(reverse=True)

    one_digit = []
    two_digit = []
    three_digit = []

    # Collect numbers based on digits
    for num in numbers:
        if len(num)==1:
            one_digit.append(num)
        if len(num)==2:
            two_digit.append(num)
        if len(num)==3:
            three_digit.append(num)

    one_digit.sort(reverse=True)
    two_digit.sort(reverse=True)
    three_digit.sort(reverse=True)

    for num in one_digit:


    two_digit_first = first_digit_2(two_digit)
    three_digit_first = first_digit_3(three_digit)

    for num in one_digit:
        if num in two_digit_first and num in three_digit_first:

        else:





    # Sort by minimum number of digits
    # In case of ties, check

    for i in range(len(numbers)):
        idx = numbers.index(max(numbers))



        if salary == '':
            salary += str(numbers[idx])
        else:
            if int(str(salary)+str(numbers[idx])) < int(str(numbers[idx])+str(salary)):
                salary = str(numbers[idx]) + salary
            else:
                salary += str(numbers[idx])

        numbers.pop(idx)

    return salary



if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
