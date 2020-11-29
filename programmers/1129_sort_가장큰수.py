# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수
# 문자열로 바꿔서 리턴
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.

# 테스트케이스 통과 / permutation 시간초과
from itertools import permutations
def solution1(numbers):
    num = [str(x) for x in numbers]
    tmp = [int(x) for x in list(map(''.join, permutations(num)))]
    return str(max(tmp))

# 통과
def solution(numbers):
    num = [str(x) for x in numbers]  # 문자열 비교를 위해 아스키코드로 정렬되는 sort 사용
    num.sort(key=lambda x: x*3, reverse=True)  # 원소들이 1000 이하이므로 최소 3자리까지 비교 가능하도록 하기
    return str(int(''.join(num)))  # '000' 처리

# 테스트 1 〉	통과 (794.34ms, 23.3MB)
# 테스트 2 〉	통과 (247.49ms, 17.2MB)
# 테스트 3 〉	통과 (1349.96ms, 27.4MB)

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))

print(ord('0'))
print(ord('2'))
print(ord('3'))

print(sorted(['333','30','3','1000'],key=lambda x:x*2, reverse=True))
print(sorted(['30'*3,'3'*3],reverse=True))
print(sorted(['30','3'],reverse=True))
print(sorted(['30'*2,'3'*2],reverse=True))
print(sorted(['adad','abcabc'],reverse=True))
