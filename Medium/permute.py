from typing import List
def permute(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    answer = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if ((i != j) and (i != k) and (j != k)):
                    answer.append([nums[i], nums[j], nums[k]])
    return answer