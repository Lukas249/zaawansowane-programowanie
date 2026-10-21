from typing import List


def fn_1(nums: List[int]) -> List[int]:
    result = []

    for num in nums:
        result.append(num * 2)

    return result


print(fn_1([1, 2, 3, 4, 5]))


def fn_2(nums: List[int]) -> List[int]:
    return [x * 2 for x in nums]


print(fn_2([1, 2, 3, 4, 5]))
