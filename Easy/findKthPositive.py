from typing import List
def findKthPositive(arr: List[int], k: int) -> int:
    ListMiss = [i for i in range(1, 1000)]
    n = len(ListMiss)
    for x in arr:
        for i in ListMiss:
            if (i == x):
                ListMiss.remove(x)
    if k <= n:
        answer = ListMiss[k - 1]
    else:
        answer = ListMiss[-1]
    return (answer)

# arr = [2,3,4,7,11]
# k = 5
arr = [1,2,3,4]
k = 2
print(findKthPositive(arr, k))