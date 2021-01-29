def minimumNumber(n, password):
    letters = ["0123456789", "abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ","!@#$%^&*()-+"]
    ans = 0
    tmp = [0,0,0,0]
    for x in password:
        for i in range(4):
            if x in letters[i]:
                tmp[i] += 1
    if 0 in tmp:
        ans += tmp.count(0); n += tmp.count(0)
    else:
        pass
    while n < 6:
        n += 1; ans += 1
    return ans

print(minimumNumber(11, '#HackerRank'))
print(minimumNumber(3, 'Ab1'))