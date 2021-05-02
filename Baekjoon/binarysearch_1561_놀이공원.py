n, m = map(int, input().split())
time_list = list(map(int, input().split()))

# 이분 탐색
left, right = 0, max(time_list)*n - 1
while left <= right:
    mid = left + (right-left) // 2
    cnt = m
    for time in time_list:
        cnt += mid // time
    if cnt >= n:
        t = mid   # 구한 시간
        right = mid - 1
    else:
        left = mid + 1

# 구한 시간 - 1분까지 탑승한 아이들 카운트
cnt = m
for time in time_list:
    cnt += (t - 1) // time

# 구한 시간 t에 탑승한 아이 카운트
for idx,time in enumerate(time_list):
    if t % time == 0:  # t 시간에 탑승한 아이
        cnt += 1
    if cnt == n:
        print(idx + 1)
        break


# 24 5
# 1 2 2 4 4
# 정답 4

# 놀이기구가 모두 비어 있는 상태에서 첫 번째 아이가 놀이기구에 탑승한다고 할 때, 줄의 마지막 아이가 타게 되는 놀이기구의 번호를 구하는 프로그램을 작성하시오.


