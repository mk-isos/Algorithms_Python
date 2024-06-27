# 문제 분석과 풀이
# 먼저 선택된 카드 묶음이 비교횟수에 영향을 준다.
# 카드 개수 작은거 먼저 합쳐야 한다.
# 두 개 합친 것을 새로운 카드 묶음으로 다시 데이터에 넣고 정렬

# 딱 생각해보니 데이터 삽입, 삭제, 정렬을 자주 해야함
# 우선순위 큐 이용

from queue import PriorityQueue

N = int(input())
pq = PriorityQueue()

for _ in range(N):
    card = int(input())
    pq.put(card)
data1 = 0
data2 = 0
sum = 0
while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    temp = data1 + data2
    sum += temp
    pq.put(temp)
print(sum)
