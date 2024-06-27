# 문제 분석
# 도시의 연결 유무를 유니온 파인드 연산을 이용해야 겠다 생각이 들어야함
# 일반적으론 유니온 파인드는 그래프 영역에서 활용 but 이 문제와 같이 단독으로도 활용 가능
# 이 문제는 도시 간 연결 데이터를 인접 행렬의 형태로
# 인접 행렬을 탐색하면서 연결될 때 마다 union 연산 수행

# 문제 해결
# 도시와 여행 경로 데이터를 저장
# 각 노드와 관련된 대표 노드 리스트 값으로 초기화

# 인접행렬 탐색 하면서 도시가 연결돼 있을 때 유니온 연산 수행
# 도시의 대표 노드가 모두 같은지 확인하고 결괏값 출력

N = int(input())
M = int(input())
dosi = [[0 for j in range(N+1)] for i in range(N+1)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(1, N+1):
    dosi[i] = list(map(int, input().split()))
    dosi[i].insert(0, 0)

route = list(map(int, input().split()))
route.insert(0, 0)

parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i

for i in range(1, N+1):
    for j in range(1, N+1):
        if dosi[i][j] == 1:
            union(i,j)

index = find(route[1])
isConnect = True
for i in range(2, len(route)):
    if index != find(route[i]):
        isConnect = False
        break

if isConnect:
    print("YES")
else:
    print("NO")
