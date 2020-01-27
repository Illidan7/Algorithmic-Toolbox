# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 3 * 10 ** 4

    # keys.sort()

    # print(keys)
    # print("The query is", query)

    # try:
    #     return keys.index(query)
    # except:
    #     return -1

    # r = 1

    # idx = 0
    #
    # keyorig = keys.copy()
    #
    # while len(keys) > 0:
    #     # print("Run no. {}".format(r))
    #     # r += 1
    #     m = len(keys)//2
    #     # print("Custom index:", idx)
    #     # print("Mid index: {} Mid element: {} ".format(m, keys[m]))
    #     if keys[m] == query and idx == 0:
    #         # print("Found")
    #         return m
    #     if keys[m] == query and idx !=0:
    #         # print("Found")
    #         return idx + m + 1
    #     if keys[m] > query:
    #         # print("Lower half")
    #         keys = keys[0:m]
    #         # print(keys)
    #     else:
    #         # print("Upper half")
    #         if idx == 0:
    #             idx += m
    #         else:
    #             idx = idx + m + 1
    #         keys = keys[m+1:len(keys)]
    #         # print(keys)
    #
    # return -1

    l = 0
    r = len(keys) - 1
    while l<=r:
        m = (l+r)//2
        if query > keys[m]:
            l = m + 1
        elif query < keys[m]:
            r = m - 1
        else:
            return m
    return -1




if __name__ == '__main__':
    # input_keys = list(map(int, input().split()))[0:]
    # input_queries = list(map(int, input().split()))[0:]

    input_keys = [int(i) for i in input().split()]
    input_queries = [int(i) for i in input().split()]

    #numkeys = input_keys[0]
    keyelements = input_keys[1:]

    queryelements = input_queries[1:]

    for q in queryelements:
        print(binary_search(keyelements, q), end=' ')
