from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for index, element in enumerate(nums):
            t = target - element
            if t in sum_dict:
                return [sum_dict[t], index]
            sum_dict[element] = index


if __name__ == '__main__':
    sln = Solution()
    print(sln.twoSum([3, 2, 4], 6))
