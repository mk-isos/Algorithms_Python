# 문제 분석
# 출발 도시와 도착 도시가 주어진다. 일반적인 위상 정렬이 아니다
# 시작점을 출발 도시로 지정하고 위상 정렬 수행하면 경로값을 모두 구할 수 있을 듯
# 근데 1분도 쉬지 않고 달려야하는 도로의 수를 구해야한다.
# 찾아보니 에지 뒤집기라는 아이디어가 있다

# 문제 풀이
# 인접 리스트에 노드 저장, 진입 차수 리스트 값 업데이트
# 역방향 인접리스트도 생성하고 저장하자.
# 시작 도시에서 위상 정렬 수행, 임계 경로 저장
# 다음 도착 도시에서 역방향으로 위상 정렬 수행
# 도시의 임계 경로값 + 도로 시간 == 이전 도시의 임계 경로값 이면 
# 1분도 쉬지않고 달리는 도로가 맞다.

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
A = [[] for _ in range(N+1)]
reverseA = [[] for _ in range(N+1)]
indegree = [0]*(N+1)    # 진입차수 리스트

for i in range(M):
    S, E, V = map(int, input().split())
    A[S].append((E, V))
    reverseA[E].append((S, V))  # 역방향 에지 정보 저장
    indegree[E] += 1    # 진입차수 리스트 저장

startDosi, endDosi = map(int, input().split())

queue = deque()
queue.append(startDosi)
result = [0]*(N+1)
while queue:    #   위상정렬 수행
    now = queue.popleft()
    for next in A[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]],result[now] + next[1])
        if indegree[next[0]] == 0:
            queue.append(next[0])

resultCount = 0
visited = [False]*(N+1)
queue.clear()
queue.append(endDosi)
visited[endDosi] = True

while queue:     #   위상정렬 reverse 수행
    now = queue.popleft()
    for next in reverseA[now]:
        # 1분도 쉬지 않는 도로 체크
        if result[next[0]] + next[1] == result[now]:
            resultCount += 1
            if not visited[next[0]]:
                visited[next[0]] = True
                queue.append(next[0])

print(result[endDosi])
print(resultCount)