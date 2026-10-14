from typing import List


def fn(nums: List[int]) -> None:
    for i in range(len(nums)):
        if i % 2 == 0:
            print(nums[i])


nums = list(range(1,11))

print("Wszystkie elementy:")
print(nums)
print("Co drugi element:")
fn(nums)