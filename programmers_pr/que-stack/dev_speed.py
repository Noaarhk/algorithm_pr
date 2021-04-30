from collections import deque


def solution(progresses, speeds):
    rest_work = list(map(lambda x, y: x - y, [100] * len(progresses), progresses))
    # print("rest_work : ", rest_work)
    answer = []
    while progresses:
        rest_day = []
        cnt = 0

        for i in range(len(progresses)):
            rest_day.append(rest_work[i] // speeds[i])

        # print("rest_day : ", rest_day)
        tmp = rest_day.copy()

        for i in range(len(progresses)):
            # print("tmp[0] : ", tmp[0])
            rest_day[i] -= tmp[0]
            if rest_day[i] <= 0:
                progresses.pop(0)
                cnt += 1
            else:
                break

        answer.append(cnt)

    return answer


# def solution_2t(progresses, speeds):
#     answer = []
#     cnt = 0
#
#     while progresses:
#         cur = progresses.copy()
#         p = (100 - cur[0]) // speeds[0]
#         for i in progresses:
#             cur[i] = i + p
#
#         for i in range(len(progresses)):
#
#             if cur[i] >= 100:
#                 progresses.pop(0)
#                 speeds.pop(0)
#                 cnt += 1
#             else:
#                 answer.append(cnt)
#                 continue
#
#         answer.append(cnt)
#
#     return answer

def solution_3(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:

        cnt = 0
        p = (100 - progresses[0]) / speeds[0]

        for i in range(len(progresses)):
            progresses[i] += (p * speeds[i])

        while progresses[0] >= 100:
            cnt += 1

            progresses.popleft()
            speeds.popleft()

            if not progresses:
                break

        answer.append(cnt)

    return answer


if __name__ == '__main__':

    # progresses = [93, 30, 55]
    # speed = [1, 30, 5]

    progresses = [2,2,1,2]
    speed = [1,1,1,1]

    # progresses = [95, 90, 99, 99, 80, 99]
    # speed = [1, 1, 1, 1, 1, 1]

    print(solution_3(progresses, speed))
