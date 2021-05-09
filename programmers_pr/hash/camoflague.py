import collections
from functools import reduce


def solution(clothes):
    cnt_categories = collections.Counter(list(map(lambda x: x[1], clothes)))
    nums_categories = list(cnt_categories.values())
    if len(nums_categories) <= 1:
        return nums_categories[0]
    else:
        cases = list(map(lambda x: x + 1, list(cnt_categories.values())))
        return reduce(lambda x, y: x * y, cases) - 1


if __name__ == '__main__':
    c = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    d = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(c))