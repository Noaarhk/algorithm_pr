def solution(numbers):
    _str_numbers = list(map(str, numbers))
    num_sorting = sorted(_str_numbers, key=lambda x: x * 4, reverse=True)
    # answer = "".join(num_sorting)
    # if int(answer) <= 0:
    #     return 0
    # # better way below
    return str(int("".join(num_sorting)))


# >> another one
import functools

def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))  # t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution_another(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer

    # _str_numbers = list(map(lambda x:str(x), numbers))
    # _str_lens = list(map(lambda x: len(x), _str_numbers))
    # first_num_sorting = sorted(_str_numbers, key=lambda x: x[0], reverse=True)
    # # second_num_sorting = sorted(first_num_sorting, key=lambda x: x[-1], reverse=True)
    # # third_num_sorting = sorted(second_num_sorting, key=lambda x: x[-2], reverse=True)
    # for i in range(1, max(_str_lens)):
    #     first_num_sorting = sorted(first_num_sorting, key=lambda x: x[-i], reverse=True)
    # return "".join(first_num_sorting)

    # for l, num in zip(_str_lens,_str_numbers):
    #     for i in range(max(_str_lens)):
    #
    # print(first_num_sorting)
    # print(second_num_sorting)
    # print("".join(second_num_sorting))

    # list(map(lambda x: x[0]),numbers)

    # for i in range(len(numbers)):


if __name__ == '__main__':
    numbers_4 = [0, 0, 0, 0]
    numbers_3 = [6, 10, 2, 100]
    numbers_1 = [6, 10, 2]
    numbers_2 = [3, 30, 34, 5, 9]
    print(solution(numbers_4))
