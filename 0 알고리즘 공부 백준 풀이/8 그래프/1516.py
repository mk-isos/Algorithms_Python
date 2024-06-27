# 문제 분석
# 어떤 건물을 짓기 위해서 먼저 지어야 하는 건물이 있을 수 있음
# 각 건물을 노드라고 생각
# 건물 수 최대가 500 ,시간 복잡도 2초니까 시간 제한 부담은 거의 없다

# 문제 풀이
# 인접 리스트로 그래프 표현
# 건물 생산 시간은 따로 저장
# 진입 차수 리스트 초기화 예제 기준 [0,1,1,2,1] 로

# 위상 정렬 실행하면서 최대 시간 업데이트
# Math.max (현재 노드에 저장된 최대 시간, 이전 노드에 저장된 최대시간 + 현재 노드의 생산시간)

from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)  # 진입차수 리스트
selfBuild = [0] * (N + 1)  # 자기자신을 짓는데 걸리는 시간

for i in range(1, N + 1):
    inputList = list(map(int, input().split()))
    selfBuild[i] = (inputList[0])  # 건물을 짓는데 걸리는 시간
    index = 1
    while True:  # 인접리스트 만들기
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
            break
        A[preTemp].append(i)
        indegree[i] += 1  # 진입차수 데이터 저장

queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = [0] * (N + 1)
while queue:  # 위상정렬 수행
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + selfBuild[now])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N + 1):
    print(result[i] + selfBuild[i])
