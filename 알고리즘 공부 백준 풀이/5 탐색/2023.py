# 문제 분석
# DFS는 재귀함수 형태
# 재귀 함수에 자릿수 개념을 붙여서 구현해보자
# (?) 문제 조건에 맞도록 가지치기도

# 문제 풀이
# 소수란
# 수의 약수가 1과 자기 자신인 수
# 자릿수가 한 개인 소수 : 2 3 5 7
# 4 6 8 9를 제외한 가지치기 방식 적용
# 이어서 자릿수가 두 개인 현재수 * 10 + a를 계산
# 그래서 이게 소수라면 재귀 함수로 자릿수를 하나 늘린다.

# 단 a 가 짝수인 경우는 항상 2를 약수로 가지니까 가지치기로 a가 짝수인 경우 제외
# 이런 방식으로 자릿수를 N까지 확장했을 때 그 값이 소수면 출력해버리자

# 풀이 사진

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())


def isPrime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True


def DFS(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:  # 짝수라면 더 이상 탐색 불필요
                continue
            if isPrime(number * 10 + i):  # 소수이면 자릿수 늘림
                DFS(number * 10 + i)


# 일의 자리 소수는 2, 3, 5, 7이므로 4가지 수 에서만 시작
DFS(2)
DFS(3)
DFS(5)
DFS(7)
