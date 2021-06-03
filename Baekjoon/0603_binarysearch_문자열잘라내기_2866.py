# 참고 : https://www.crocus.co.kr/1071

r,c = map(int, input().split())
table = [str(input()) for i in range(r)]
start, end, mid = 0, r-1, 0
tmp_list = []

while start <= end:
    mid = start + (end-start) // 2
    check = False
    for j in range(c): # 열
        tmp = ''
        for i in range(mid, r):  # 행
            tmp += table[i][j]
        if tmp in tmp_list:
            check = True
            break
        else:
            tmp_list.append(tmp)
    if check:
        end = mid - 1
    else:
        start = mid + 1
    trace = check
    tmp_dict = []
if trace:
    print(mid-1)
else:
    print(mid)


# 중복 나타나면 end = mid-1 정답이어야 하고, 안 나타났으면 start=mid+1
# 이분탐색 후 마지막 mid가 중복었다면 mid-1이 정답
# 마지막 mid가 중복 아니었다면 그 다음 문자부터 중복이니까 mid가 정답