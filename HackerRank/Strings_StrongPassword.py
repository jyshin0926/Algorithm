def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    ans = 0
    tmp = [0,0,0,0]
    for x in password:
        if x in numbers:
            tmp[0] += 1
        if x in lower_case:
            tmp[1] += 1
        if x in upper_case:
            tmp[2] += 1
        if x in special_characters:
            tmp[3] += 1
    if 0 in tmp:
        ans += tmp.count(0); n += tmp.count(0)
    else:
        pass
    while n < 6:
        n += 1; ans += 1
    return ans

print(minimumNumber(11, '#HackerRank'))
print(minimumNumber(3, 'Ab1'))