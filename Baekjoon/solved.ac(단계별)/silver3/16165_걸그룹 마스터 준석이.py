from collections import defaultdict

n, m = map(int, input().split())
gg = defaultdict(list)

for i in range(n):
    group = input()
    num = int(input())
    member = []
    for j in range(num):
        member.append(input())
    gg[group] = sorted(member)

ans = []
for i in range(m):
    name = input()
    type = int(input())
    if type == 0:
        ans += gg[name]
    if type == 1:
        for key,val in gg.items():
            if name in val:
                ans.append(key)
print(*ans,sep='\n')

