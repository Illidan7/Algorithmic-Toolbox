# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements, hi, lo = 0):
    assert len(elements) <= 10 ** 5

    # x = round(len(elements)/2)
    # el1 = elements[0:x]
    # el2 = elements[x:len(elements)]

    # print("Elements are :", elements[lo:hi])

    # If only one element in series return it
    if lo == hi or hi-lo == 1:
        # print("Returning {}".format(elements[lo]))
        return elements[lo]

    # Recurse on two halves of element list
    mid = (hi-lo)//2 + lo
    # print("Left side mid:{} low:{}".format(mid,lo))
    left = majority_element(elements, mid, lo)
    # print("Left returned: {}".format(left))
    # print("Right side hi:{} mid:{}".format(hi,mid))
    right = majority_element(elements, hi, mid)
    # print("Right returned: {}".format(right))

    # If two halves same majority element
    if left == right:
        # print("Both halves same")
        return left

    # Else count and return
    lmaj_count = sum(1 for i in range(lo, hi) if elements[i] == left)
    rmaj_count = sum(1 for i in range(lo, hi) if elements[i] == right)

    return left if lmaj_count > rmaj_count else right



if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    e = majority_element(input_elements, input_n)

    # print("Majority element is :", e)

    if input_elements.count(e) > len(input_elements) / 2:
        print(1)
    else:
        print(0)
