def solution(s):
    s = s.lower()
    ans = ""
    tmp = ""
    table = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    for char in s:
        tmp += char
        if tmp in table.keys():
            ans += table[tmp]
            tmp = ""
        elif char in table.values():
            ans += char
            tmp = ''

    return int(ans)


if __name__ == '__main__':
    s_1 = "one4seveneight"
    # 1478

    s_2 = "23four5six7"
    # 234567

    s_3 = "2three45sixseven"
    # 234567

    print(solution(s_1))
