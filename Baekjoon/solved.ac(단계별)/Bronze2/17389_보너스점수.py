n = int(input())
s = input()

score = 0; bonus = 0
for i, v in enumerate(s):
    if v == 'O':
        score += (i+1)+bonus
        bonus += 1
    else:
        bonus = 0
print(score)