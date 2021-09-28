# 최대한 낮을 때 사서 높을 때 팔기

import sys

def maxProfit2(prices):
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)
    return profit


# time out
def maxProfit(prices):
    profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            profit = max(prices[j]-prices[i], profit)
    return profit



print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))