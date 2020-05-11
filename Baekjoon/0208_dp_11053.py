n = int(input())
seq = list(map(int, input().split()))
asc = [0] * n       # 증가하는 수열 체크 위해 seq 길이만큼의 리스트 생성
for i in range(len(seq)):
    for j in range(i):  # 0 ~ i-1
        if seq[i] > seq[j] and asc[i] < asc[j]:
            asc[i] = asc[j]
    asc[i] += 1
print(max(asc))
print(asc)
