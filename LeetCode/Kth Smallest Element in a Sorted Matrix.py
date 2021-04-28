from typing import List

# Runtime: 212 ms, faster than 37.18% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 79.06% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
def kthSmallest1(matrix: List[List[int]], k: int) -> int:
    target = sorted(sum(matrix,[]))[k-1]
    return target

# Runtime: 168 ms, faster than 77.05% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.2 MB, less than 48.71% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
def kthSmallest2(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    small, big = matrix[0][0], matrix[n-1][n-1]
    while small <= big:
        val = small + (big-small)//2
        cnt = check(matrix, val)
        if cnt < k:
            small = val + 1
        else:
            big = val - 1
    return int(small)

# 크기에 따른 순서 리턴 함수
def check(matrix, val):
    i = 0; j = len(matrix[0])-1
    cnt = 0
    while i < len(matrix) and j >= 0:
        if matrix[i][j] > val:
            j -= 1
        else:
            cnt += j+1
            i += 1
    return cnt


print(kthSmallest2([[1,5,9],[10,11,13],[12,13,15]], 8))
print(kthSmallest2([[-5]], 1))
print(kthSmallest2([[1,4],[2,5]],2))




