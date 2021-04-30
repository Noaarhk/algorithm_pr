import collections


def hap(x, y):
    return x + y


print(hap(1, 2))

print((lambda x, y: x + y)(1, 2))

# map(함수, 리스트) -> 리스트로부터 원소를 하나씩 꺼내서 함수를 적용시키고 결과를 새로운 리스트에 담아준다.
answer = list(map(lambda x: x ** 2, range(5)))
print(answer)




    # if phone_book[0] in phone_book[1:][:3]:
    #     return False


# reduce(함수, 순서형 자료(문자열, 리스트, 튜플)) - 순서형 자료의 원소들을 누적적으로 함수에 적용시킨다.

from functools import reduce

#
# answer_2 = reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
# print(answer_2)
# answer_3 = reduce(lambda x, y: y + x, 'abcde')
# print(answer_3)
#
# # filter(함수, 리스트)
# answer_4 = list(filter(lambda x: x < 5, range(10)))
# print(answer_4)
# # 1 = True, 0 = False - 구분하기
# answer_5 = list(filter(lambda x: not x % 2, range(10)))
# print(answer_5)

# sorted( key : lambda)
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age

print(solution())
