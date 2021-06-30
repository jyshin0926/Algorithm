n = int(input())
switch = list(map(int, input().split()))
on_off = {0:1, 1:0}
ppl = int(input())
for _ in range(ppl):
    sex, num = map(int, input().split())
    if sex == 1:    # 남자일 때
        for i in range(len(switch)):
            if (i+1) % num == 0:
                switch[i] = on_off[switch[i]]
    else:   # 여자일 때
        i, j = num-2, num
        switch[num-1] = on_off[switch[num-1]] # 일단 주어진 값 변경해주고
        while i >= 0 and j < n:     # 주변 대칭값 탐색
            if switch[i] == switch[j]:
                switch[i] = switch[j] = on_off[switch[i]]
            else:
                break
            i -= 1
            j += 1
for i in range(0, n, 20): # for문 증가치와 함께 print문에서도 인덱스범위를 동일하게 20개까지 끊어주어 출력 범위가 안 겹치게 함
    print(*switch[i:i+20])


# 남: 스위치 번호가 자신이 받은 수의 배수이면 스위치 상태 바꾸기
# 여: 좌우 대칭으로 구간 삼아서 스위치 상태 바꾸기
# 스위치 상태(light 배열)은 한 줄에 20개씩 출력해야 함

# tmp = [i for i in range(8)]
# for i in range(0,8,2):
#     print(tmp[i:i+2])
#
# for i in range(0,8):
#     print('2번째:',tmp[i:i+2])