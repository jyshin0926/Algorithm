## idea : Floyd-Warshall

# input
n, m = map(int, input().split())
friend = [[6 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friend[a-1][b-1] = 1    # 직접 친구관계인 경우 1
    friend[b-1][a-1] = 1    # 마찬가지

# floyd-warshall
for k in range(n):      # 경로 노드의 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(n):  # 시작 노드
        for j in range(n):  # 마지막 노드
            if i == j:  # 자기 자신과는 친구가 되지 못한다(자기 자신으로 오는 경로 없음)
                friend[i][j] = 0
            else:    # 경로 갱신
                friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])

# output
bacon = list()
for r in friend:
    bacon.append(sum(r))
print(bacon.index(min(bacon)) + 1)
