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


print(solution([1, 2, 3, 2, 3]))

# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지

# 효율성  테스트
# 테스트 1 〉	통과 (130.46ms, 18.8MB)
# 테스트 2 〉	통과 (95.01ms, 17.6MB)
# 테스트 3 〉	통과 (151.92ms, 19.6MB)
# 테스트 4 〉	통과 (110.17ms, 18.3MB)
# 테스트 5 〉	통과 (73.85ms, 17.1MB)