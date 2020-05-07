# 선수들의 숫자를 셀 때, 리스트 자료구조를 이용할 경우, 10만명이나 되기 때문에 접근 비용이 매우 큽니다.
# 그래서 Hash 자료 구조를 이용해 마라톤 선수들 숫자를 세야 풀리는 문제입니다.
# collections.Counter(list) 메서드는 리스트를 dictionary 형태로 숫자를 세서 반환

from collections import Counter

def solution(participant, completion):

    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    diff = participant_counter - completion_counter
    return list(diff)[0]

participant = list(input().split())
completion = list(input().split())
print(solution(participant, completion))
