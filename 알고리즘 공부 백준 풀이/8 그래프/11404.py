# 문제 분석
# 모든 도시에 쌍과 관련된 최솟값을 찾아야함
# 모든 노드와 관련된 최소 경로 구하려면 "플로이드-워셜 알고리즘"
# 도시 최대 수가 100개 O(N^3)이라서 가능

# 문제 풀이
# 버스 비용 정보를 인접 행렬에 저장
# 인접 행렬 초기화
# 플로이드-워셜 알고리즘 수행
# Math.min(distance[S][E], distance[S][K] + distnace[K][E])
# 이 점화식 3중 for문으로 모든 중간 경로를 탐색

# 알고리즘 수행 후 변경된 인접 행렬을 출력

import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]
for i in range(1, N+1): # 인접 행렬 초기화
    distance[i][i] = 0

for i in range(M):
    s, e, v = map(int, input().split())
    if distance[s][e] > v:
        distance[s][e] = v

# 플로이드 워셜 수행
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()

