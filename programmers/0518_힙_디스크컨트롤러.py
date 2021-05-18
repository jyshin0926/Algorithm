def solution(jobs):
    job = sorted(jobs, key=lambda x:x[1])  # 소요 시간 기준으로 sorting
    #print(job)
    cur = 0; ans = 0
    while len(job) > 0:
        for i in range(len(job)):
            if job[i][0] <= cur:
                cur += job[i][1]
                ans += (cur-job[i][0])
                #print(ans)
                job.pop(i)
                break
            elif i == len(job)-1:
                cur += 1
    return ans//len(jobs)

# 풀이2 heapq
import heapq
def solution2(jobs):
    ans, cur, cnt = 0,0,0
    start = -1
    heap = []
    while len(jobs) > cnt:
        for s,t in jobs:
            if start < s <= cur:
                # 힙에 push할 때는 작업의 소요 시간 기준으로 최소힙 만들어져야하므로
                # jobs의 요소를 [소요시간, 요청시점]으로 앞뒤 바꿔서 넣어준다
                heapq.heappush(heap, [t,s])
        if len(heap) > 0:
            tmp = heapq.heappop(heap)
            start = cur
            cur += tmp[0]
            ans += (cur - tmp[1])
            cnt += 1
        else:
            cur += 1
    return ans//len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
))   # 72

print(solution2([[0, 3], [1, 9], [2, 6]]))
print(solution2([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
))


# 하드디스크는 한 번에 하나의 작업만 수행 가눙
# 작업이 요청되는 시점, 작업의 소요시간
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지
# 소수점 이하 수 버리기

# 예시 보면 소요시간 기준으로 sort하는 게 빠름 --> min값
# t = 요청 실제 시작 시점 - 요청 시점 + 소요시간
# jobs 인덱스별 t 구한 후 합해서 len(jobs)로 나눈 결과