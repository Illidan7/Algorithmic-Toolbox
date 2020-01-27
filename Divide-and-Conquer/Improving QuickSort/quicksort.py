# python3

from random import randint


def partition3(array, left, right):

    x = array[left]
    # print("Pivot elt: {}".format(x))
    # Index for < x
    j = left
    # Index for = x
    # s = left
    s = 0


    for i in range(left+1, right+1):
        if array[i] < x:
            j += 1
            array[j], array[i] = array[i], array[j]
        if array[i] == x:
            s += 1
            j += 1
            #array[left], array[i] = array[i], array[left]
            array.insert(left, array.pop(i))

    # print("All less than elements till: {}".format(j))
    # print("All same elements till: {}".format(s))


    for el in range(left, left+s+1):
            array[el], array[j] = array[j], array[el]
            if j > 0:
                j-=1

    if s == (j-left):
        # print("s: {} j: {} left: {}".format(s,j,left))
        return left, s
    else:
        return j+1, j+1+s#j+s-left

    # m2 = left
    # for i in range(left+1, right):
    #     if array[i] <= array[left]:
    #         array[m2+1], array[i] = array[i], array[m2+1]
    #         m2 += 1
    #
    # array[left], array[m2] = array[m2], array[left]
    #
    # m1 = m2
    # for i in range(left, m2):
    #     if i == m1:
    #         break
    #     if array[i] == array[m2]:
    #         array[i], array[m1-1] = array[m1-1], array[i]
    #         m1 -= 1
    #
    # return m1, m2






def randomized_quick_sort(array, left, right):
    # print("Working on {} to {} of array".format(left, right))
    # if left >= right:
    #     # print("Array from {} to {} is sorted".format(left, right))
    #     return
    # k = randint(left, right)
    # # print("Random idx: {} Random elt: {}".format(k, array[k]))
    # array[left], array[k] = array[k], array[left]
    # m1, m2 = partition3(array, left, right)
    #
    # # print(array)
    # #
    # # print("m1:{} m2:{}".format(m1,m2))
    #
    # randomized_quick_sort(array, left, m1-1)
    # randomized_quick_sort(array, m2+1, right)

    while left < right:
        # Pivot element
        mid = (left+right)//2
        lst = [array[left], array[mid], array[right]]
        lst.sort()
        k = array.index(lst[1])
        # k = randint(left, right)
        # Move pivot element to first
        array[left], array[k] = array[k], array[left]
        # Call to partition
        m1, m2 = partition3(array, left, right)

        if (m1 - 1 - left) < (right - m2 + 1):
            randomized_quick_sort(array, left, m1-1)
            left = m2 + 1
        else:
            randomized_quick_sort(array, m2+1, right)
            right = m1 - 1






if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    #assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
