n,m  = map(int, input().split())
a,b = map(list,input().split())

alphabet = {'A':3, 'B':2, 'C':1, 'D':2, 'E':4,'F':3, 'G':1, 'H':3,
            'I':1, 'J':1, 'K':3, 'L':1, 'M':3, 'N':2, 'O':1, 'P':2,
            'Q':2, 'R':2, 'S':1, 'T':2, 'U':1, 'V':1, 'W':1, 'X':2,
            'Y':2, 'Z':1}

tmp = []
for i in range(min(n,m)):
    tmp += a.pop(0) + b.pop(0)
tmp += a+b

for i in range(len(tmp)):
    tmp[i] = alphabet[tmp[i]]

while tmp:
    if len(tmp) == 2:
        break
    new_tmp = []
    for x,y in zip(tmp, tmp[1:]):
        if x+y < 10:
            new_tmp.append(x+y)
        elif x+y >= 10:
            new_tmp.append((x+y) % 10)
    tmp = new_tmp


ans = int(''.join([str(x) for x in tmp]))
print(ans,'%',sep='')


