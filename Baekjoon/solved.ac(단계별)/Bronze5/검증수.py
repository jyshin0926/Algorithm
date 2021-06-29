tmp = list(map(lambda x:x**2, list(map(int, input().split()))))
print(sum(tmp) % 10)
