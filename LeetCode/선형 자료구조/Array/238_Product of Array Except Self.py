def productExceptSelf(nums):
    out = [1 for _ in range(len(nums))]
    p = 1
    # 왼쪽 곱셈
    for i in range(len(nums)):
        out[i] *= p
        p *= nums[i]
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums)-1, -1, -1):
        out[i] *= p
        p *= nums[i]
    return out

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))