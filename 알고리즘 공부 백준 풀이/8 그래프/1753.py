# 문제 분석
# 최단거리 구하는 문제, 다익스트라 알고리즘의 가장 기본 형태

# 문제 풀이
# 인접 리스트에 노드 저장, 거리 리스트 초기화 (출발 0, 나머지는 매우 큰 수)
# 최초 시작점을 우선순위 큐에 삽입
# 다익스트라 알고리즘 수행
# 거리 리스트에서 아직 방문 안 한 노드 중 가장 작은 노드 선택
# 그 노드랑 연결된 노드들의 최단 거릿 값을 업뎃
# (연결 노드 거리 리스트 값 )보다 (선택 노드 거리 리스트 값 + 에지 가중치)가 더 작은 경우 업뎃
# 큐가 빌 때까지 위 과정 반복

import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
K = int(input())
distance = [sys.maxsize] * (V + 1)
visited = [False] * (V + 1)
myList = [[] for _ in range(V + 1)]
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())  # 가중치가 있는 인접 리스트 저장
    myList[u].append((v, w))

q.put((0, K))  # K를 시작점으로 설정
distance[K] = 0
while q.qsize() > 0:
    current = q.get()
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in myList[c_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[c_v] + value:  # 최소 거리로 업데이트
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))
for i in range(1, V + 1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
