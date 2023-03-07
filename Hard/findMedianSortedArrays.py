from typing import List
import numpy as np
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    x = np.array(nums1)
    y = np.array(nums2)
    arrConcat = np.concatenate((x, y))
    return (np.median(arrConcat, axis=None))

nums1 = [1,3]
nums2 = [2]

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))