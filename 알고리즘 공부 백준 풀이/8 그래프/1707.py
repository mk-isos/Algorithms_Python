# 문제 분석
# 생각해 보면 트리는 항상 이분 그래프가 된다
# 사이클이 발생하지 않으면 탐색하면서 다음 노드를 이번 노드와 다른 집합으로 지정하기
# 하지만 사이클이 발생하면 이분 그래프가 불가능 할 때가 있다.

# 문제 풀이
# 인접리스트로 그래프 구현
# 모든 노드로 각각 DFS탐색
# DFS로 이미 방문한 노드가 나와 같은 집합이면 이분 그래프 아닌 걸로
# 이분 그래프가 아니면 이후 노드는 탐색x

# DFS실행 이유
# 그래프의 모든 노드가 이어져 있지 않고
# 여러 개의 부분 그래프로 존재하는 케이스가 있을지도

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
IsEven = True

def DFS(node):
    global IsEven
    visited[node] = True
    for i in A[node]:
        if not visited[i]:
            check[i] = (check[node]+1)%2
            DFS(i)
        elif check[node] == check[i]:
            IsEven = False


for _ in range(N):
    V, E = map(int, input().split())
    A = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    check = [0] * (V + 1)
    IsEven = True

    for i in range(E):
        Start, End = map(int, input().split())
        A[Start].append(End)
        A[End].append(Start)

    for i in range(1, V + 1):
        if IsEven:
            DFS(i)
        else:
            break

    check[1] = 0
    if IsEven:
        print("YES")
    else:
        print("NO")



