class My_Solution():
    def is_True(self, arr, h):
        bigger_num = []
        for num in arr:
            if num >= h:
                bigger_num.append(num)
        if len(bigger_num) >= h:
            return True
        else:
            return False

    def is_True_2(self, arr, h):
        if len(list(filter(lambda x: x >= h, arr))) >= h:
            return True
        else:
            return False

    def solution(self, citation):
        cnt = 0

        while True:
            if len(citation) == 1 or int("".join(map(str, citation))) == 0:
                return 0
            elif self.is_True_2(citation, cnt):
                cnt += 1
            else:
                cnt -= 1
                break
        return cnt

    def solution_2(self, citation):
        cnt = 0
        while True:
            if self.is_True_2(citation, cnt):
                cnt += 1
            else:
                cnt -= 1
                break
        return cnt




class Other_Solution():

    def counting(self, l, n):
        return len(list(filter(lambda x: x >= n, l)))

    def solution(self, citations):
        answer = 0
        for i in range(max(citations)):
            if self.counting(citations, i) >= i:
                answer = i
            else:
                break
        return answer


if __name__ == '__main__':
    citation = [3, 0, 6, 1, 5]

    result = 3

    solution_1 = My_Solution()
    solution_2 = Other_Solution()

    print(solution_1.solution(citation))
    print(solution_1.solution_2(citation))
    print(solution_2.solution(citation))
