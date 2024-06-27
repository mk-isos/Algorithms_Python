# 큐 이해 문제
# 가장 위의 카드를 가장 아래에 있는 카드 밑으로 옮기는 동작 = 큐의 선입선출 성질
# 카드 개수 최대가 500,000이므로 시간 복잡도 제약도 크지 않음
# 큐로 해결해야지

# 문제 풀이
# 1 popleft를 수행하여 맨 앞의 카드 버리기
# 2 popleft -> append 맨 앞 카드를 가장 아래로
# 3 큐 크기가 1까지 과정 1,2 반복 후 출력

from collections import deque
N = int(input())
myQueue = deque()
for i in range(1, N+1):
    myQueue.append(i)
while len(myQueue) > 1:     # 카드가 1장 남을 때까지
    myQueue.popleft()       # 맨 위의 카드를 버림
    myQueue.append(myQueue.popleft())   # 맨 위의 카드를 가장 아래 카드 밑으로 이동
print(myQueue[0])   # 마지막으로 남은 카드 출력