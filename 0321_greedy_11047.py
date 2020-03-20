n, k = map(int, input().split())
coin = []
cnt = 0
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)         # greedy    # 가장 큰 값부터 넣어주며 필요한 최소 개수 찾기
for i in coin:
    cnt += k//i
    k %= i          # k -= (k//i) * i     # 수를 나눈 후 나머지를 대입
print(cnt)
