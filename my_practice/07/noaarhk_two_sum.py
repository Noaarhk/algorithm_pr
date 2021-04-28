from typing import List


# brute force
class Solution_0:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# use dict, enumerate
class Solution_1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_d = {}
        for i, num in enumerate(nums):
            nums_d[num] = i
        for i, num in enumerate(nums):
            if target - num in nums_d and i != nums_d[target - num]:
                return [nums.index(num), nums_d[target - num]]


if __name__ == "__main__":
    solution_0 = Solution_0()
    solution_1 = Solution_1()

    nums = [2, 7, 11, 15]
    target = 9

    print(solution_0.twoSum(nums, target))
    print(solution_1.twoSum(nums, target))
