'''
공채 기출 1번 기억

학생들이 상호평가 한 2차배열 given
자기자신이 평가한 점수가 최고점이거나 최소점이고 유일한 점수인 경우 제외하고 평균낸다.
<ex>
학생 1  2  3
[ [90,70,30],
  [45,50,60],
  [53,26,96],
]
평균
등급

<ex_2>
score = [[50, 90], [50, 87]]
    # 예상 "DA"

'''
import collections


def solution(s):
    s_t = [[0 for _ in range(len(s))] for _ in range(len(s))]

    for i in range(len(s)):
        for j in range(len(s)):
            s_t[j][i] = s[i][j]

    cnt_s_t = {}
    ave = []
    result = ""

    for i in range(len(s)):
        cnt_s_t[i] = collections.Counter(s_t[i])

    for i in range(len(s)):
        len_s = len(s)

        # if s_t[i][i] == max(s_t[i]) | min(s_t[i][i]) and cnt_s_t[i][s_t[i][i]] == 1:
        if s_t[i][i] == max(s_t[i]) or s_t[i][i] == min(s_t[i]):
            if cnt_s_t[i][s_t[i][i]] == 1:
                s_t[i][i] = 0
                len_s -= 1
        ave.append(sum(s_t[i]) / len_s)

        if ave[i] < 50:
            result += 'F'
        elif ave[i] < 70:
            result += 'D'
        elif ave[i] < 80:
            result += 'C'
        elif ave[i] < 90:
            result += 'B'
        else:
            result += 'A'

    return result


if __name__ == '__main__':
    score = [[50, 90], [50, 87]]
    # 예상 "DA"
    print(solution(score))
