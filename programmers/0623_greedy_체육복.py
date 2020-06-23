def solution(n, lost, reserve):
    ans = n
    set_lost = list(set(lost) - set(reserve))
    set_reserve = list(set(reserve) - set(lost))

    for b in set_reserve:
        if b-1 in set_lost:
            set_lost.remove(b-1)
        elif b-1 in set_lost:
            set_lost.remove(b+1)
    ans -= len(set_lost)
    return ans

print(solution(5,[2,4],[1,3,5]))