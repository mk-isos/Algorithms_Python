# 문제 분석
# N -1 개 비율로 N개 비율을 알 수 있다 ?
# 그래프 관점으로 생각 -> 사이클 없는 트리 구조
# 그러면 임의의 노드에서 DFS 진행하면서 정답 찾기
# DFS과정에서 유클리드 호제법을 사용해서
# 비율들의 최소 공배수와 최대 공약수 구하고
# 재료의 최소 질량을 구해보자 .....

# 문제 풀이
# 인접리스트로 각 재료의 비율자료를 그래프로 구현
# 데이터 저장 떄마다 비율 관련 최소 공배수 업데이트
# 임의의 시작점에 최대 공배수 값 저장
# 시작점에서 DFS로 탐색 : 각 노드의 값을 이전 노드의 값과의 비율 계산
# 각 노드의 값을 모든 노드의 최대 공약수로 나눠서 출력

N = int(input())
A = [[] for _ in range(N)]
visited = [False] * (N)
D = [0] * (N)
lcm = 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            D[next] = D[v] * i[2] // i[1]
            DFS(next)

for i in range(N - 1):
    a, b, p, q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))

D[0] = lcm
DFS(0)
mgcd = D[0]
for i in range(1, N):
    mgcd = gcd(mgcd, D[i])
for i in range(N):
    print(int(D[i] // mgcd), end=' ')
