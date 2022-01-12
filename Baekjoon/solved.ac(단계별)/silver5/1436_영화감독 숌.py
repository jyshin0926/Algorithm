title = 666
n = int(input())

while n:
    if '666' in str(title):
        n -= 1
        if n == 0:
            print(title)
    title += 1
