from collections import deque

# 매번 최댓값을 계산하지 않고 교체하는 방식으로 시간복잡도 줄이기
def maxSlidingWindow(nums,k):
    ans = []; window = deque()
    for i,v in enumerate(nums):
        # 윈도우 큐의 마지막 요소를 인덱스로 하는 nums의 value가 현재 value보다 작을 때
        while window and nums[window[-1]] < v:
            window.pop()  # window에서 맨 마지막 요소(nums의 인덱스) pop

        # 윈도우에 nums 인덱스 저장하기
        window.append(i)

        # 현재 nums의 인덱스가 윈도우 사이즈인 k를 넘어섰을 때 맨 앞 인덱스 빼주기
        # deque maxlen으로는 안 됨(위에서 value로 체크해서 윈도우에 있는 값을 빼주는 때도 있기 때문에 maxlen 자체는 유지될 수 있어서
        # nums의 인덱스로 판단하려면 따로 아래같이 if문 줘야함.
        if i == window[0] + k:
            window.popleft()
        #print(window)

        # 새로운 윈도우 사이즈마다 최댓값 배열에 넣기
        if i >= k-1:
            ans.append(nums[window[0]])
    return ans



# time limit exceeded (O(k*n) : 매번 윈도우 최댓값 계산하니까)
# def maxSlidingWindow(nums, k):
#     tmp = []
#     for i in range(len(nums)-k+1):
#         tmp.append(max(nums[i:i+k]))
#     return tmp

# print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
# print(maxSlidingWindow(nums = [1], k = 1))
# print(maxSlidingWindow(nums = [1,-1], k = 1))
# print(maxSlidingWindow(nums = [9,11], k = 2))
# print(maxSlidingWindow(nums = [4,-2], k = 2))
print(maxSlidingWindow(nums = [7,2,4], k = 2))

