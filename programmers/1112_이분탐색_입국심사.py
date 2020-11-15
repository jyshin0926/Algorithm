# https://wayhome25.github.io/cs/2017/04/15/cs-16/  # binary search 참고

def solution(n,times):
    start,end = 1, min(times)*n
    ans = 0
    while(start <= end):
        mid = (start+end)//2
        tmp = n
        for i in times:
            tmp -= mid//i
            if tmp <= 0:
                ans = mid
                end = mid - 1
                break
        if tmp > 0:
            start = mid + 1
    return ans

print(solution(6,[7,10]))


# 테스트케이스 시간초과 다수
# def solution(n,times):
#     tmp = sorted([x*i for x in times for i in range(1,n)])[:n]
#     return tmp[-1]

# bisect 모듈 참고(binary search)

# 제한사항
# 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
# 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
# 심사관은 1명 이상 100,000명 이하입니다.
# --> 수가 너무 크므로 이분탐색 필요

# n명이 입국심사. 심사관마다 소요시간 다름
# 처음에는 모든 심사대 비어있음. 한 심사대는 한명만 심사 가능. 빨리 끝나는 심사대 있으면 그곳으로 가서 심사 가능
# 모든 사람 심사 소요시간 최소

# 7, 14, 21,
# 10, 20, 30

# 7, 10, 14, 20, 21, 30
# 이분탐색 기준 : 주어진 시간동안 심사 마쳤을 때 심사 마친 사람 수 n명 이상이면 심사시간 줄이고 n명 미만이면 심사 시간 늘려가면서 최솟값 찾는 형태
# 이분탐색 할 값: 한 명의 심사관에게 얼마만큼의 시간 줄지