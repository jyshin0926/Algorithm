n,m = map(int, input().split())
num, *truth = map(int, input().split())
truth_list = [*truth]
cnt = m; total_party = []
for _ in range(m):
    total, *pt = map(int, input().split())
    participants = [*pt]
    total_party += [participants]
    # participants에 truth가 있으면 그 cnt -= 1
    # 그 파티 참석자들을 truth에 추가
    for x in participants:
        if x in truth_list:
            truth_list += [y for y in participants if y not in truth_list]
idx = 0
while idx < len(total_party):
    for party in total_party[idx]:
        if len(total_party) <= 0:
            break
        if party in truth_list:
            total_party.pop(idx)
            #idx = 0
        else:
            idx += 1
print(len(total_party))

# 모든 파티에 참석해야 함
# 진실을 아는 사람이 있는 파티에 이 참석하는 경우가 있는 사람이 있을 땐 제외
