# 문제 분석
# 자연수를 받아 자릿수별로 정렬해야함.
# 먼저 숫자를 각 자릿수별로 나누는 작업 필요
# -> 파이썬에서는 input 데이터를 list로 변환하면 자동으로 자릿수 나누어 리스트화 해준다.
# ( 파이썬 짱 )

# 이번에도 그저 sort()함수를 이용하면 되지만, N의 길이가 크지 않으니까 선택 정렬을 사용해서 내림차순 정렬해봐야지.

# 정렬 알고리즘 링크 첨부

# 문제 풀이
# 1. list 변환 사용해서 데이터를 리스트에 저장
# 2. 데이터들을 선택 정렬 알고리즘 이용해서 내림차순 정렬
# 내림차순 정렬이니까 최댓값 찾아서 기준이 되는 자리와 swap

import sys

print = sys.stdout.write

A = list(input())

for i in range(len(A)):
    Max = i

    for j in range(i + 1, len(A)):
        if A[j] > A[Max]:  # 내림차순이므로 최댓값을 찾음
            Max = j

    if A[i] < A[Max]:
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp

for i in range(len(A)):
    print(A[i])
