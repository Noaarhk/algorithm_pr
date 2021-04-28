def solution_3(bridge_lenth, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_lenth

    while bridge:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time

# def solution(bridge_length, weight, truck_weights):
#     wait_l = []
#     # on_bridge = deque()
#     crossed = []
#     time = 0
#
#     for i in range(len(truck_weights)):
#         wait_l.append(truck_weights.pop())
#
#     # 대기열이나 다리에 트럭이 있는경우 과정 반복
#     while wait_l[-1] != 0 or on_bridge:
#         # 다리가 비어있는 경우
#         if not on_bridge:
#             on_bridge.append(wait_l.pop())
#             time += 1
#
#         # 다리에 다른 트럭이 있는경우
#         else:
#             # 최대 하중을 초과하지 않는 경우 다리에 추가  / error -> wait_l 이 비어있는 경우 wait_l [-1] 조회 불가.....
#
#             # 대기열이 비어있는 경우 0을 추가해준다.?
#             if not wait_l:
#                 wait_l.append(0)
#
#             if on_bridge[-1] + wait_l[-1] < weight:
#                 on_bridge.append(wait_l.pop())
#                 time += 1
#             # 최대 하중 초과하는 경우 다리에 있는 것 중 앞의 것 완료목록으로 보내기
#             else:
#                 while on_bridge:
#                     crossed.append(on_bridge.popleft())
#                 time += 2
#                 on_bridge.append(wait_l.pop())
#                 if not wait_l:
#                     wait_l.append(0)
#     return time


def solution_re(bridge_length, weight, truck_weights):
    truck_weights.reverse()
    wait = truck_weights
    crossed = []
    time = 0

    bridge_empty_check = []
    bridge_on = [[] for _ in range(bridge_length)]
    for i in range(bridge_length):
        bridge_empty_check.append(bool(bridge_on[i]))

    while True in bridge_empty_check or wait:

        # 다리가 비어있는경우
        for i in range(bridge_length):
            if True not in bridge_empty_check:

                bridge_on[-i - 1].append(wait.pop())
                time += 1
            # 다리가 비어있지 않는 경우
            else:
                # 다리 하중 검사
                # if bridge_on[-1]
                bridge_on[-i - 2].append(bridge_on[-i - 1].pop())
                time += 1

    # 2차배열 조작 불가 -> ㅍ포
    print(wait)
    print(bridge_on)
    print(bridge_empty_check)

    return time


if __name__ == '__main__':
    print(solution_3(2, 10, [7, 4, 5, 6]))