'''
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

array = [ 1,5,2,6,3,7,4] commands = [ [2,5,3], [4,4,1], [1,7,3] ] return = [5,6,3]
'''


def solution(array, commands):
    result = []
    # print(array)
    # print(array[commands[0][0] - 1:commands[0][1]])
    # print(sorted(array[commands[0][0] - 1:commands[0][1]]))
    # print(sorted(array[commands[0][0] - 1:commands[0][1]])[commands[0][2] - 1])
    for i in range(len(commands)):
        result.append(sorted(array[commands[i][0] - 1:commands[i][1]])[commands[i][2] - 1])

    return result


def simple_solution(array, commands):
    # map (함수, 리스트 ) 리스트의 각 요소를 함수에 넣어서 리스트에 반환한다.
    # 1. x = [2,5,3]
    # 2. x = [4,4,1]
    # 3. x = [1,7,3]
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))


if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))
