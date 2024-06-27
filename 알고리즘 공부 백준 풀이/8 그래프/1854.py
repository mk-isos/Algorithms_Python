# 문제풀이 다시 정리 필요


# 문제 분석
# 시작점, 도착점 주고 목적지까지 k번째 최단경로 구하기
# 노드 수 1,000개, 에지수 2,000,000 시간제약 2초니까 다익스트라 알고리즘으로 접근

# k번째 최단 경로 해결
# 최단경로 리스트 K개의 행을 갖는 2차원 리스트로 변경
# 이러면 최단이랑 최단 ~ K번째 최단 경로까지 가능 할 듯
# 노드를 여러 번 쓰는 경우가 있을테니
# 기존 로직에서 사용한 노드 방문 리스트 체크하고 다음 도착시 해당 노드 사용않기 위해 설정하는 건 안해도 될 듯

# 문제 풀이
# 일단 예제기반 그래프 그리고
# 변수선언하고 다익스트라 준비하듯이 준비
# 기존과 다른 점은 최단 거리 리스트를 1차원이 아니라 K개 행을 갖는 2차원 리스트로 선언

import sys
import heapq
input = sys.stdin.readline
N, M, K = map(int, input().split())
W = [[] for _ in range(N+1)]
distance = [[sys.maxsize] * K for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    W[a].append((b,c))

pq = [(0,1)]
distance[1][0] = 0
while pq:
    cost,node = heapq.heappop(pq)
    for nNode, nCost in W[node]:
        sCost = cost + nCost
        if distance[nNode][K-1] > sCost:
            distance[nNode][K-1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq, [sCost, nNode])

for i in range(1,N+1):
    if distance[i][K-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][K-1])
