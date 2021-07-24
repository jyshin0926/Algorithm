import re
def solution(s):
    # in 사용할 때 list, tuple 시간복잡도는 Average : O(n)
    # in 사용할 때 set, dict 시간복잡도는 Average : O(1), Worst : O(n)
    # set, dict은 내부적으로 hash를 통해 저장하므로 접근하는 시간은 O(1)
    # 그러나 해쉬의 충돌이 많아 성능이 떨어지는 경우 O(n)이 걸릴 수 있음
    ans = {}  # not in 사용할 때 시간복잡도를 낮추기 위해 dict로 설정
    s = s[2:-1].split(',{')
    s.sort(key=len)
    for val in s:
        match_text = re.findall("\d+",val)
        for x in match_text:
            if int(x) not in ans:
                ans[int(x)] = 1
    return list(ans.keys())

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
