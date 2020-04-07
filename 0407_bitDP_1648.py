# 단순 brute-force를 하면 시간이 매우 오래 걸리므로 memoization 필요
# 현재 인덱스인 [i, j] 는 같아도 앞으로 채울 수 있는 칸이 다를 수 있으므로 
# i, j 뿐만 아니라 해당행과 다음행의 칸 정보를 갖고 있는 2진수를 모두 사용해서 메모이제이션 해주어야 함
# 4가지 변수 모두 고려하면 좋겠지만 n =14, m=14 일 때 14*14*2^14*2*14 이므로 메모리 초과 위험하므로
# 이진수 두개 중 하나만 이용
# 이렇게 하려면 아무 인덱스에서 저장하면 안 되고 맨 위 칸에 방문했을 때 메모이제이션 이용해주면 됨

def dp(answer, n, m, i, j, now_state, next_state):  # 아래 -> 오른쪽 우선 순으로 진행
    tmp1, tmp2 = 0,0     # 도미노 1x2 또는 2x1
    if j == m:
        if now_state == 1 << n:     # 열의 개수에 해당하는 n 사이즈의 2진수 이용
            return 1
        else:
            return 0
    if i == n:
        now_state = next_state
        next_state = 1 << n     # n번째 비트 켜기
        return dp(answer, n, m, 0, j+1, now_state, next_state)  # 다음 줄로 이동
    else:
        if next_state == (1 << n) and answer[i][j][now_state] != -1:
            return answer[i][j][now_state]
        if now_state & 1 << i: # 현재 칸이 채워져있다면 다음 칸으로 전진
            tmp1 = dp(answer, n, m, i+1, j, now_state, next_state)
        else:
            tmp1 = dp(answer, n, m, i+1, j, now_state, next_state+(1 << i))  # 1x2 도미노
            if not(now_state & 1 << (i+1)):
                tmp2 = dp(answer, n, m, i+2, j, now_state, next_state)  # 2x1 도미노
    total = (tmp1 + tmp2) % 9901
    if next_state == (1 << n):
        answer[i][j][now_state] = total
    return total


n, m = map(int, input().split(' '))

answer = [[[-1]*(1 << (n+1)) for i in range(m)] for j in range(n)]
now_state = 1 << n
next_state = 1 << n
print(dp(answer, n, m, 0, 0, now_state, next_state))