# 재귀

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

def pattern(n):
    # n = 3^1일 때까지 재귀돌리고 배열 리턴시키기
    if n == 3:
        arr[0][:] = arr[2][:] = [1]*3
        arr[1][:] = [1,0,1]
        return

    div3 = n // 3
    pattern(div3)  # n을 3으로 나눈 값으로 재귀돌리기
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # 가운데는 비우기 위해 패스
                continue
            else:
                for k in range(div3):
                   # print('arr[k]:',arr[k])
                    arr[div3*i+k][div3*j:div3*(j+1)] = arr[k][:div3]   # 슬라이싱 때문에 오래 걸리는 듯

# n = 9 , div3
# k -> 0~8
pattern(n)  # 재귀함수 초기값 n 넣고 돌리기
for i in arr:
    for j in i:
        if j:
            print('*',end='')
        else:
            print(' ',end='')
    print()

# 3^1일 때 가운데 비우고 3^0 = 1개 씩의 별 찍힘
# 3^i 일 때 가운데 비우고 3^(i-1)개 씩의 별 찍힘


