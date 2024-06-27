# 문제 분석
# 에라토스테네스의 체를 이용해 범위에 해당하는 모든 소수 구하기
# 구한 소수 중 팰린드롬 수를 찾기

# 팰린드롬 수를 판별할 때 숫잣값이 리스트 형태로 적절하게 변환이 가능하다.
# 위를 알면 더 쉽게 로직 구현 가능

# 문제 풀이
# 2 ~ 10,000,000 사이에 존재하는 모든 소수 구하기
# 그리고 나서 펠린드롬 수 구해야함

# 소수의 값을 리스트 형태로 변환하고 
# 양 끝의 투 포인터를 비교하면 쉽게 펠린드롬 수 구할 수 있음

import math
N = int(input())
A = [0] * (10000001)

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)) + 1)):  # 제곱근까지만 수행
    if A[i] == 0:
        continue
    for j in range(i + i, len(A), i):  # 배수 지우기
        A[j] = 0

def isPalindrome(target):  # 펠린드롬 수 판별 함수
    temp = list(str(target))
    s = 0
    e = len(temp) - 1
    while (s < e):
        if temp[s] != temp[e]:
            return False
        s += 1
        e -= 1
    return True

i = N
while True:  # N부터 1씩 증가시키면서 소수와 팰림드롬 수가 맞는지 판별
    if A[i] != 0:
        result = A[i]
        if (isPalindrome(result)):
            print(result)
            break
    i += 1
