n, k = map(int, input().split())
sieve = [True] * (n+1)
m = int(n**0.5)
chk = []
for i in range(2,m+1):
    if sieve[i] == True:
        chk.append(i)
        for j in range(2*i, n+1, i):
            sieve[j] = False
            if j not in chk:
                chk.append(j)
chk += [i for i in range(m+1,n+1) if sieve[i] == True]
print(chk[k-1])