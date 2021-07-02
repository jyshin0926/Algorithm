# brute force
def solution(prices):
    ans = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i, len(prices)-1):
            if prices[j] >= prices[i]:
                cnt += 1
            else:
                break
        ans.append(cnt)
    return ans

# 효율성
# 테스트 1 〉	통과 (130.46ms, 18.8MB)
# 테스트 2 〉	통과 (95.01ms, 17.6MB)
# 테스트 3 〉	통과 (151.92ms, 19.6MB)
# 테스트 4 〉	통과 (110.17ms, 18.3MB)
# 테스트 5 〉	통과 (73.85ms, 17.1MB)

# stack  # LIFO
def solution2(prices):
    ans = [0]*len(prices)
    stack = []
    for idx, val in enumerate(prices):
        while stack and val < prices[stack[-1]]:  # 다음값이 떨어졌다면
            j = stack.pop()  # 스택에서 해당 값(prices의 인덱스) pop
            ans[j] = idx - j
        stack.append(idx) # 스택 비어있거나 주가 안떨어졌으면 스택에 쌓기

    # 스택에 남아있는 것들은 끝까지 주가 안 떨어진 것들. 다 비워주자
    while stack:
        j = stack.pop()
        ans[j] = (len(prices)-1)-j
    return ans

# 효율성
# 테스트 1 〉	통과 (22.89ms, 18.8MB)
# 테스트 2 〉	통과 (17.05ms, 17.5MB)
# 테스트 3 〉	통과 (25.87ms, 19.4MB)
# 테스트 4 〉	통과 (20.55ms, 18.3MB)
# 테스트 5 〉	통과 (14.35ms, 16.9MB)

print(solution2([1, 2, 3, 2, 3]))
