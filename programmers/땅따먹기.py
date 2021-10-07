# 통과 풀이
def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
    print(land)
    return max(land[-1])

# 틀린 풀이
def solution_(land):
    ans = 0
    i = 0; skip = len(land[0])+1  # 이전 행 인덱스를 skip에 저장
    while i < len(land):
        # 일단 행의 최대값 찾기
        val = max(land[i])
        # 행의 최대값 인덱스 저장
        j = land[i].index(val)
        # 이전 행 인덱스(skip)과 현재 행 인덱스가 다르면 넘어감
        if j != skip:
            pass
        # 이전 행 최대값 인덱스와 현재 행 최대값 인덱스가 같다면
        # 현재 행 최대값을 0으로 변경하고 새로운 최대값 구하기
        # 여기가 오류로구먼(이전 행 최대값을 더한 게 현재 행 최대값을 더했을 때보다 꼭 크리라는 보장이 없음!)
        else:
            land[i][j] = 0
            val = max(land[i])
            j = land[i].index(val)
        ans += val
        skip = j
        i += 1
    return ans

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))