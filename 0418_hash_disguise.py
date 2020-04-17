from collections import Counter
from functools import reduce

## code 1
# def solution(clothes):
#
#     answer = 1
#     kind = Counter([x for name, x in clothes])
#     for value in kind:
#         answer *= kind[value] + 1
#     return answer - 1

## code 2
# reduce 함수 사용
# reduce(function, iterable, initializer=None)
# 첫 번째 파라미터 : 함수(람다 또는 정의해놓은 함수 모두 가능)
# 두 번째 파라미터 : 계산을 하고자 하는 리스트
# 세 번째 파라미터 : 초기값(안 줘도 무방)
def solution(clothes):
    kind = Counter([x for name, x in clothes])
    answer = reduce(lambda x, y: (x*y+1), kind.values(), 1) - 1
    return answer


clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))