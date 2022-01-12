m, n = map(int, input().split())
x = int(n**0.5)
sieve = [False,False] + [True] * (n-1)
for i in range(2, x+1):
    if sieve[i] == True:
        for j in range(2*i, n+1, i):
            sieve[j] = False

print(*[i for i in range(m,n+1) if sieve[i] == True], sep='\n')