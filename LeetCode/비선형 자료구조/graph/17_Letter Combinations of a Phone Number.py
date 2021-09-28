# dfs로 구하기
def letterCombinations2(digits):
    def dfs(idx, path):
        # 끝까지 탐색하고 나면 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return

        # 입력값 자릿수 단위 반복
        for i in range(idx, len(digits)):
            # 숫자에 해당하는 모든 문자열 반복
            for j in dic[digits[i]]:
                dfs(i+1, path+j)

    if not digits:
        return []

    dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs',
       '8':'tuv','9':'wxyz'}

    result = []
    dfs(idx=0, path='')
    return result


# product로 구하기
from itertools import product
def letterCombinations(digits):
    digits = list(digits)
    digit_dict = {'2': ['a','b','c'],
                  '3': ['d','e','f'],
                  '4': ['g','h','i'],
                  '5': ['j','k','l'],
                  '6': ['m','n','o'],
                  '7': ['p','q','r','s'],
                  '8': ['t','u','v'],
                  '9': ['w','x','y','z']}
    if len(digits) == 0:
        return []
    tmp= []
    for x in digits:
        tmp.append(digit_dict[x])
   # ans = [''.join(x) for x in product(*tmp)]
    ans = list(map(list, product(*tmp)))
    return ans

print(letterCombinations('23'))
print(letterCombinations(''))
print(letterCombinations('2'))

# 폰 번호 눌렀을 때 나올 수 있는 문자열 조합 리턴
# 숫자는 2-9 범위
# 숫자에 대한 알파벳을  다 붙여? 그리고 그 다음 숫자에 대한 알파벳은 어떻게?