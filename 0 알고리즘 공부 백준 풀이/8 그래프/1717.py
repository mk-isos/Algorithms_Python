# 문제 분석
# 최대 원소 개수 1,000,000과 질의 개수 100,000이 큰 편이라서 
# 경로 압축이 필요하다.
# 전형적인 유니온 파인드 문제

# 문제 풀이
# 처음에는 노드가 연결돼 있지 않으니 각 노드 대표는 자기 자신
# 각 노드의 값을 자기 인덱스 값으로 초기화

# find연산으로 특정 노드의 대표를 찾고
# union연산으로 2개의 노드를 각 대표 노드를 찾아 연결


import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
parent = [0] * (N + 1)


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])  # 재귀 형태로 구현 -> 경로 압축 부분
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


for i in range(0, N + 1):
    parent[i] = i

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")
