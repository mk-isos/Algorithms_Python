# 문제 분석
# 숫자 사이 소수 출력 문제
# N의 최대 범위가 1,000,000이라서 일반적인 소수 구하기 방식 x
# 에라토스테네스 방법

# *일반적인 방법 소수를 찾을 때 
# 2이상부터 자기 자신보다 작은 수로 나눴을 때 나머지가 0이 아닌 수

# 문제 풀이
# 크기 N + 1인 리스트를 선언
# 값은 인덱스 값으로 채우기 (소수 구하기에서 0번쨰 배열 사용 x)
# 1은 소수 아니라 삭제
# 2부터 N의 제곱근까지 탐색
# 값이 인덱스 값이면 그대로, 그 값의 배수를 탐색해 0으로 변경

# 배열에 남은 숫자 중 M이상 N이하의 수 모두 출력


import math

M, N = map(int, input().split())
A = [0] * (N + 1)

for i in range(2, N + 1):
    A[i] = i
for i in range(2, int(math.sqrt(N)) + 1):  # 제곱근까지만 수행
    if A[i] == 0:
        continue
    for j in range(i + i, N + 1, i):  # 배수 지우기
        A[j] = 0
for i in range(M, N + 1):
    if A[i] != 0:
        print(A[i])

