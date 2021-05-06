from collections import deque


def solution(priorities, location):
    pair = []
    for index, prior in enumerate(priorities):
        pair.append((prior, index))

    p_d = deque(pair)
    # print(p_d)
    # print(p_d[0])
    # print(max(p_d))
    while p_d[0][0] < max(list(p_d)[1:])[0]:
        # print(p_d[0])
        # print( max(list(p_d)[1:])[0])
        p_d.append(p_d.popleft())
    # print(p_d)
    for i in range(len(priorities)):
        if p_d[i][1] == location:
            return i + 1


if __name__ == '__main__':
    # A = list("abcd")
    # B = deque(A)
    # print(B)
    # B.append(B.popleft())
    # print(B)
    k = [1, 1, 3, 1, 8, 8]
    kk = 0
    priorities = [2, 1, 3, 2]
    location = 2
    # a = {(2, 0), (1, 1), (3, 2), (2, 3)}
    # b = {}
    # for v, i in a:
    #     b[i] = v
    #
    #
    # print(list(b.keys()))
    # print(max(list(b.keys())[1:]))

    ans = 1
    print(solution(k, kk))
    print(solution(priorities, location))
    # p_d = deque(priorities)
    # print(max)

    # print(list(priorities[][0]))
    # print(max(priorities[1:][0]))
    # if priorities[0][0] < max(priorities[1:][0]):
    #     print(solution(priorities, location))

    # pair = {}
    # for index, prior in enumerate(priorities):
    #     pair[index] = prior
    # print(list(pair.values()))
