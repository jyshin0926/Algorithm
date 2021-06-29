l,p = map(int, input().split())
tmp = ' '.join(list(map(lambda x: str(x-l*p),list(map(int, input().split())))))
print(tmp)
