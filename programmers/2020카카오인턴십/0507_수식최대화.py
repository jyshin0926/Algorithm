# eval 함수는 매개변수로 받은 expression(=식)을 문자열로 받아서 실행하는 함수
def solution(expression):
    ans = 0
    priorities = [['*','-','+'],
                  ['*','+','-'],
                  ['+','-','*'],
                  ['+','*','-'],
                  ['-','+','*'],
                  ['-','*','+']]
    for priority in priorities:
        res = int(calc(priority,0,expression))
        ans = max(ans, abs(res))
    return ans

def calc(priority,n,expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority,n+1,e) for e in expression.split('*')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority,n+1,e) for e in expression.split('-')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority,n+1,e) for e in expression.split('+')]))

    return str(res)


if __name__ == '__main__':
    for x in ["100-200*300-500+20","50*6-3*2"]:
        print(solution(x))
#
# print("100-200*300-500+20".split('*'))
# print('*'.join("100-200*300-500+20".split('*')))
# print(eval('*'.join("100-200*300-500+20".split('*'))))