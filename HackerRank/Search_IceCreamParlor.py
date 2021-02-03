def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == m and i != j:
                return i+1, j+1

print(icecreamParlor(4,[1,4,5,3,2]))
print(icecreamParlor(4,[2,2,4,3]))

# t: ice cream parlor에 가는 횟수
# m: 쓸 비용
# cost : 각 i번째 flavor의 cost
# n : 한 번에 제공되는 맛
# 맞는 cost에 해당되는 flavor의 Index+1 리턴(오름순으로 차례대로)
