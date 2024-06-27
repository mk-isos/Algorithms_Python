# 문제분석
# 시작, 도착점주고 목적지까지 최소 비용구하기
# 버스 비용이 음수가 아니라서 다익스타라 쓰면 딱일듯
# 도시 최대 수 1,000개라서 인접 행렬 방식으로 그래프 표현가능하지만
# 시간 복잡도와 공간 복잡도 측면에서 인접리스트 사용할 거

# 문제 풀이
# 일단 예제 기반 그래프 그리기 대충
# 도시 개수의 크기 만큼 인접 리스트 설정
# 데이터는 (목표 노드, 가중치) 형태로 설정
# 다음 버스 개수의 크기만큼 반복문 돌리기 인접리스트에 저장
# 다익스트라 수행

import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
M = int(input())
myList = [[] for _ in range(N + 1)]
dist = [sys.maxsize] * (N + 1)
visit = [False] * (N + 1)

for _ in range(M):
    start, end, weight = map(int, input().split())
    myList[start].append((end, weight))

start_idnex, end_index = map(int, input().split())

def dijkstra(start, end):
    pq = PriorityQueue()
    pq.put((0, start))
    dist[start] = 0
    while pq.qsize() > 0:
        nowNode = pq.get()
        now = nowNode[1]
        if not visit[now]:
            visit[now] = True
            for n in myList[now]:
                if not visit[n[0]] and dist[n[0]] > dist[now] + n[1]:
                    dist[n[0]] = dist[now] + n[1]
                    pq.put((dist[n[0]], n[0]))
    return dist[end]

print(dijkstra(start_idnex, end_index))
