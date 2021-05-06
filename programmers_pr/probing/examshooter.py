def solution(answers):
    students = ["12345", "21232425", "3311224455"]
    counts = [0] * 3
    answer = []
    # inefficient
    for i in range(len(students)):
        while len(students[i]) < len(answers):
            students[i] += students[i]

        # print(students)
        for j in range(len(answers)):
            if students[i][j] == str(answers[j]):
                counts[i] += 1

    en = []
    for i, v in enumerate(counts):
        en.append((v, i))

    # counts 중복이 없을 때
    if len(set(counts)) == len(counts):
        return [max(en)[1] + 1]

    # 중복이 있을 때, 정렬시 앞의 두개가 같거나 모두같거나 두가지경우
    else:
        for i in range(3):
            if max(counts) == en[i][0]:
                answer.append(en[i][1] + 1)
        return answer


def better_solution(answers):
    students = ["12345", "21232425", "3311224455"]
    counts = [0] * 3
    answer = []
    # inefficient
    for i in range(len(students)):
        while len(students[i]) < len(answers):
            students[i] += students[i]

        # print(students)
        for j in range(len(answers)):
            if students[i][j] == str(answers[j]):
                counts[i] += 1
    en = []
    for i, v in enumerate(counts):
        en.append((v, i))
        if max(counts) == en[i][0]:
            answer.append(en[i][1] + 1)
    return answer


def efficient_sol(answers):
    student = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    results = []
    answer = []

    for j in range(len(student)):
        cnt = 0
        for i in range(len(answers)):
            if answers[i] == student[j][i % len(student[j])]:
                cnt += 1
        results.append(cnt)

    for i, v in enumerate(results):
        if max(results) == v:
            answer.append(i + 1)
    return answer


def god_sol(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]


if __name__ == '__main__':
    answers = [1, 3, 2, 4, 2]
    print(efficient_sol(answers))
