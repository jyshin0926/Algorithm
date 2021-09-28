import sys

# def hanoi(n, start, target, sub):
#     if n > 1:
#         hanoi(n-1, start, sub, target)
#     print(start, target)
#
#     if n > 1:
#         hanoi(n-1, sub, target, start)




def hanoi(n, start, target, sub):
    if n == 0:
        return
    hanoi(n-1, start, sub, target)  # 맨 아래 원반 이외 원반들을 보조막대로 재귀적으로 옮기기
    print(start, target)            # 그 다음, 맨 아래 원반을 목표막대로 이동시킴
    hanoi(n-1, sub, target, start)  # 마지막으로, 보조막대로 옮겼던 원반들을 그 위에 얹는다.


n = int(sys.stdin.readline())
print(2**n - 1)
hanoi(n, 1, 3, 2)