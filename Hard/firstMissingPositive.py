from typing import List
def firstMissingPositive(nums: List[int]) -> int:
    ListMiss = [i for i in range(1, 10)]
    n = len(ListMiss)
    for x in nums:
        for i in ListMiss:
            if (i == x):
                ListMiss.remove(x)
    return (ListMiss[0])
nums = [1,2,0]
# nums = [3,4,-1,1]
# nums = [7,8,9,11,12]
print(firstMissingPositive(nums))