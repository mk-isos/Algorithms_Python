# 문제 분석
# 모든 도로의 거리가 1이라서 가중치가 없는 인접 리스트로 표현
# 도시 300,000 , 도로 최대 크기 1,000,000이므로 BFS탐색사용하면 해결 가능

# 문제 풀이
# 인접 리스트로 도시, 도로 그래프 구현
# BFS탐색 알고리즘으로 탐색하면서 각 최단 거릿값을 방문 리스트에 저장
# 탐색 종료 후 방문 리스트에서 값이 K와 같은 도시 번호를 출력

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())  # 노드의 수, 에지의 수, 목표거리, 시작점
A = [[] for _ in range(N + 1)]
answer = []
visited = [-1] * (N + 1)

def BFS(v):  # BFS 탐색 함수 구현
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if visited[i] == -1:
                visited[i] = visited[now_Node] + 1
                queue.append(i)

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

BFS(X)

for i in range(N + 1):
    if visited[i] == K:
        answer.append(i)
if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)



