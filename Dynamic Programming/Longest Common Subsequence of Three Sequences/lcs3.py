# python3

def edit_distance(p, q, r):
    dp_result = [[[0 for k in range(len(p)+1)] for j in range(len(q)+1)] for i in range(len(r)+1)]

    # for y in range(len(t) + 1):
    #     dp_result[y][0] = y

    for i in range(1, len(p)+1):
        for j in range(1, len(q)+1):
            for k in range(1, len(r)+1):
                skip1 = dp_result[i-1][j][k] #+ 1
                skip2 = dp_result[i][j-1][k] #+ 1
                skip3 = dp_result[i][j][k-1]
                match_op = dp_result[i-1][j-1][k-1] + 1
                #mismatch_op = dp_result[j-1][i-1] + 1
                if p[i-1] == q[j-1] and q[j-1] == r[k-1]:
                    dp_result[i][j][k] = match_op
                else:
                    dp_result[i][j][k] = max(skip1, skip2, skip3)

    return dp_result[len(p)][len(q)][len(r)]


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    return edit_distance(first_sequence, second_sequence, third_sequence)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
