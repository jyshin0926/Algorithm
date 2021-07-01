# linked_list, bfs, 집합 자료형
# https://hangjo-o.tistory.com/18 참고
from collections import deque

n,m = map(int, input().split())
truth = deque(map(int, input().split()[1:]))  # 필요없는 값들은 받지 않기 for 클린코드
# linked[i]에 있는 사람들은 파티에 i와 같이 있었던 사람들
linked = {i: [] for i in range(1, n+1)}
parties = []
visit = {i: True if i in truth else False for i in range(1,n+1)} # bfs에 사용

for _ in range(m):
    participants = list(map(int, input().split()))[1:]
    parties += [participants]
    for i in participants:
        linked[i] += [y for y in participants if y not in linked[i]]

bfs = truth.copy()
while bfs:
    cur_man = bfs.popleft()
    for i in linked[cur_man]:
        if not visit[i]:
            bfs.append(i)
            visit[i] = True
            truth.append(i)
cnt = 0
for party in parties:
    if not set(party) & set(truth):
        cnt += 1
print(cnt)


# 통과x - 다시 풀어보기
# n,m = map(int, input().split())
# num, *truth = map(int, input().split())
# truth_list = [*truth]
# cnt = m; total_party = []
# for _ in range(m):
#     total, *pt = map(int, input().split())
#     participants = [*pt]
#     total_party += [participants]
#     # participants에 truth가 있으면 그 cnt -= 1
#     # 그 파티 참석자들을 truth에 추가
#     for x in participants:
#         if x in truth_list:
#             truth_list += [y for y in participants if y not in truth_list]
# idx = 0
# while idx < len(total_party):
#     for party in total_party[idx]:
#         if len(total_party) <= 0:
#             break
#         if party in truth_list:
#             total_party.pop(idx)
#             #idx = 0
#         else:
#             idx += 1
# print(len(total_party))

# 모든 파티에 참석해야 함
# 진실을 아는 사람이 있는 파티에 이 참석하는 경우가 있는 사람이 있을 땐 제외
