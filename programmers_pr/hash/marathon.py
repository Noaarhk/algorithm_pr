# for k in range(len(a)):
#     if a[k] not in b:
#         print(a[k])
import collections


# not considering person with the same name
def solution_error(participants, completions):
    for participant in participants:
        if participant not in completions:
            print(participant)


#
def solution_n2(participants, completions):
    for completion in completions:
        for participant in participants:
            if completion == participant:
                del participant

    return participants[0]


def solution_n1(participants, completions):
    '''
    1. 참여자 전체중, 각 이름을 가진 사람의 수를 센다. collections.Counter
    -> 1보다 큰 경우 : 동명이인이 있는경우
    2. 완주자 명단에 같은 이름이 있는경우 1씩 뺀다.
    3. Counterdict의 값이 0보다 큰 경우 (= 1인 경우만 존재 )를 return
    => value로 key값을 찾아서 반환하기 위해서는 로직을 새로 짜야한다. 효율적이지 않음

    1. 동명이인 숫자를 센다. collection.Counter(participants)
    2. 완주자리스트의 이름을 하나씩 dict에 비교하며 dict에서 제거한다. 1보다 큰겨우는 1씩 빼고 1인경우는 아이템을 제거한다.  -> keys()로 출력하기 위함
    3. dict.keys() 는 class type이므로 list로 변환한다.
    4. 정답은 한명이고, str으로 받아야 하므로 list로 변환한 정보에서 첫번째 값을 인덱스[0]로 조회한다.
    '''

    prt_d = collections.Counter(participants)
    for completion in completions:
        if prt_d[completion] > 1:
            prt_d[completion] -= 1
        else:
            del prt_d[completion]
    return list(prt_d.keys())[0]


# dict 간 연산이 가능하다??? ㄷ ㄷ
def solution_of_god(participants, completions):
    prt_d = collections.Counter(participants)
    cmp_d = collections.Counter(completions)

    answer = prt_d - cmp_d
    return list(answer.keys())[0]

    # for completion in completions:
    #     if completion in prt_d:
    #         prt_d[completion] -= 1
    #         completions.remove(completion)ㄷ
    #
    #     if prt_d[completion] == 1:
    #         # prt_d 에서 value가 1인 key를 출력한다.
    #         return prt_d.keys()


# def solution_n2(participants, completions):
#     # 동명이인 고려
#     name = collections.Counter(participants)
#
#     for completion in completions:
#         #     for participant in participants:
#         #         if completion == participant:
#         #             del participant
#         #
#         # return participants[0]
#
#         if name[completion] > 1:
#             name[completion] -= 1
#         else:
#             del (name[completion])
#     return list(name.keys())


if __name__ == '__main__':
    a_1 = ["mislav", "stanko", "mislav", "ana", "mislav", "namgyu"]
    b_1 = ["stanko", "ana", "mislav"]

    # print(solution_error(a, b))
    # print(solution_n2(a, b))
    # print(solution_n1(a_1, b_1))
    # print(solution_n1(a, b))
    # print(solution_n1(a, b))
    # print(solution_of_god(a_1, b_1))

    print(collections.Counter(a_1) - collections.Counter(b_1))
