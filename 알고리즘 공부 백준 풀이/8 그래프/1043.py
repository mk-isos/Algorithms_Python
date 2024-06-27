# 문제 분석
# 파티에 참석한 사람들을 1개 집합으로
# 각 파티마다 union연산 이용 -> 사람들 연결
# 각 파티의 대표 노드와 진실 아는 사람들의 대표노드가 동일한지 find연산

# 문제 풀이
# 진실 아는 사람, 파티의 데이터를 대표노드 초기화
# union 연산 수행해서 각 파티에 참여한 사람들을 1개 그룹으로
# find연산 수행해서 각 대표 노드와 진실 아는 사람이 같은 그룹에 있는지 확인
# 모든 파티에 대해 위 과정을 반복
# 각 파티의 대표노드가 진실을 아는 사람과 다른 그룹에 있다면 결괏값 증가
# 과장 가능한 파티의 개수 출력

N, M = map(int, input().split())
trueP = list(map(int, input().split()))  # 진실을 아는 사람 저장
T = trueP[0]
# Python에서 리스트나 다른 시퀀스 유형의 요소를 제거하는 명령이당
del trueP[0]
result = 0
party = [[] for _ in range(M)]

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

def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(M):
    party[i] = list(map(int, input().split()))  # 파티 데이터 저장
    del party[i][0]

parent = [0] * (N + 1)
for i in range(N + 1):  # 대표 노드를 자기 자신으로 초기화
    parent[i] = i

for i in range(M):  # 각 파티에 참여한 사람들을 1개의 그룹으로 만들기
    firstPeople = party[i][0]
    for j in range(1, len(party[i])):
        union(firstPeople, party[i][j])

#  각 파티의 대표 노드와 진실을 아는 사람들의 대표 노드가 같다면 과장할 수 없음
for i in range(M):
    isPossible = True
    cur = party[i][0]
    for j in range(len(trueP)):
        if find(cur) == find(trueP[j]):
            isPossible = False
            break
    if isPossible:
        result += 1  # 모두 다르면 결괏값 1 증가
print(result)
