#  N(1 ≤ N ≤ 2,000) 라서 좋은 수 하나를 찾는 알고리즘의 시간 복잡도는 N^2보다 작아야함.
# 만약 좋은 수 하나를 찾는데 시간 복잡도가 N^2을 사용해버리면 
# 최종 시간 복잡도는 N^3이 되어서 제한시간안에 풀 수가 없다.
# 따라서 nlogn 이 최소겠다.

# 그래서 정렬, 투 포인터 알고리즘을 사용할 것이다.
# 단 , 정렬된 데이터에서 자기 자신을 좋은 수 만들기에 포함하면 안된다.

# 풀이
# 1. 수를 입력받아 리스트에 저장 -> 정렬
# 2. 투포인터 이동
# 투포인터 알고리즘을 계속 반복.

# for N 만큼 반복 :
# 변수 초기화(찾고자 하는 값 find- A[k], 포인터 i, 포인터 j)
# while i < j:
# if A[i] + Alj] == find:
# 두 포인터 1, j가 k가 아닐 때 좋은 수 개수 1 증가 및 while 문 종료 두 포인터 나 j가 K가 맞을 때 포인터 변경 및 계속 수행
# elif A[i] + A[i] < find: 포인터 오 증가
# else: 포인터 j 감소

import sys
input = sys.stdin.readline

N = int(input())
Result = 0
A = list(map(int, input().split()))

A.sort()

for k in range(N):
    find = A[k]
    i = int(0)
    j = int(N - 1)
    
    while i < j:  # 투 포인터 알고리즘
        if A[i] + A[j] == find:  # find는 서로 다른 두 수의 합 이어야 함을 체크
            if i != k and j != k:
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1

print(Result)