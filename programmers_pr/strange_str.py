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
    print(solution_0(s))
