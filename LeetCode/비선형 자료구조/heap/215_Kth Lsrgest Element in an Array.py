# heapq의 nlargest 이용
def solution4(nums,k):
    return heapq.nlargest(k,nums)[-1]

# heapq의 heapify 이용
def solution3(nums,k):
    heapq.heapify(nums)
    for _ in range(0,len(nums)-k):
        heapq.heappop(nums)
    return heapq.heappop(nums)


# heapq 모듈 이용
# heapq 모듈은 min heap만 지원하므로 음수로 저장한 다음,
# 가장 낮은 수부터 추출해서 부호를 변환하면 max heap처럼 동작하도록 구현
import heapq
def findKthLargest2(nums,k):
    heap = []
    for n in nums:
        heapq.heappush(heap,-n)
    for _ in range(1,k):
        heapq.heappop(heap)
    return -(heapq.heappop(heap))

# 정렬 이용
def findKthLargest(nums,k):
    return sorted(nums,reverse=True)[k-1]

print(solution4(nums = [3,2,1,5,6,4], k = 2))
print(solution4(nums = [3,2,3,1,2,4,5,5,6], k = 4))
# print(findKthLargest2(nums = [3,2,1,5,6,4], k = 2))
# print(findKthLargest2(nums = [3,2,3,1,2,4,5,5,6], k = 4))