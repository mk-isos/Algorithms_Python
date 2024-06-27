## 블로그 업로드 x

# 문제 분석
# N과 M의 크기가 작은 편 , 시간 복잡도는 크게 신경 안써야지
# 예를 들어 A노드에서 방문 노드가 B , C이면 B, C는 A의 신뢰받는 노드가 된다.

# 문제 풀이
# 인접리스트로 그래프 표현
# 모든 노드를 각각 BFS로 탐색
# 탐색 노드들 신뢰도 1 씩 올리기
# 신뢰도 리스트 탐색하면서 최댓값을 MAX로 지정
# MAX가지고 있는 값들 오름차순 출력하기

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1  # 신규 노드 인덱스의 정답 리스트 값을 증가
                queue.append(i)


for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

for i in range(1, N + 1):  # 모든 노드에서 BFS 실행
    visited = [False] * (N + 1)
    BFS(i)

maxVal = 0
for i in range(1, N + 1):
    maxVal = max(maxVal, answer[i])

for i in range(1, N + 1):
    if maxVal == answer[i]:
        print(i, end=' ')

## 위 시간 초과

## 시간초과 결국 해결못해서  Pypy로도 돌려보고 다했는데 뭐지 
### 결국 구글링해서 풀었는데 다시 풀어봐야지