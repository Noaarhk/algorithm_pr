# time out
def solution_0(s):
    s_dict = {}
    s_list = s.split(" ")
    result = []

    for i, word in enumerate(s_list):
        s_dict[i] = word

    for i in s_dict:
        ans = ""

        for j in range(len(s_dict[i])):
            if j % 2 == 0:
                ans += s_dict[i][j].upper()
            else:
                ans += s_dict[i][j].lower()

        result.append(ans)

    result = " ".join(result)

    return result


def solution_1(s):
    s_list = s.split(" ")
    print(s_list)

    return None


if __name__ == '__main__':
    s = "try hello world"
    dict = {}
    s_l = list(s)
    # for i in s.split(" "):
    #     dict[i].append(i)
    # print(solution_0(s))
    # s_l = [i for i in range(len(s)) if i % 2 == 0]
    # print([i for i in range(20)])
    a = sorted(enumerate(s.split(" ")))
    print(s.index('l'))  # -> 제일 먼저 나오는 인덱스 리턴
    print(s_l.index('l'))

