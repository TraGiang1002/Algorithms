from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    answer = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if ((i != j) and (i != k) and (j != k) and (nums[i] + nums[j] + nums[k] == 0)):
                    answer.append([nums[i], nums[j], nums[k]])
    return answer

# nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
nums = [0,0,0]
print(threeSum(nums))