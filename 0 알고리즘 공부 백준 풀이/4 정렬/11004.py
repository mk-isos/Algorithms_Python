# 문제 분석
# 퀵 정렬을 연습해볼텐데 
# 사실 퀵 정렬은 최악의 상황에 O(n^2)이라서 이 문제의 경우 병합정렬쓰는게 나을 듯

# 퀵 정렬 pivot을 정하는 법
# • pivot == K
# : K번째 수를 찾은 것이므로 알고리즘을 종료한다.
# • pivot > K
# : pivot의 왼쪽 부분에 K가 있으므로 왼쪽(S~ pivot - 1)만 정렬을 수행한다.
# • pivot < K
# : pivot의 오른쪽 부분에 K가 있으므로 오른쪽(pivot + 1~ E)만 정렬을 수행한다.

# 저는 배열의 중간위치를 pivot으로

# 문제 풀이

# 피벗 구하기 함수(시작, 종료):
# 데이터가 2개인 경우는 바로 비교하여 정렬
# M(중앙값)
# 중앙값을 시작 위치와 swap 
# pivot (피벗)을 시작 위치 값 A[S]로 저장
# i (시작점), j(종료점)

# while i <= j:
# 피벗보다 큰 수가 나올 때까지 i 증가 
# 피벗보다 작은 수가 나올 때까지 j 감소 
# 찾은 i와 j 데이터를 swap


################################################

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))


def quickSort(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K:  # K번째 수가 pivot이면 더이상 구할 필요 없음
            return
        elif K < pivot:  # K가 pivot보다 작으면 왼쪽 그룹만 정렬
            quickSort(S, pivot - 1, K)
        else:  # K가 pivot보다 크면 오른쪽 그룹만 정렬
            quickSort(pivot + 1, E, K)


def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def partition(S, E):
    global A

    if S + 1 == E:
        if A[S] > A[E]:
            swap(S, E)
        return E

    M = (S + E) // 2
    swap(S, M)
    pivot = A[S]
    i = S + 1
    j = E
    while i <= j:
        while pivot < A[j] and j > 0:
            j = j - 1
        while pivot > A[i] and i < len(A)-1:
            i = i + 1
        if i <= j:
            swap(i, j)
            i = i + 1
            j = j - 1
    # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
    A[S] = A[j]
    A[j] = pivot
    return j


quickSort(0, N - 1, K - 1)
print(A[K - 1])
