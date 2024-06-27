# 문제 분석
# 노드의 최대 개수가 1,000이므로 시간복잡도 N^2이하의 알고리즘 모두 사용 가능
# 연결요소는 에지로 연결된 노드의 집합이고
# 한 번의 DFS가 끝날 때까지 탐색한 모든 노드의 집합을 하나의 연결 요소라고 판단

# 문제 풀이
# 그래프를 인접리스트로 저장
# 방문 리스트 초기화
# 방향이 없으니 양쪽 방향으로 에지 모두 저장

# 임의의 시작점에서 DFS 수행
# DFS 실행 횟수가 곧 연결 요소 개수이다

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]

visited = [False] * (n+1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)  # 양방향 에지이므로 양쪽에 에지를 더하기
    A[e].append(s)
count = 0
for i in range(1, n+1):
    if not visited[i]:  # 연결 노드 중 방문하지 않았던 노드만 탐색
        count += 1
        DFS(i)
print(count)

###################################
import sys
sys.setrecursionlimit(10000)

# Python에서 재귀 호출의 최대 깊이(recursion depth)를 설정하는 방법을 보여줍니다.
# sys.setrecursionlimit(10000)은 재귀 호출의 최대 깊이를 10,000으로 설정합니다. 
# 기본적으로 Python은 재귀 호출의 최대 깊이를 1000으로 설정하며, 
# 이 코드를 사용하여 최대 깊이를 더 늘릴 수 있습니다.

