from typing import List


def fn_1(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        nums[i] *= 2

    return nums

print(fn_1([1,2,3,4,5]))

def fn_2(nums: List[int]) -> List[int]:
    return [x * 2 for x in nums]

print(fn_2([1,2,3,4,5]))


