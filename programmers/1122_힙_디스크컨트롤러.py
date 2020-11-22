def solution(job):
    cur = 0   # 현재 시점
    jobs = sorted(job.copy(), key=lambda x:x[1])
    time = 0
    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= cur:
                cur += jobs[i][1]
                time += (cur-jobs[i][0])
                del jobs[i]
                break
            elif i == len(jobs)-1:
                cur += 1
    return time//len(job)

print(solution([[0, 3], [1, 9], [2, 6]]))




# 하드디스크는 한 번에 하나의 작업만 수행 가눙
# 작업이 요청되는 시점, 작업의 소요시간
# 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지
# 소수점 이하 수 버리기

# 예시 보면 소요시간 기준으로 sort하는 게 빠름 --> min값
# t = 요청 실제 시작 시점 - 요청 시점 + 소요시간
# jobs 인덱스별 t 구한 후 합해서 len(jobs)로 나눈 결과