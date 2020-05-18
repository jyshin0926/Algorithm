import re
def solution(operations):
    answer = []
    for i in range(len(operations)):
        if 'I' in operations[i]:
            answer.append(int(''.join(re.findall(r'[-+]?\d+',operations[i]))))
        elif len(answer) != 0:
            if operations[i] == 'D 1':
                answer.remove(max(answer))
            elif operations[i] == 'D -1':
                answer.remove(min(answer))
    if not answer:
        return [0, 0]
    else:
        answer = [max(answer),min(answer)]
    return answer

ope = 	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
opp = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
op = ['I 7','I 5','I -5','D -1']
print(solution(ope))
print(solution(opp))
print(solution(op))


# re.findall(r"[-+]?\d*\.\d+|\d+", "Current Level: -13.2 db or 14.2 or 3")
# ['-13.2', '14.2', '3']