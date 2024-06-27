# 문제 분석
# min의 최댓값이 1,000,000,000,000 으로 매우 큰 것 같지만 
# min , max 사이의 수들 안에서 구하면 되니까
# 1,000,000의 데이터만 확인하면 된다
# 제곱수 판별을 일반적인 반복문 구하면 시간 초과 일 듯
# 에라토스테네스의 체 알고리즘 이용해서 풀장

# 문제 풀이 
# 2의 제곱인 4부터 max 안에 제곱수들 찾기
# 데이터를 순차적 탐색 x
# 에라토스테네스의 체 방식으로 제곱수의 배수 형태로 탐색하기
# 시간복잡도 최소화 !!

import math

Min, Max = map(int, input().split())
Check = [False] * (Max - Min + 1)

for i in range(2, int(math.sqrt(Max) + 1)):
    pow = i * i
    start_index = int(Min / pow)
    if Min % pow != 0:
        start_index += 1	# 나머지가 있는 경우 1을 더해 Min보다 큰 제곱수에서 시작하도록 설정
    for j in range(start_index, int(Max / pow) + 1):	# 제곱수를 True로 변경
        Check[int((j * pow) - Min)] = True
count = 0
for i in range(0, Max - Min + 1):
    if not Check[i]:
        count += 1
print(count)
