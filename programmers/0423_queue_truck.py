from collections import deque

def solution(bridge_length, weight, truck_weights):

    dq = deque([0]*bridge_length)   # 다리 위 상황 체크
    dq_weight = 0
    truck_weights = deque(truck_weights)
    answer = 0
    while dq:   # 반복문 돌며 다리 다 지난 트럭 나가고 맨 뒤로는 트럭이 계속 들어가게 함(FIFO)
        answer += 1
        out = dq.popleft()      # 다리 통과해서 나가는 값
        dq_weight -= out

        if truck_weights:
            if dq_weight+truck_weights[0] <= weight:
                go_in = truck_weights.popleft()     # 다리에 들어가는 값
                dq.append(go_in)
                dq_weight += go_in
            else:
                dq.append(0)
    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
# bridge_length = 100
# weight = 100
# truck_weights = [10]
print(solution(bridge_length, weight, truck_weights))
