def solution(number, k):
    tmp = []
    number = list(number)

    for x in number:
        while tmp and tmp[-1] < x and k > 0:
            tmp.pop()
            k -= 1
        tmp.append(x)

    if k > 0:
        tmp = tmp[:-k]

    ans = ''.join(tmp)
    return ans


print(solution('10000', 2))
print(solution('1231234', 3))
print(solution('4177252841', 7))