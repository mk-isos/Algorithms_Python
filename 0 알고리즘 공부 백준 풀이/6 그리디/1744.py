# 문제 분석
# N의 최대 범위 10,000이라서 시간 복잡도 제약은 적은 듯
# 큰 수들끼리 묶어야 결괏값이 커진다.
# 또 음수끼리 곱하면 양ㅅ수로 변하는 성질 고려

# 문제 풀이
# 수의 집합을
# 1보다 큰 양수, 1, 0, 음수 로 나누어 저장

# 1보다 큰 수의 집합을 정렬해 최댓값부터 차례대로 곱한 후에 더하기
# 원소 개수 홀수일 떄 
# 마지막 남은 수 그냥 더하자

# 음수의 집합도 정렬해서 최솟값부터 차례대로 곱하고 더하기
# 원소 개수가 홀수일 때
# 수열에 0이 있으면 1개남은 음수를 곱해서 0만들기
# 0없으면 그냥 더하자

# 위 과정에서 구한 값들 더하고
# 그 더한 값에 숫자 1의 개수를 더하고 마무리!!!

from queue import PriorityQueue

N = int(input())
plusPq = PriorityQueue()
mlusPq = PriorityQueue()
one = 0
zero = 0

for i in range(N):  # 4가지로 데이터 분리 저장
    data = int(input())
    if data > 1:
        plusPq.put(data * -1)   # 양수 내림차순 정렬을 위해 -1을 곱하여 저장
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        mlusPq.put(data)

sum = 0
while plusPq.qsize() > 1:   # 양수 처리
    first = plusPq.get() * -1
    second = plusPq.get() * -1
    sum += first * second
if plusPq.qsize() > 0:
    sum += plusPq.get() * -1

while mlusPq.qsize() > 1:   # 음수 처리
    first = mlusPq.get()
    second = mlusPq.get()
    sum += first * second
if mlusPq.qsize() > 0:
    if zero == 0:
        sum += mlusPq.get()

sum += one  # 1 처리

print(sum)
