# 문제에서 수의 개수와 합을 구해야 하는 횟수는 최대 100,000이다
# 게다가 구간마다 합을 매번 계산하면 1초안에 모든 구간 합 계싼을 끝낼 수 없다.
# 이럴 떄 구간 합을 이용!!!
# 구간 합을 매번 계산한다면 최악의 경우 1억 회 이상의 연산을 수행 따라서 1초 이상의 수행 시간이 필요.

import sys

input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prifix_sum = [0]
temp = 0
for i in numbers:
    temp = temp + i
    prifix_sum.append(temp)  # 합 배열 만들기
for i in range(quizNo):
    s, e = map(int, input().split())
    print(prifix_sum[e] - prifix_sum[s - 1])  # 합 배열에서 구간합 구하기
