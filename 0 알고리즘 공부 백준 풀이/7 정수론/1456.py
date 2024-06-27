# 어떤 수가 소수의 N제곱(N ≥ 2) 꼴일 때, 그 수를 거의 소수라고 한다.

# 문제 분석
# 최대 범위 안에 해당하는 모든 소수 구하고
# N 제곱값이 범위 안에 존재하는지 판단해서 문제 해결
# 10^14의 제곱근인 10^7까지 소수 탐색

# 에라토스테네스 체를 이용해서 소수 구하고
# 그 이후에 제곱값이 범위 안에 존재하는지 판별

# 문제 풀이
# 2 ~ B 범위 사이에 존재하는 모든 소수 구하기
# 각 소수를 N제곱한 값이 B보다 커질 때까지 반복문 실행
# 소수를 N제곱한 값이 A보다 크거나 같으면 거의 소수로 판단해서 카운트

# 실제 구현하다보면 N제곱한 값을 구하는 도중 값이 변수 표현 범위를 초과하는 경우가 발생
# 따라서 계싼 오류를 방지하려면 N^k 과 B 값이 아니라 N과 B / N ^ k-1 비교하는 형식으로 식을 정리

import math

Min, Max = map(int, input().split())
A = [0] * (10000001)

for i in range(2, len(A)):
    A[i] = i
for i in range(2, int(math.sqrt(len(A)) + 1)):  # 제곱근까지만 수행
    if A[i] == 0:
        continue
    for j in range(i + i, len(A), i):  # 배수 지우기
        A[j] = 0

count = 0
for i in range(2, 10000001):
    if A[i] != 0:
        temp = A[i]
        # 변수 표현 범위를 넘어갈 수 있어 이항 정리로 처리
        while A[i] <= Max / temp:
            if A[i] >= Min / temp:
                count += 1
            temp = temp * A[i]
print(count)
