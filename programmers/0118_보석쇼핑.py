# gems 배열 크기는 최대 100000이므로 O(n^2)으로 풀면 시간 초과
# 투 포인터 알고리즘 활용하여 O(n)으로 탐색해야 함
from collections import Counter

def solution(gems):
    ans = []
    kind = len(set(gems))
    tmp = Counter(ans)
    start = 0; end = 0
    tmp[gems[start]] = 1

    while start < len(gems):
        if len(tmp) == kind:  # 모든 보석 채워진 경우 start 인덱스 옮기며 구간 축소 가능한 지 탐색
            ans.append([start+1, end+1])
            tmp[gems[start]] -= 1      # 옮기기 전에 빈도수 감소시켜주기
            if tmp[gems[start]] == 0:  # 0이 될 경우 해당 보석 완전히 제거
                del tmp[gems[start]]
            start += 1
        else:  # 아직 모든 보석 안 채워진 경우 end 인덱스 옮기며 끝까지 탐색
            end += 1
            if end == len(gems):
                break
            else:
                tmp[gems[end]] += 1
    idx = [x[1] - x[0] for x in ans]
    return ans[idx.index(min(idx))]



print(solution(["A","A","B"]))      # [2,3] 나와야함
print(solution(["DIA","EM","EM","RUB","DIA"]))      # [3,5] 나와야함
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))  # [3,7]
print(solution(["AA", "AB", "AC", "AA", "AC"])) # [1,3]
print(solution(["XYZ", "XYZ", "XYZ"]))  # [1,1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))  # [1,5]
