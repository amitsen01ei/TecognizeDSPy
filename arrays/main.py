from typing import List


def lin_search(list: List[int], target: int):
    for index, element in list:
        if element == target:
            return index

    return -1


def print_hi():

    li = [2, 3, 4, 5]
    print(len(li))
    print(li[2])
    new_li = list(filter(lambda x: x % 2 == 0, li))
    print(new_li)


def reverse(li):
    start = 0
    end = len(li) - 1

    while start < end:
        temp = li[start]
        li[start] = li[end]
        li[end] = temp
        start += 1
        end -= 1


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5]
    reverse(li)
    print(li)
