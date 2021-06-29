n, score, p = map(int, input().split())
if n > 0:
    score_list = list(map(int, input().split()))
    ans = 0
    # 추가 시 p 길이를 넘을 때면 min(score_list) 또는 score_list[-1]이랑 비교해서 낮으면 -1 출력
    if len(score_list) == p and score <= min(score_list):
        print(-1)
    else:
        if score in score_list:
            tmp = score_list.index(score)
            ans = tmp+1
            cnt = 0
            for x in score_list[tmp:]:
                if x == score:
                    cnt += 1
                else:
                    break
        elif score not in score_list:
            new_score_list = sorted(score_list + [score], reverse=True)
            ans = new_score_list.index(score) + 1
        print(ans)
else:
    print(1)
