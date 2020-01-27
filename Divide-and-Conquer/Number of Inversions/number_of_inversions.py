# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def Merge(b,c):

    d = []
    ninv = 0

    # print("Merging {} and {}".format(b,c))

    while len(b) != 0 and len(c) != 0:
        # print(d)
        b1 = b[0]
        c1 = c[0]
        if b1 <= c1:
            d.append(b1)
            del b[0]
        else:
            d.append(c1)
            ninv += len(b)
            del c[0]

    if len(b) != 0:
        for i in range(len(b)):
            d.append(b[i])
            # print(d)
    else:
        for i in range(len(c)):
            d.append(c[i])
            # print(d)

    return d, ninv


def MergeSort(a):
    ninv = 0
    if len(a) == 1:
        return a, ninv
    m = len(a)//2
    # print("b:{} c:{}".format(a[0:m], a[m:len(a)]))
    b, ninvr = MergeSort(a[0:m])
    c, ninvl = MergeSort(a[m:len(a)])
    aa, ninv = Merge(b,c)

    return aa, ninv + ninvr + ninvl

def compute_inversions(a):
    MergeSort(a)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    # print("Input ok")
    # print(elements)
    sorted_elements, ninv = MergeSort(elements)
    # print("Sorted array: {}".format(sorted_elements))
    # print("Number of inversions: {}".format(ninv))
    print(ninv)
