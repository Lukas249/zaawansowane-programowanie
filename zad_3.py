from typing import List


def fn(nums: List[int]) -> None:
    for num in nums:
        if num % 2 == 0:
            print(num)


nums = list(range(10))

fn(nums)