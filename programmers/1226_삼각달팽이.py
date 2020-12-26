# 조건문이 중요한 문제
# 경로에 따라 조건 나누기

def solution(n):
    ans = [[0]*x for x in range(1, n+1)]
    maxVal = n*(n+1)//2  # 변수 저장. 시간 단축
    num, x, y, way = 1,0,0,'down'
    while True:
        if num > maxVal: # break 문으로 시간 단축
            break
        ans[x][y] = num
        if way == 'down':
            x += 1
            if x == n or ans[x][y] != 0:  # or 조건 우선 순위 주의. x == n 이 뒤로 가면 out of range 뜸
                way = 'right'; x -= 1; y += 1   # 경로 변경

        elif way == 'right':
            y += 1
            if y == n or ans[x][y] != 0:
                way = 'up'; x -= 1; y -= 2  # 경로 변경

        elif way == 'up':
            x -= 1; y -= 1
            if ans[x][y] != 0:
                way = 'down'; x += 2; y += 1; n -= 1  # 경로 변경 및 범위 변경
        num += 1

    return [val for row in ans for val in row] # sum 보다 시간 단축됨
    #return sum(ans,[])

print(solution(4))
print(solution(5))
print(solution(6))
print(solution(10))

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (1.65ms, 10.8MB)
# 테스트 5 〉	통과 (1.45ms, 10.9MB)
# 테스트 6 〉	통과 (1.53ms, 10.9MB)
# 테스트 7 〉	통과 (126.82ms, 58.3MB)
# 테스트 8 〉	통과 (144.48ms, 58.3MB)
# 테스트 9 〉	통과 (128.11ms, 60.2MB)


