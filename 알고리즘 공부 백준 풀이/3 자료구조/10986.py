# N의 최댓값이 10^6이라 모든 구간 합을 구해야 하므로 1초 안에 연산하기는 어렵다.
# 그래서 구간 합 배열을 이용하자.

# 나머지 합 문제 풀이의 핵심 아이디어
# • (A + B》 % C는 ((A % C) + (B% C) % C와 같다.
# 다시 말해 특정 구간 수들의 나머지 연산을 더해 나머지 연산을 한 값과 이 구간 합의 나머지 연산을 한 값은 동일하다.
# • 구간 합 배열을 이용한 식 S[j] - S[i]는 원본 리스트의 i + 1부터 j까지의 구간 함이다.
# • S[j]) % M의 값과 S[i] % M의 값이 같다면 (S[j]- S[i]) % M은 0이다.
#  즉, 구간 함 배열의 원소를 M으로 나눈 나머지로 업데이트하고 S[i]와 S[j]가
#  같은 (i, j)쌍을 찾으면 원본 리스트에서 i + 1부터 j까지의 구간 합이 M으로 나누어떨어진다는 것을 알 수 있다.

# S[i] = S[i-1] + A[i]  # 합 배열 저장
# (C[i] * (C[i] - 1) / 2)  # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
S[0] = A[0]
answer = 0
for i in range(1, n):
    S[i] = S[i - 1] + A[i]  # 합 배열 저장

for i in range(n):
    remainder = int(S[i] % m)  # 합 배열의 모든 값에 % 연산 수행
    if remainder == 0:  # 0 ~ i까지의 구간 합 자체가 0일 때 정답에 더하기
        answer += 1
    C[remainder] += 1  # 나머지가 같은 인덱스의 개수

for i in range(m):
    # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if C[i] > 1:
        answer += C[i] * (C[i] - 1) / 2

print(int(answer))
