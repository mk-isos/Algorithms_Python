# 문제 분석
# 지금까지 그래프 데이터를 저장하고 저장한 자료구조를 이용
# 이 문제는 그래프 원리로 그래프를 역으로 그리는 방식으로 접근해서 풀어야 할 듯

# A B C 특정 무게 상태를 1개의 노드로 가정, 무게 상태가 에지로 이어진 인접노드라 생각

# 문제 풀기
# 처음 출발노드를 (0, 0, 3번째 물통 용랼)
# BFS탐색
# BFS 과정
# 1 노드에서 갈 수 있는 6개의 경우(A- B,A- C, B- A,B-C,C- A, C- B)에 관해 다음 노드로 정해 큐에 추가한다. 
# A, B, C 무게가 동일한 노드에 방문한 이력이 있을 때는 큐에 추가하지 않는다.

# 2 보내는 물통의 모든 용량을 받는 물통에 저장하고, 보내는 물통에는 0을 저장한다. 
# 단, 받는 물통이 넘칠 때 는 초과하는 값만큼 보내는 물통에 남긴다.

# 3 큐에 추가하는 시점에 1번째 물통(A)의 무게가 0일 때가 있으면 
# 3번째 물통(C)의 값을 정답 리스트에 추가한다.

from collections import deque

Sender = [0, 0, 1, 1, 2, 2]
Receiver = [1, 2, 0, 2, 0, 1]
now = list(map(int, input().split()))
visited = [[False for j in range(201)] for i in range(201)]
answer = [False] * 201

def BFS():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    answer[now[2]] = True
    while queue:
        now_Node = queue.popleft()
        A = now_Node[0]
        B = now_Node[1]
        C = now[2] - A - B  # C는 전체 물의 양에서 A와 B를 뺀 것
        for k in range(6):  # A → B, A → C, B → A, B → C, C → A, C → B
            next = [A, B, C]
            next[Receiver[k]] += next[Sender[k]]
            next[Sender[k]] = 0
            if next[Receiver[k]] > now[Receiver[k]]:  # 물이 넘칠 때
                # 초과하는 만큼 다시 이전 물통에 넣어주기
                next[Sender[k]] = next[Receiver[k]] - now[Receiver[k]]
                next[Receiver[k]] = now[Receiver[k]]  # 대상 물통 최대로 채우기
            if not visited[next[0]][next[1]]:  # A와 B의 물의 양으로 방문 리스트 체크
                visited[next[0]][next[1]] = True
                queue.append((next[0], next[1]))
                if next[0] == 0:  # A의 물의 양이 0일때 C의 물의 무게를 정답 변수에 저장
                    answer[next[2]] = True

BFS()
for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')
