from typing import List

# Runtime: 44 ms, faster than 38.63% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.6 MB, less than 79.58% of Python3 online submissions for Search in Rotated Sorted Array.
def search1(nums: List[int], target: int) -> int:
    if target not in nums:
        return -1
    if target in nums:
        return nums.index(target)


# Runtime: 36 ms, faster than 89.61% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.4 MB, less than 93.12% of Python3 online submissions for Search in Rotated Sorted Array.
def search2(nums: List[int], target: int) -> int:
    if not nums:
        return -1

    # 최솟값 찾기
    left, right = 0, len(nums)-1
    while left < right:
        mid = left + (right-left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    pivot = left

    # 이진탐색
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left)//2
        mid_pivot = (mid+pivot) % len(nums)

        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    return -1


print(search2([4,5,6,7,0,1,2],0))
print(search2([4,5,6,7,0,1,2],3))
print(search2([1],0))
print(search2([5,1,3],5))



