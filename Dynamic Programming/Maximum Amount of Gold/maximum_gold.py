# python3

from sys import stdin

def edit_distance(s, t):
    dp_result = [[0 for x in range(len(s) + 1)] for y in range(len(t) + 1)]
    # for y in range(len(t) + 1):
    #     dp_result[y][0] = y

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            insert_op = dp_result[j-1][i] #+ 1
            delete_op = dp_result[j][i-1] #+ 1
            match_op = dp_result[j-1][i-1] + 1
            #mismatch_op = dp_result[j-1][i-1] + 1
            if s[i-1] == t[j-1]:
                dp_result[j][i] = match_op
            else:
                dp_result[j][i] = max(insert_op, delete_op)

    return dp_result[len(t)][len(s)]

def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    bkpkconf = [[0 for c in range(capacity+1)] for w in range(len(weights)+1)]

    # print(bkpkconf)

    for w in range(1, len(weights)+1):
        for c in range(1, capacity+1):
            bkpkconf[w][c] = bkpkconf[w-1][c]
            if weights[w-1] <= c:
                val = bkpkconf[w-1][c-weights[w-1]] + weights[w-1]
                if bkpkconf[w][c] < val:
                    bkpkconf[w][c] = val

    return bkpkconf[len(weights)][capacity]

# def optimal_weight(W, w):
#     dp_result = [[0 for x in range(W + 1)] for y in range(n + 1)]
#
#     for i in range(1, n+1):
#         for weight in range(1, W+1):
#             dp_result[i][weight] = dp_result[i-1][weight]
#             if w[i-1] <= weight:
#                 val = dp_result[i-1][weight - w[i-1]] + w[i-1]
#                 if val > dp_result[i][weight]:
#                     dp_result[i][weight] = val
#
#     # return dp_result
#     return dp_result[n][W]



if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))

    # print(optimal_weight(input_capacity, input_weights))
