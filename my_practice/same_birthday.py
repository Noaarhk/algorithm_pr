import random

class Solution:
    def samebday(self,trial:int):
        same_birthdays = 0

        for _ in range(trial):
            birthdays = []

            for i in range(23):
                birthday = random.randint(1, 365)
                if birthday in birthdays:
                    same_birthdays += 1
                    break
                birthdays.append(birthday)
                
        # trial 만큼 시도 중 23명중 동일 생일자가 있을 확률
        print(f'{same_birthdays / trial * 100}%')

if __name__ == '__main__':

    solution = Solution()
    solution.samebday(100000)



