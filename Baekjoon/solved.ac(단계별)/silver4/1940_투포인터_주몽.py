# n개 재료 중 2개 고유 번호 합쳐서 m 되는 경우의 수 출력

n,m = int(input()), int(input())
ans = 0
materials = list(map(int, input().split()))
for i in range(len(materials)):
    for j in range(i, len(materials)):
        if materials[i] + materials[j] == m:
            ans += 1
print(ans)
