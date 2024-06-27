# 문제 분석
# N의 최대가 10,000,000으로 졸라 크다..
# nlogn보다 더 빠른 알고리즘이 필요하다.
# 문제에서 숫자크기가 10,000보다 작다했으니 기수 정렬과 함께 많이 사용되는 계수 정렬 (counting sort)를 사용해서 문제 해결
# 계수 정렬은 기수정렬보다 로직이 좀 더 간단

# 문제 풀이
# 숫자 크기 10,000보다 작기 떄문에 10,001 크기의 리스트 선언
# 입력 받는 수를 차례대로 리스트의 인덱스 값을 1 증가
# 그 후 리스트 탐색하면서 해당 값이 있는 인덱스를 값만큼 반복하여 출력

import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001
for i in range(N):
    count[int(input())] += 1
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
