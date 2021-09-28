# len(nums)//2 만큼 페어 만들고,
# n개 페어를 이용한 min(a,b) 합으로 만들 수 있는 최대값 구하기
# 아이디어 : 인접요소페어 만들기

def arrayPairSum(nums):
    result = 0
    nums.sort()
    for a,b in zip(nums[::2],nums[1::2]):
        result += min(a,b)
    return result

def arrayPairSum2(nums):
    sum = 0; pair = []
    nums.sort()
    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
    return sum

def arrayPairSum3(nums):
    sum = 0;
    nums.sort()
    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n
    return sum


def arrayPairSum4(nums):
    return sum(sorted(nums)[::2])

print(arrayPairSum4([1,4,3,2]))
print(arrayPairSum4([6,2,6,5,1,2]))
