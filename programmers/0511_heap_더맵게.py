# code1
def solution(scoville, K):
    import heapq        # heapq는 파이썬의 내장 모듈
    heap = []           # heapq를 사용하기 위한 리스트 생성

    for s in scoville:
        heapq.heappush(heap, s)     # heapq 모듈을 이진트리(binary tree)기반의 최소 힙(min heap)자료구조 제공
    answer = 0
    while len(heap) > 0:
        if heap[0] >= K:    # min heap에서 가장 작은 값은 항상 인덱스 0, 즉 이진 트리의 루트에 위치 # 첫 번째 value가 스코빌지수 이상일 때
            return answer   # 최소값이 scoville 지수 이상이므로 모든 음식이 K 지수 이상
        a = heapq.heappop(heap)  # heappop()은 리스트의 가장 작은 원소를 삭제 후 그 값을 리턴함
        if heap != []:      # a를 꺼낸 후에도 data가 빈 리스트가 아닐 때
            b = heapq.heappop(heap)  # 두 번째로 순한 음식 꺼내기
            heapq.heappush(heap, a + (b*2))     # 스코빌 지수 계산
        answer += 1    # 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수 return
    return -1       # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return

## code2
import heapq
def solution2(scoville, K):
    answer = 0
    heapq.heapify(scoville)     # heapify는 리스트를 min heap으로 변형시켜줌
    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) <= 0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
    return answer




scvlle = [1,2,3,9,10,12]
K = 7
print(solution(scvlle,K))
print(solution2(scvlle,K))