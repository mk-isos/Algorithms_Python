# 크기를 비교해야하니까 값을 정렬하면 문제를 풀기 좋을 것 같다.
#  N(1 ≤ N ≤ 15,000) 이므로 O(nlogn) 시간 복잡도 사용해도 될 듯하다.
# 즉 정렬 쓸거임.

# 1. 오름차순 정렬
# 2. 투포인터 이동해서 풀 것이다. 정렬한 수를 처음부터 반복해서 풀거다.
# 투 포인터 이동 원칙
# while i < j:
# if 재료 합 <M: 작은 번호 재료를 한 칸 위로 변경
# elif 재료 합> M: 큰 번호 재료를 한 칸 아래로 변경
# else 경우의 수 증가, 양쪽 index 각각 변경

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
A = list(map(int, input().split()))

A.sort()

count = int(0)
i = int(0)
j = int(N - 1)

while i < j:
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1
print(count)
