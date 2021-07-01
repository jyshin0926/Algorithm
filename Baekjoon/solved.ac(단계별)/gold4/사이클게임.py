# 두 플레이어 차례로
# 홀수, 짝수 번갈아서
# 0 ~ n-1 까지 평면 점 n개
# 점 세 개 일직선에 안 놓임
# # 차례마다 두 점 선택해서 선분 긋기. 중복x, 교차 가능
# 처음으로 사이클 완성하면 게임 종료
# 사이클 C는 플레이어가 그린 선분의 부분집합
# 몇 번째 차례에서 사이클 완성되었는지, 아직 게임 진행중인지 판단하는 프로그램 작성하려 함
# n : 점 개수, m: 번째 차례

# union-find
# 유니온파인드 알고리즘 참고 : https://hellominchan.tistory.com/259
# 들어오는 것들 union으로 다 넣어서 부분 집합 통일시키기
# 들어오기 전에 둘의 부모가 같아서 이미 해당 부분집합에 들어가있는 두 숫자라면 무조건 사이클 생긴다!

import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def find(x):  # x 정점의 루트 노드 탐색
    if x == arr[x]: # 이미 그 자신이 루트노드인 경우
        return x
    else:
        arr[x] = find(arr[x])  # arr[x]로 x와 연결된 노드 찾아가기(루트 노드 탐색)
        return arr[x]   # x의 루트노드 갱신

def union(x,y):  # x와 y 집합을 병합
    x = find(x) # x의 루트노드 탐색
    y = find(y) # y의 루트노드 탐색
    if x < y:   # 작은 루트 노드를 기준으로 합침
        arr[y] = x
    else:
        arr[x] = y

n, m = map(int, input().split())
arr = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i+1)
        break
    else:
        union(a,b) # 두 지점을 잇는 선분이 생길 때마다 두 지점을 union
else:  # for-else문 사용
    print(0)


# for ~ else문은 “for문에서 break가 발생하지 않았을 경우”의 동작을 else문에 적어주는 것
# for문 안에서 break가 발생한다면 11~12번째 줄의 else문은 실행되지 않는다.