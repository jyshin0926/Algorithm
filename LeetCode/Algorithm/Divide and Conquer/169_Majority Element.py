from collections import Counter, defaultdict

# 그냥 pythonic하게 풀기 - 빠름
# Runtime: 156 ms, faster than 95.07% of Python3 online submissions for Majority Element.
# Memory Usage: 15.4 MB, less than 82.82% of Python3 online submissions for Majority Element.
def solution4(nums):
    return sorted(nums)[len(nums)//2]


# 분할정복
# Runtime: 244 ms, faster than 20.08% of Python3 online submissions for Majority Element.
# Memory Usage: 15.6 MB, less than 51.81% of Python3 online submissions for Majority Element.
def solution3(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    half = len(nums)//2
    a = solution3(nums[:half])
    b = solution3(nums[half:])

    # a가 만약 현재 분할된 리스트 nums에서 과반수를 차지한다면 해당 인덱스는 1이 되고
    # [b,a][1]이 되어 a를 리턴하고 이외에는 b를 리턴
    print('출력:',[b,a][nums.count(a) > half])
    return [b,a][nums.count(a) > half]


# 메모이제이션 활용한 dp
# Runtime: 164 ms, faster than 79.49% of Python3 online submissions for Majority Element.
# Memory Usage: 15.6 MB, less than 51.81% of Python3 online submissions for Majority Element.
def solution2(nums):
    counts = defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)
        # 앞에서부터 하나씩 과반수를 넘는지 체크하다가 과반수를 넘으면 정답처리
        if counts[num] > len(nums) // 2:
            return num


# Counter 이용
# Runtime: 152 ms, faster than 98.27% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 51.81% of Python3 online submissions for Majority Element.
def solution1(nums):
    return Counter(nums).most_common(1)[0][0]

print(solution3([3,2,3]))
print(solution3([2,2,1,1,1,2,2]))