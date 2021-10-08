def switch(scores):
    # map, zip으로 행열 바꾸기
    # zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
    # 여기서 사용한 *iterable은 반복 가능(iterable)한 자료형 여러 개를 입력할 수 있다는 의미
    score1 = list(map(list, zip(*scores)))
    print('score1:',score1)

    # list comprehension으로 바꾸기
    score2 = [ [i[j] for i in scores] for j in range(len(scores)) ]
    print('score2:',score2)


def solution2(scores):
    ans = ''
    for i, x in enumerate(zip(*scores)):
        avg = (sum(x) - x[i]) / (len(x)-1) if x[i] in (min(x),max(x)) and x.count(x) == 1 else sum(x) / len(x)
        ans += '%s' % (
            'A' if 90 <= avg else
            'B' if 80 <= avg else
            'C' if 70 <= avg else
            'D' if 50 <= avg else
            'F'
        )
    return ans


from collections import defaultdict
def solution(scores):
    ret = ''
    dic = defaultdict(list)
    for i, x in enumerate(scores):
        for j, y in enumerate(x):
            dic[j].append(y)

    for k, v in dic.items():
        max_val = max(v)
        min_val = min(v)
        s = 0;
        l = 0
        print(max_val, min_val)
        for i, x in enumerate(v):
            if k == i and x in [max_val, min_val] and v.count(x) == 1:
                pass
            else:
                s += x
                l += 1
        avg = s / l
        ret += '%s' % (
            'A' if 90 <= avg else
            'B' if 80 <= avg else
            'C' if 70 <= avg else
            'D' if 50 <= avg else
            'F'
        )
    return ret

# 한 행에 있는 것들을 sum하는 게 아니라 각 행의 똑같은 열에 있는 것들을 sum
# 평균 학점 구해서 문자열로 리턴하기
# 본인에게 부여한 점수가 유일한 최고점/최저점이면 그 점수 제외하고 평균 구하기
# scores는 n*n 행렬

# 각 행의 요소들 중 가장 최고, 최저값 파악해두고
# 그 요소가 i==j 인지 체크
# 해당되면 그 요소 제외하고 평균내기


print(solution2([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]	))
# print(solution([[50,90],[50,87]]))
# print(solution([[70,49,90],[68,50,38],[73,31,100]]))


# 6시 32분 시작 -> 7시 25분 통과
# 어떤 점수들을 평가했는지, 또 어떤 점수들로 평균내는지를 잘 파악하지 않은 채 시작해서 오래 걸린 문제
# 프로그래머스 환경에서만 하려니까 확실히 힘들다.
# 한 행에 해당하는 요소들이 아닌, 각 행별 같은 열의 요소들을 대상으로 해야하는 것을 파악하는 데에도 느렸지만, 파악한 후에는 딕셔너리를 사용하는 것을 빨리 떠올렸음
# 이거 다른 방법도 있나 찾아보기
# 노트에 정리하니까 훨씬 빨리 파악 가능하다.