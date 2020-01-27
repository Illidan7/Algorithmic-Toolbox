# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    n_stops = 0
    pos = 0

    stops.append(d)

    #print(stops)
    #print(stops[0])

    allstops = stops.copy()
    allstops.insert(0, 0)

    # print(stops)
    # print(stops[0])


    for i in range(len(stops)):

        #print("Loop ", i, stops[i])

        maxdist = pos + m
        #print(stops[i]-pos)
        if stops[i] > maxdist:
            # print(stops[i])
            pos = allstops[i]
            n_stops += 1
            # print(pos)
            if stops[i]-pos > m:
                return -1

    return n_stops



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
