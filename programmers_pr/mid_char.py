def my_solution(s):
    '''
    1. enumerate -> dict
    2. 짝수 길이인 경우 [len // 2 : len // 2 + 2] return
    3. 홀수 길이인 경우 [len // 2 + 1] return

    -> 문자열 인덱스 조회되는거 까먹고 이상한 짓을 함
    '''

    s_dict = {}
    for i, v in enumerate(s):
        s_dict[i] = v

    if len(s) % 2 == 1:
        return s_dict[len(s) // 2]

    else:
        return s_dict[len(s) // 2 - 1] + s_dict[len(s) // 2]


def solution(s):
    return s[(len(s) - 1) // 2:len(s) // 2 + 1]


# (len(str)-1)//2:len(str)//2+1

if __name__ == '__main__':
    e = "abcd"
    o = "abcde"

    print(solution(o))
    print(solution(e))

    a = []
