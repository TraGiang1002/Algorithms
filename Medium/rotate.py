from typing import List
import numpy as np
def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    A = np.array(matrix)
    n = len(A[0,:])
    for i in range(n):
        A[i, :] = A[i-1, :]
    # for j in range(n):
    #     for i in range(n):
    #         A[i,j] = A[i-1,j-1]
    return A

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))
