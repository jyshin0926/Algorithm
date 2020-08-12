def solution(triangle):
    for row in range(1, len(triangle)):
        # row별 index값 별로 비교
        for idx in range(row+1):
            # 가장 왼쪽 값인 경우
            if idx == 0:
                triangle[row][idx] += triangle[row-1][idx]
            # 가장 오른쪽 값인 경우
            elif idx == row:
                triangle[row][idx] += triangle[row-1][idx-1]
            else:
                triangle[row][idx] += max(triangle[row-1][idx-1], triangle[row-1][idx])
    answer = max(triangle[-1])

    # 가장 마지막 row의 최댓값 return
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))