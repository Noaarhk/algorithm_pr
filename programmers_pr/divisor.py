def my_solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0:
        answer.append(-1)

    answer.sort()

    return answer


def gods_solution(arr, divisor):
    # python은 or 앞이 참일경우 해당 값까지만 , 거짓일경우 뒤에 것 호출
    return sorted(n for n in arr if n % divisor == 0) or [-1]


if __name__ == '__main__':
    arr = [5, 9, 7, 10]
    print(gods_solution(arr, 100))

    a = "aav"
    b = a.upper()
    print(b)
    # asjkldf = [ i for i in arr if i % 100 == 0] or [-1]
    # print(asjkldf)
