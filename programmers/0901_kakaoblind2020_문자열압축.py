def solution(s):
    ans = len(s)
    for sl in range(1,len(s)//2 + 1):
        ret = ""        # 각 분할당 비교할 문자열
        cnt = 1     # 현재까지 중복개수
        prev = s[:sl]   # 이전 문자
        # print('sl: ', s[sl])
        # print('prev: ',prev)
        for i in range(sl, len(s) + 1, sl):    # sl부터 sl 단위로
            if prev == s[i:i+sl]:       # 이전 문자와 지금 잘린 문자열이 같을 때
                cnt += 1            # cnt += 1
            else:            # 이전 문자와 지금 잘린 문자열이 다를 때
                if cnt != 1:    # cnt 가 2 이상일 경우 각 분할 문자열에 cnt 더해서 추가
                    ret = ret + str(cnt) + prev
                else:               # counter가 1일 경우
                    ret = ret + prev
                prev = s[i:i+sl]
                cnt = 1
        ans = min(ans, len(ret))   # 각 분할단위당 가장 짧은 길이를 min, ans를 이용해 비교
    return min(ans,len(s)), ret

#print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))


# 문자열 최대 절편 길이는 문자열 길이의 절반 이하
# 체크해서 다음에도 똑같은 거 있으면 카운팅숫자 + 문자 를 문자열의 부분으로 리턴