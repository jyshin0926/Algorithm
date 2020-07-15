def solution(people, limit):

    ppl = sorted(people)
    ans = len(ppl)
    minidx, maxidx = 0, len(ppl) - 1
    while ppl and minidx < maxidx:
        if ppl[minidx] + ppl[maxidx] <= limit:
            ans -= 1
            minidx += 1
            maxidx -= 1
        else:
            maxidx -= 1

    return ans