n = int(input())
b_seq = list(map(int, input().split()))
a_seq = [b_seq[0]]
for i in range(1,len(b_seq)):
    x = (b_seq[i] * (i+1)) - sum(a_seq)
    a_seq.append(x)

print(*a_seq)