def solution(prices):
    ans = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i, len(prices)-1):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                break
        ans.append(cnt)
    return ans


prices = [1,2,3,2,3]  # 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지 return
print(solution(prices))



# if prices[i] <= prices[j]: cnt += 1