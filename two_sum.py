from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    sum_dict = {}
    for index, element in enumerate(nums):
        t = target - element
        if t in sum_dict:
            return [sum_dict[t], index]
        sum_dict[element] = index


if __name__ == '__main__':
    print(two_sum([3, 2, 4], 6))
