def solution(n,times):
    ans = 0
    left, right = 0, min(times)*n - 1
    while left <= right:
        mid = left + (right-left)//2
        tmp = n
        for i in times:
            tmp -= mid//i
            if tmp <= 0:
                ans = mid
                right = mid - 1
                break
        if tmp > 0:
            left = mid+1
    return ans

print(solution(6, [7,10]))

# 7, 10, 14, 20, 21, 30
# 이분탐색 기준 : 주어진 시간동안 심사 마쳤을 때 심사 마친 사람 수 n명 이상이면 심사시간 줄이고 n명 미만이면 심사 시간 늘려가면서 최솟값 찾는 형태
# 이분탐색 할 값: 한 명의 심사관에게 얼마만큼의 시간 줄지