from typing import List


def intro():
    f = ("유남규", 12140952, False)
    print("my name is", f[0], "and student number is", f[1], "do I have a pet? ", f[2])


def q7():
    # a,b=map(str,input("두 단 입력하세요").split())
    a = input("암호를 입력하시오 : ")

    # 짧은 단어 우선
    if a == "ASC":
        b, c = input("2개의 단어 입력 : ").split()
        if len(b) < len(c):
            print(b, c)
        elif len(b) > len(c):
            print(c, b)
        else:
            print(b, c)
        exit()

    # 긴단어 우선
    elif a == "DESC":
        b, c = input("2개의 단어 입력 : ").split()
        if len(b) > len(c):
            print(b, c)
        elif len(b) < len(c):
            print(c, b)
        else:
            print(b, c)
        exit()

    else:
        print("잘못 입력하였습니다.")
        exit()


def sol_1(num: int):
    even = ""
    odd = ""

    for i in range(1, num + 1):
        if i % 2 == 1:
            odd += str(i) + " "
        else:
            even += str(i) + " "

    print(even)
    print(odd)


def sol_2(num: int):
    even = []
    odd = []

    for i in range(1, num + 1):
        if i % 2 == 1:
            odd.append(str(i))
        else:
            even.append(str(i))

    print(" ".join(even))
    print(" ".join(odd))


def sol_3(num: int):
    num_list = []
    for i in range(1, num + 1):
        num_list.append(i)

    for e in range(0, len(num_list), 2):
        print(e, end=" ")

    print()

    for o in range(1, len(num_list), 2):
        print(o, end=" ")


def snail(depth: int) -> int:

    day = 0

    # say the depth is height remaining to climb
    while depth > 0:
        depth -= 55
        depth += 13
        if depth > 0:
            day += 1

    return day


if __name__ == '__main__':
    # sol_1(10)
    # sol_2(10)
    # sol_3(10)

    print(snail(depth=300))
