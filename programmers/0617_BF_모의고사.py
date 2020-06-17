def solution(answers):
    ans = []
    cnt = [0,0,0]
    supo1 = []
    supo2 = []
    supo3 = []
    tmp1 = [i for i in range(1, 6, 1)]  # [1,2,3,4,5]   # 0~4
    tmp2 = [2,1,2,3,2,4,2,5]    # 0~7
    tmp3 = [3,3,1,1,2,2,4,4,5,5]    # 0 ~ 9
    for i in range(len(answers)):
        supo1.append(tmp1[i % 5])
        supo2.append(tmp2[i % 8])
        supo3.append(tmp3[i % 10])
        if supo1[i] == answers[i]:
            cnt[0] += 1
        if supo2[i] == answers[i]:
            cnt[1] += 1
        if supo3[i] == answers[i]:
            cnt[2] += 1

    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            ans.append(i+1)
    return ans


def solution2(answers):
    tmp1 = [1,2,3,4,5]
    tmp2 = [2,1,2,3,2,4,2,5]
    tmp3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    ans = []
    for i, answer in enumerate(answers):
        if answer == tmp1[i % len(tmp1)]:
            score[0] += 1
        if answer == tmp2[i % len(tmp2)]:
            score[1] += 1
        if answer == tmp3[i % len(tmp3)]:
            score[2] += 1

    for i, s in enumerate(score):
        if s == max(score):
            ans.append(i+1)
    return ans


answers1 = [1,2,3,4,5]
answers2 = [1,3,2,4,2]
answers = [1,2,3,4,5,1,2,3,4]
print(solution2(answers))
print(solution(answers1))
print(solution2(answers1))
print(solution(answers2))
print(solution2(answers2))