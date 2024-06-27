# 문제 분석
# N의 최대 범위 2,000이므로 알고리즘의 시간 복잡도 좀 여유롭다.
# 주어진 모든 노드에 DFS를 수행하기
# 깊이가 5 이상이면 1 출력, 아니면 0 출력
# DFS의 시간 복잡도는 O(V+E)이므로 최대 4,000
# 모든 노드를 진행해도 4,000 * 2,000 즉 8,000,000이다
# DFS 사용 가능

# 문제 풀이
# 그래프 데이터를 인접 리스트로 저장
# 모든 노드에서 DFS를 수행
# 수행할 때 재귀 호출 마다 깊이를 더하자
# 깊이가 5되면 1을 출력
# 프로그램 종료
# 모든 노드를 돌아도 1이 출력이 안되면 0 출력


import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
N, M = map(int, input().split())
arrive = False

A = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)


def DFS(now, depth):
    global arrive
    
    if depth == 5 or arrive == True:    # 깊이가 5가 되면 종료
        arrive = True
        return
    
    visited[now] = True
    
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth + 1)   # 재귀 호출 마다 깊이 증가
    visited[now] = False


for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)  # 양방향 에지이므로 양쪽에 에지를 더하기
    A[e].append(s)

for i in range(N):
    DFS(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)

