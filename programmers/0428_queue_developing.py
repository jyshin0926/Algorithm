# 이 문제는 들어온 순서대로 나가야 하기 때문에 큐로 플이
# progresses, speeds 를 모두 큐로 가정하고 풀이

def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0:
            answer.append(cnt)  # 배포 개수 answer에 넣어주기
    return answer

progresses = [93,30,55]
speeds = [1,30,5]
print(solution(progresses, speeds))
