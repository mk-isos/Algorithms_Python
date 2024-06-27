# 문제 분석
# 파이썬을 이용하면 솔직히 매우 쉽게 정렬이 가능하다. sort() 함수 이용

# 정렬을 직접 구현해 해결해봐야지

# N의 최대 범위가 1,000 이라서  O(n^2)으로 풀기 가능.
# 버블 정렬 이용해서 풀어야지 (그래도 시간 복잡도 안에서 해결 가능)

# 정렬 알고리즘 링크 넣기

N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(N):
    print(A[i])