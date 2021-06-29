hex = input()[::-1]; ans = 0
for i in range(len(hex)):
    if hex[i].isdigit() == True:
        ans += int(hex[i]) * (16**i)
    if hex[i].isalpha() == True:
        x = ord(hex[i])-55
        ans += x * (16**i)
print(ans)



