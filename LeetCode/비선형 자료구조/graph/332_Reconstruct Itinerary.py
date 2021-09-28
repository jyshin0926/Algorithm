from collections import defaultdict

# sol1. dfs(재귀) + 스택연산
def findItinerary(tickets):
    graph = defaultdict(list)
    # 그래프 뒤집어서 구성
    for x,y in sorted(tickets,reverse=True):
        graph[x].append(y)
    print('graph:',graph)
    result = []
    def dfs(departure):
        while graph[departure]:
            dfs(graph[departure].pop())  # 맨 마지막 값을 불러오는 스택 연산 실행
            # 재귀로 불러낸 것들 쌓여있고
        # graph[departure] 기 앖으면 재귀 마치고 쌓여있는 것 차례로 LIFO로 불러와서 stack에 append
        result.append(departure)
    dfs('JFK')

    # LIFO로 불러와서 쌓여있으므로 첫번째 지점인 JFK가 가장 마지막에 append 되어있는 순서이므로
    # 역순으로 출력해줘야 함
    return result[::-1]



# sol2. 스택을 활용한 일정 그래프 반복
def findItinerary2(tickets):
    graph = defaultdict(list)
    # 그래프 뒤집어서 구성
    for a, b in sorted(tickets,reverse=True):
        graph[a].append(b)
    result, stack = [], ['JFK']
    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        result.append(stack.pop())

    # 다시 뒤집어서 어휘 순 결과로 출력
    return result[::-1]





print(findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
# 알파벳순으로 방문하기