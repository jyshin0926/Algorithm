# heights 배열에 오른쪽 부터 pop()을 한 후
# pop()한 value와 남은 height의 원소들은 거꾸로 비교하여 큰 수가 나오면 해당 인덱스를 저장하는 방식
# 마지막 원소를 pop()한다는 것에서 스택과 연관 (LIFO)
def solution(heights):
    answer = [0]*len(heights)
    while heights:
        right = heights.pop()
        for i in range(len(heights)-1,-1,-1):
            if heights[i] > right:
                answer[len(heights)] = i+1
                break
    return answer

heights = [6, 9, 5, 7, 4]
print(solution(heights))