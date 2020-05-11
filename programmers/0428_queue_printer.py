# 프린터니까 중요도 max인 프린트물부터 주어진 location까지 순회해야 함
# FIFO (queue)

# func1
def solution(priorities, location):
    answer = 0
    while priorities:
        # 첫번째 문서가 중요도가 가장 높은 경우
        if max(priorities) == priorities[0]:
            answer += 1
            priorities.pop(0)
            if location == 0:
                return answer
            else:
                location -= 1
        # 첫번째 문서가 중요도가 가장 높지 않은 경우
        else:
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities)-1    # 옮긴 문서의 위치 조정
            else:
                location -= 1   # 위치 조정
    return answer


# func2
def solution2(priorities, location):
    answer = 0
    while True:
        printer = max(priorities)
        temp = priorities.pop(0)
        if printer == temp:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(temp)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer

