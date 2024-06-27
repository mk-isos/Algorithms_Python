# 문제 분석
# N, M 최대 크기가 100. 매우 작음 -> 시간제한 고민 x
# 이 문제는 완전 탐색 진행하며 몇 번째 깊이에서 원하는 값을 찾을지 구하는 것과 동일

# BFS를 사용해 최초로 도달했을 떄 깊이를 출력하면 문제를 해결 가능

# DFS보다 BFS를 쓰는 이유
# BFS가 해당 깊이에서 갈 수 있는 노드 탐색을 마치고 다음 깊이로 넘어가니까

# 문제 풀이
# 예제 입력 2번 기준
# 먼저 2차원 리스트에 데이터를 저장
# (1,1)에서 BFS 실행
# 상하좌우 네 방향을 보며 인접한 칸을 보고 숫자가 1이면서 아직 미방문이면 큐에 삽입
# 종료 지점 (N,M)에서 BFS 종료 후 깊이 출력

# 방문된 데이터의 값을 depth의 값으로 저장하기 위해 이전 데이터 값 +1로 업데이트


from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
A = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    numbers = list(input())
    for j in range(M):
        A[i][j] = int(numbers[j])


def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]

            if x >= 0 and y >= 0 and x < N and y < M:
                if A[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    A[x][y] = A[now[0]][now[1]] + 1
                    queue.append((x, y))


BFS(0, 0)

print(A[N - 1][M - 1])
