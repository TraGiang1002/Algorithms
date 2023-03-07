from typing import List
def searchInsert(nums: List[int], target: int) -> int:
    n = len(nums)
    for i in range(n):
        if (nums[i] == target):
            return i
        elif nums[0] > target:
            return 0
        elif nums[-1] < target:
            return n
        else:
            for i in range(len(nums) - 1):
                if nums[i] < target and nums[i + 1] > target:
                    return i + 1
nums = [1,3,5,6]
target = 5

# nums = [1,3,5,6]
# target = 2
#
# nums = [1,3,5,6]
# target = 7

print(searchInsert(nums, target))