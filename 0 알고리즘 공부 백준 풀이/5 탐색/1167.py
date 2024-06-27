# 문제 분석
# 가장 긴 경로를 찾는 방법 관련 아이디어가 필요하다
# 아이디어
# 임의의 노드에서 가장 긴 경로로 연결돼 있는 노드는 트리의 지름에 해당하는 두 노드 중 하나

# 문제 풀이
# 그래프를 인접 리스트로 저장
# (노드, 가중치)로 표현하고 싶어서 노드를 튜플로 선언

# 임의의 노드에서 BFS를 수행하고 탐색할 때 각 노드의 거리를 리스트에 저장
# 그렇게 하나의 노드로 다 방문하여 거리 리스트를 업데이트
# 위 과정에서 얻은 리스트에서 임의의 노드와 가장 먼 노드 찾기
# 그 노드부터 다시 BFS 수행
# 이제 여기서 얻은 리스트에서 가장 큰 값이 트리의 지름이다.


from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]

for _ in range(N):
    Data = list(map(int, input().split()))
    index = 0
    S = Data[index]
    index += 1
    while True:
        E = Data[index]
        if E == -1:
            break
        V = Data[index + 1]
        A[S].append((E, V))
        index += 2

distance = [0] * (N + 1)
visited = [False] * (N + 1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_Node] + i[1]

BFS(1)
Max = 1
for i in range(2, N + 1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (N + 1)
visited = [False] * (N + 1)
BFS(Max)
distance.sort()
print(distance[N])
