# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):


    numseg = len(segments)
    idx = 0
    visits = []

    segments.sort(key = lambda x: x[1])
    #
    # while idx < numseg:
    #
    #     curr = segments[idx]
    #
    #     while idx < numseg-1 and curr[1] > segments[idx+1][0]:
    #         idx += 1
    #
    #     visits.append(curr[1])
    #     idx += 1






    # origsegs = segments.copy()
    #
    # # print("All segments")
    # # print(segments)
    #
    while numseg > 0:

        lmost = segments[0]
        lmost_idx = 0

        for i, segment in enumerate(segments):
            if segment.start <= lmost.end:


        # print("Number of segments remaining")
        # print(numseg)

        visitnum = 0

        for i, segment in enumerate(segments):
            if segment.start < lmost.start:
                lmost = segment
                lmost_idx = i

        maxseg = 1
        segscovered = [lmost_idx]

        # print("Left most segment found")
        # print(lmost.start, lmost.end, lmost_idx)

        for n in range(lmost.start, lmost.end+1):

            nseg = 1
            segs = [lmost_idx]

            for i, segment in enumerate(segments):

                if i != lmost_idx:

                    if segment.start <= n <= segment.end:
                        nseg += 1
                        segs.append(i)

            if nseg >= maxseg:
                maxseg = nseg
                segscovered = segs
                visitnum = n

        # print("Visit at")
        # print(visitnum)
        # print("Segments covered:")
        # print(maxseg)
        # print("")




        visits.append(visitnum)
        # print("All visits so far")
        # print(visits)
        numseg -= maxseg
        # print("Segments covered in run:")
        # print(segscovered)
        segscovered.sort(reverse=True)
        for i in segscovered:
            # print(i)
            segments.pop(i)
        # print("Segments remaining")
        # print(segments)



    return visits



if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    # n = int(input())
    # data = list(map(int, input().split()))
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
