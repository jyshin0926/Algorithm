def check(result):
    for x, y, kind in result:
        if kind == 0 :  # 기둥인 경우
            # 바닥 위에 있어야 함 / 보의 한쪽 끝 부분 위에 있어야 함 / 다른 기둥 위에 있어야 함
            if y == 0 or (x-1, y, 1) in result or (x, y, 1) in result or (x, y-1, 0) in result:
                continue
            else:
                return False
        elif kind == 1: # 보인 경우
            # 한쪽 끝 부분이 기둥 위에 있어야 함 / 양쪽 끝 부분이 다른 보와 동시에 연결되어야 함
            if (x, y-1, 0) in result or (x+1, y-1, 0) in result or ((x-1,y,1) in result and (x+1, y, 1) in result):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    result = set()
    for a in build_frame:
        x, y, what, how = a
        if how == 1:        # 설치
            result.add((x,y,what))
            # is_true = check(result)
            # if is_true:
            #     continue
            # else:
            #     result.remove((x,y,what))
            if check(result) is False:          # 이렇게 하면 코드는 간결해지지만 위의 코드처럼 조건을 나눠주면 수행속도가 더 빨라진다.
                result.remove((x,y,what))
        elif how == 0:      # 삭제
            if (x,y,what) in result:
                result.remove((x,y,what))
                is_true = check(result)
                # if is_true:
                #     continue
                # else:
                #     result.add((x,y,what))
                if check(result) is False:
                    result.add((x,y,what))
    result = [list(i) for i in result]      # 리스트화
    return sorted(result)


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))