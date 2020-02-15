num = input()
num = ''.join(sorted(num, reverse=True))
s = 0
if '0' not in num:        # num = int(input()) 으로 하면 TypeError: argument of type 'int' is not iterable 나므로 num을 str 타입으로 줘야함
    print(-1)             # 30의 배수이므로 0이 들어가야 함.
else:
    for i in num:
        s += int(i)
    if s % 3 != 0:        # 30의 배수이므로 모든 자리 수의 합은 3의 배수여야 함.
        print(-1)
    else:
        print(num)