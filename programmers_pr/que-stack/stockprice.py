from collections import deque


def solution_on2(prices):
    answer = [0] * len(prices)
    for i in range(len(prices) - 1):
        for k in range(i, len(prices) - 1):
            if prices[i] > prices[k]:
                break
            else:
                answer[i] += 1
    return answer


# def solution_er1(prices):
#     answer = []
#     i = 0
#     while 1 < len(prices):
#
#         if prices[0] <= min(prices[1:]):
#             answer.append(len(prices) - 1)
#         else:
#             answer.append(prices.index(min(prices[1:])))
#
#         prices.pop(0)
#
#     answer.append(0)
#
#     return answer

#
# def solution_err2(prices):
#     stack = prices.copy()
#     answer, seen = [], []
#     while stack:
#         seen.append(stack.pop(0))
#         for i in stack:
#             if seen[-1] > i:
#                 l = prices.index(seen[-1])
#                 r = prices.index(i)
#                 answer.append(r - l)
#     return answer

def solution_queue(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer

# def solution_err3(prices):
#     answer = []
#     for i in range(len(prices) - 1):
#         if prices[i] <= min(prices[i + 1:]):
#             answer.append(len(prices) - 1 - i)
#
#         else:
#             answer.append(prices.index(min(prices[i + 1:])) - i)
#             # error : price.index( 값) 값이 중복된 경우 앞의 인덱스를 리턴한다.
#     answer.append(0)
#
#     return answer


if __name__ == '__main__':
    a = [1, 2, 3, 2, 3]

    b = [5, 2, 1, 0, 4, 10, 5]
    print(solution_queue(b))
