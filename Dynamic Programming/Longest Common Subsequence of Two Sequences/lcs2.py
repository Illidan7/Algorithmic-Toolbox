# python3

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

def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    return edit_distance(first_sequence, second_sequence)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
