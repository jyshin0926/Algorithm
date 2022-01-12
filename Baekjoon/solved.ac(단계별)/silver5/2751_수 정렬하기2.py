# 풀이 2
import sys
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i,j,k = 0,0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
    return arr

n = int(sys.stdin.readline())
tmp = []

for _ in range(n):
    tmp.append(int(sys.stdin.readline()))

tmp = merge_sort(tmp)
print(*tmp, sep='\n')

# 풀이 1

# n = int(sys.stdin.readline())
# tmp = []
# for i in range(n):
#     tmp.append(int(sys.stdin.readline()))
#
# tmp.sort()
# print(*tmp, sep='\n')
