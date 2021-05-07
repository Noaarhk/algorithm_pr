'''
문제 설명
배열이 하나 입력됩니다. 배열의 각 원소에 대해 해당 원소의 값보다 큰 원소들 중에서 해당 원소와 가장 가까운 위치에 있는 원소의 인덱스를 찾아주세요.

조건:

특정 원소에 대해, 해당 원소보다 큰 원소가 없다면 -1을 정답으로 합니다.
가장 가까운 원소가 하나 이상이라면, 인덱스가 가장 작은 것을 정답으로 합니다.
각 원소는 0과 100,000 사이의 값입니다.
입력 배열의 길이는 0부터 100,000 사이입니다.
인덱스는 0부터 시작합니다.
이 문제에는 알고리즘의 효율성을 측정하기 위한 테스트 케이스가 포함되어 있으며, 모든 테스트 케이스를 통과하려면 시간복잡도 O(n) 이상의 알고리즘이 필요합니다.

    <ex>
    array = [3, 5, 4, 1, 2]
    answer = [1, -1, 1, 2, 2]
'''


#
# def solution(array):
#     ans = [0] * len(array)
#     en = []
#     for i, v in enumerate(array):
#         en.append((v, i))
#
#     # i = index
#     for i in range(len(en)):
#         dist = 0
#         tmp = []
#         if en[i][0] >= max(en)[0]:
#             ans[en[i][1]] = -1
#         # print(ans)
#         for j in range(len(en)):
#             if en[i][0] < en[j][0]:
#                 tmp.append(en[j])
#         # 거리측정
#         # dist_dict = {}
#         # for v, k in tmp:
#         #     abs(en[i][1] - tmp[k][1])
#         # print(dist_dict)
#
#         # dist = min(dist, abs(en[i][1] - tmp[k][1]))

def solution(array):
    ar_en = []

    for i, v in enumerate(array):
        ar_en.append((v, i))

    ans = [0] * len(array)
    print(ar_en)
    for v, i in ar_en:
        tmp = []
        for j in range(len(array)):
            if v < array[j]:
                tmp.append((abs(i - j), j))
        # print('tmp = ', tmp)
        # print('min(tmp) = ',min(tmp))

        if not tmp:
            ans[i] = -1
        else:
            ans[i] = min(tmp)[1]

        # print('ans = ', ans)

    return ans


def sol_2t(array):
    ans = [0] * len(array)

    for i, v in enumerate(array):
        tmp = []
        for j in range(len(array)):
            if v < array[j]:
                tmp.append((abs(i - j), j))

        if not tmp:
            ans[i] = -1
        else:
            ans[i] = min(tmp)[1]

    return ans

    #
    # for i, v in ar_en:
    #     tmp = []
    #     for j in range(len(array)):
    #         if v < array[j]:
    #             tmp.append((abs(i - j), i))
    #
    #     ans[min(tmp)[1]] = min(tmp)[0]
    #
    #     if not tmp:
    #         ans[i] = -1
    #
    # return ans

    # ans = [0] * len(array)
    # tmp = []
    # for i, v in ar_en:
    #     for j in range(len(array)):
    #         if v < array[j]:
    #             tmp[i] = array[j]
    #
    #     if not tmp:
    #         tmp[i] = -1


if __name__ == '__main__':
    array = [3, 5, 4, 1, 2]
    # array = [3, 5, 1, 5, 4, 3]

    answer = [1, -1, 1, 2, 2]
    print(solution(array))
    print(sol_2t(array))



    # for k, v in enumerate(array):
    #     dict_[k] = v
    #
    #
    # bb = list(zip(array,answer))
    # print(bb[3:])
    # # print(dict_[:1])
    # print(max(dict_.values()))

    #
    # s_a = sorted(array)
    # print(max(answer[0],answer[2]))
