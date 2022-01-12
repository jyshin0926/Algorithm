n = int(input())
tmp = [list(map(int, input().split())) for _ in range(n)]
ans = [1 for _ in range(n)]
for i, v in enumerate(tmp):
    for j, v2 in enumerate(tmp):
        if i != j and v[0] < v2[0] and v[1] < v2[1]:
            ans[i] += 1
        continue
print(*ans)



# n = int(input())
# tmp = [list(map(int, input().split())) for _ in range(n)]
# ans = [1 for _ in range(n)]
#
# for i, v in enumerate(tmp):
#     for j, v2 in enumerate(tmp):
#         if v[0] < v2[0] and v[1] < v2[1]:
#             ans[i] += 1
#         continue
# print(*ans)

# n명 집단에서 각 사람의 덩치 등수는 자신보다 더 '큰 덩치'의 사람의 수로 정해짐
# 자신보다 더 큰 덩치의 사람이 k명이면 그 사람의 덩치 등수는 k+1
# 같은 덩치 등수를 가진 사람은 여러 명도 가능