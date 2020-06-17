def solution(citations):
    citations.sort()
    n = len(citations)
    for i in range(n):      # [0,1,3,5,6]
        if citations[i] >= n-i:
            return n-i
    return 0


def solution2(citations):
    citations.sort(reverse=True)
    # print(citations)    # [6, 5, 3, 1, 0]
    # print(list(enumerate(citations, start=1))) # enumerate(arr,start=number) 로 시작 번호를 정할 수 있다.
    # print(list(map(min, enumerate(citations, start=1))))   # [1, 2, 3, 1, 0] # enumerate 에는 index와 value가 튜플형태로 담기므로 하나의 튜플 에서 index와 value 중 min값을 map으로 구함
    # print(min(enumerate(citations, start=1)))   # (1, 6)
    ans = max(map(min, enumerate(citations, start=1)))

    return ans

citations = [3, 0, 6, 1, 5]
print(solution(citations))
