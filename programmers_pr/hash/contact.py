'''
한 번호가 다른 번호의 접두사인 경우가 있으면 False, 아니면 True
'''

# 테스트케이스 3개 실패
# def my_solution(phone_book):
#
#     for left in range(len(phone_book)):
#         for right in range(left + 1, len(phone_book)):
#             if phone_book[left] == phone_book[right][:len(phone_book[left])]:
#                 return False
#     return True
#
# # 시간 복잡도?
def my_solution_2(phone_book):
    # phone_dict = {}
    # for item in phone_book:
    #     phone_dict[item] = 1
    for item in phone_book:
        temp = ''
        for number in item:
            temp += number
        if temp in item and temp != item:
            return False
    return True
#
#
#
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 return False
#     return answer
#
#
# def solution_2(phoneBook):
#     phoneBook = sorted(phoneBook)
#     print(phoneBook)
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         print("p1 = %s, p2 = %s" % (p1, p2))
#         if p2.startswith(p1):
#             return False
#     return True
import collections


def my_solution(phone_book):

    for item in phone_book:
        comp = list(map(lambda x: x[:len(item)], phone_book))
        for i in range(len(comp)):
            tmp = comp.copy()
            tmp.remove(comp[i])
            if comp[i] in tmp:
                return False
        return True




    # for item in phone_book:
    #     cmp = collections.Counter(list(map(lambda x: x[:len(item)], phone_book)))
    #     for i in cmp.values():
    #         if i > 1:
    #             return False
    # return True

def others_solution(phoneBook):

    phoneBook = sorted(phoneBook)
    print(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2 ,sep=',')
        if p2.startswith(p1):
            pass
    return True

if __name__ == '__main__':
    a = ["119", "97674223", "1195524421"]
    b = ["123", "456", "789"]
    c = ["12", "123", "1235", "567", "88"]
    print(my_solution_2(a))
    # print(others_solution(a))
