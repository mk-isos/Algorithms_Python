# 문제 분석
# 시작점 및 다른 노드 관련 최단 거리 구하는 문제
# 에지 가중치가 0 또는 음수도 가능
# 그렇기 때문에 벨만포드 사용해야지 생각

# 문제 풀이
# 에지 리스트에 데이터 저장
# 거리 리스트 초기화
# 벨만 포드 알고리즘 수행
# 링크 첨부
# 음수 사이클 존재하면 -1, 아니면 거리 리스트 값 출력

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize]*(N+1)
for i in range(M):  # 에지 데이터 저장
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 벨만포드 수행
distance[1] = 0
for _ in range(N-1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

# 음수 사이클 확인
mCycle = False
for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True

if not mCycle:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)

