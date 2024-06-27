# 문제 분석
# N의 최대 범위가 100,000, nlogn 알고리즘으로 풀기 가능
# 데이터 삽입 떄 마다 절댓값관련 정렬해야함. -> 우선순위 큐?
# 근데 절대값 정렬해야해서 우선순위 큐의 정렬기준을 직접 정해야할 듯
# * 절대값 같으면 음수 우선 출력인듯

# 문제 풀이
# 1 x = 0일 때 
# 큐가 비어 있으면 0 출력
# 아니면 절댓값이 최소인 값 출력
# 절댓값 같으면 음수 출력
# 2 x = 1일 때
# put으로 큐에 새로운 값을 추가하고 우선순위 큐 정렬 기준으로 자동 정렬

from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline

N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else:
        # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
        myQueue.put((abs(request), request))

# print = sys.stdout.write: 
# 기존의 print 함수를 sys.stdout.write 함수로 재정의. 
# 이렇게 하면 출력이 줄 바꿈 없이 이어짐.