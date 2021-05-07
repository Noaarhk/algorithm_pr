from typing import List


def _multi(l):
    return l[0] * l[-1]


def solution(brown, yellow):
    y_list = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y_list.append((yellow // i, i))

    b_list = list(map(lambda x: (x[0] + 2, x[1] + 2), y_list))
    for i in range(len(b_list)):
        if _multi(b_list[i]) - _multi(y_list[i]) == brown:
            return list(b_list[i])


if __name__ == '__main__':
    b = 24
    y = 24
    answer = [4, 3]
    # print(_multi(answer))
    print(solution(b, y))
