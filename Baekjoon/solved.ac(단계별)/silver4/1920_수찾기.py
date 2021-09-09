n = int(input())
a_n = set(map(int, input().split())) # 헐? 이걸 list에서 set으로 바꾸기만 했는데 시간초과였다가 바로 통과되네..
m = int(input())
m_list = list(map(int, input().split()))

for x in m_list:
    if x in a_n:
        print(1)
    else:
        print(0)



# 다른 코드
n = int(input())
a_n = {i:1 for i in map(int, input().split())}
m = input()
m_list = list(map(int, input().split()))

for x in m_list:
    print(a_n.get(x,0))