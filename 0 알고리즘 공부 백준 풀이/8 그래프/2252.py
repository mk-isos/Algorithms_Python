# 문제 분석
# 학생들을 노드로 키 순서 비교를 에지로 만들고 노드 순서를 출력

# 문제 풀이
# 인접리스트에 노드 저장, 진입 차수 배열값 업데이트
# 위상 정렬 수행
# 1. 진입차수가 0인 노드를 큐에 저장
# 2. 큐에소 데이터 뽑아서 탐색 결과에 추가, 노드의 진입 차수 1씩 감소
# 3. 진입 차수가 0이 되는 노드를 큐에 삽입
# 4. 큐 빌 때 까지 위 과정들 반복

from collections import deque
N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)  # 진입차수 배열

for i in range(M):
    S, E = map(int, input().split())
    A[S].append(E)
    indegree[E] += 1  # 집입차수 데이터 저장

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:  # 위상정렬 수행
    now = queue.popleft()
    print(now, end=' ')
    for next in A[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)
