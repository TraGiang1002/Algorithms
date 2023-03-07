from typing import List
def jump(self, nums: List[int]) -> int:
    n = len(nums)
    count = 0
    for i in range(n):
        while ((i + nums[i]) >= n):
            i = i + nums[i]
            # nums[i] = nums[i+nums[i]]
            count = count + 1
    return count

# nums = [2,3,1,1,4]
nums = [2,3,0,1,4]
print(jump(nums))