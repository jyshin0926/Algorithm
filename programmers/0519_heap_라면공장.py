# heapq는 최소힙 기반의 라이브러리이므로 최대 힙으로 이용하려면 -1을 곱해서 저장한 후, 꺼낼 때 다시 -1을 곱해주어야 함
import heapq
def solution(stock, dates, supplies, k):
    ans = 0
    j = 0
    pq = []
    while stock < k:
        for i in range(j, len(dates)):
            if stock < dates[i]:
                break
            heapq.heappush(pq, -supplies[i])
            j += 1
        stock += heapq.heappop(pq) * -1
        ans += 1
    return ans

stk = 4
d = [4, 10, 15]
spp = [20, 5, 10]
k = 30
print(solution(stk, d, spp, k))