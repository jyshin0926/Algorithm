import sys
import bisect
# def minimumLoss(price):
#     min_loss = sys.maxsize
#     for i in range(len(price)):
#         for j in range(i+1, len(price)):
#             if price[i] > price[j]:
#                 min_loss = min(min_loss, price[i]-price[j])
#     return min_loss

def minimumLoss(price):
    ans = float('inf'); stack = [price[0]]
    for num in price[1:]:
        if num < stack[0]:
            ans = min(ans, stack[0]-num)
            stack.insert(0,num)
        else:
            idx = bisect.bisect(stack, num)
            if idx < len(stack):
                ans = min(ans, stack[idx]-num)
            stack.insert(idx, num)
    return ans

print(minimumLoss([20,15,8,2,12]))
print(minimumLoss([5,10,3]))
print(minimumLoss([20,7,8,2,5]))