# 초당 최대 처리량: 응답완료 여부 관계없이 1초간 처리하는 요청의 최대 개수
# 효율성 위해 백트래킹으로 시작과 끝만 검사하기

def solution1(lines):
    ans = 0
    tmp = []
    for x in lines:
        S = x.split(' ')[1].split(':')   # 응답완료시간
        T = float(x.split(' ')[2][:-1])  # 처리시간
        start = round(float(S[0])*3600 + float(S[1])*60 + float(S[2]) + 0.001 - T, 3)
        end = round(float(S[0])*3600 + float(S[1])*60 + float(S[2]),3)
        tmp.append([start, end])

    for req in tmp:
        cnt_st = 0; cnt_ed = 0
        st_st = req[0]; st_ed = req[0] + 1
        ed_st = req[1]; ed_ed = req[1] + 1
        for req2 in tmp:
            if req2[1] >= st_st and req2[0] < st_ed:  # 시작 지점 케이스
                cnt_st += 1
            if req2[1] >= ed_st and req2[0] < ed_ed:  # 종료 지점 케이스
                cnt_ed += 1
            ans = max(ans, cnt_st, cnt_ed)
    return ans

# 테스트 1 〉	통과 (0.10ms, 10.2MB)
# 테스트 2 〉	통과 (256.63ms, 10.4MB)
# 테스트 3 〉	통과 (254.31ms, 10.3MB)
# 테스트 4 〉	통과 (0.03ms, 10.2MB)
# 테스트 5 〉	통과 (3.90ms, 10.3MB)
# 테스트 18 〉	통과 (1175.08ms, 10.5MB)
# 테스트 19 〉	통과 (958.44ms, 10.5MB)
# 테스트 20 〉	통과 (958.55ms, 10.4MB)



# 빠른 실행 위해 함수화
def check(time, tmp):
    cnt = 0
    st = time; ed = time+1
    for req in tmp:
        if req[1] >= st and req[0] < ed:   # 종료지점과 시작지점이 특정 로그 시간의 처리 구간 내에 포함되어 있으면
            cnt += 1
    return cnt

def solution(lines):
    ans = 0
    tmp = []
    for x in lines:
        S = x.split(' ')[1].split(':')   # 응답완료시간
        T = float(x.split(' ')[2][:-1])  # 처리시간
        start = round(float(S[0])*3600 + float(S[1])*60 + float(S[2]) + 0.001 - T, 3)
        end = round(float(S[0])*3600 + float(S[1])*60 + float(S[2]),3)
        tmp.append([start, end])

    for req in tmp:
        ans = max(ans, check(req[0], tmp),check(req[1], tmp))
    return ans
# 테스트 1 〉	통과 (0.09ms, 10.2MB)
# 테스트 2 〉	통과 (103.26ms, 10.2MB)
# 테스트 3 〉	통과 (115.94ms, 10.4MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (2.29ms, 10.4MB)
# 테스트 18 〉	통과 (542.03ms, 10.4MB)
# 테스트 19 〉	통과 (413.52ms, 10.5MB)
# 테스트 20 〉	통과 (379.87ms, 10.4MB)


print(solution(['2016-09-15 01:00:04.001 2.0s',
                '2016-09-15 01:00:07.000 2s']))
print(solution(['2016-09-15 01:00:04.002 2.0s',
                '2016-09-15 01:00:07.000 2s']))
print(solution([
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]))


# lines 배열은 N(1 ≦ N ≦ 2,000)개의 로그 문자열
# 각 로그 문자열마다 요청에 대한 응답완료시간 S와 처리시간 T가 공백으로 구분
# 응답완료시간 S는 작년 추석인 2016년 9월 15일만 포함하여 고정 길이 2016-09-15 hh:mm:ss.sss 형식

# 처리시간 T는 0.1s, 0.312s, 2s 와 같이 최대 소수점 셋째 자리까지 기록하며
# 뒤에는 초 단위를 의미하는 s로 끝난다.
# (처리시간은 시작시간과 끝시간을 포함)
# 처리시간은 0.001 ≦ T ≦ 3.000
# lines 배열은 응답완료시간 S를 기준으로 오름차순 정렬

# 동일한 최대 처리량을 갖는 1초 구간은 여러 개 존재할 수 있으므로 이 문제에서는 구간이 아닌 개수만 출력