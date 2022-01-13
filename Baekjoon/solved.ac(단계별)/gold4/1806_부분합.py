import sys
n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right, val = 0,0,0
ans = sys.maxsize

while True:
    if val < s:
        if right == n: break
        val += arr[right]
        right += 1
    else:
        ans = min(ans, right-left)
        val -= arr[left]
        left += 1
if ans == sys.maxsize:
    print(0)
else:
    print(ans)
