# 문제 분석
# 일정 범위에서 최솟값을 구하는 문제
# 그래서 슬라이딩 윈도우와 정렬 사용해야지
# 일반적인 정렬은 nlogn이라서 "N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)"
# L, N 범위때문에 정렬을 사용못함..
# O(n)으로 해결해야 한다.
# 최근 단계별 문제 풀이에서 덱을 구현해보았는데 그래서 덱으로 구현해서 정렬 효과를 볼 것이다.

# 문제 풀이
# 1. 덱에서는 (인덱스, 숫자) 형태의 노드를 클래스로 구현해서 저장

# 덱 저장은 굿노트 사진 첨부할 예정

# 3. 인덱스 범위가 슬라이딩 윈도우를 벗어남
# 이때는 최솟값을 윈도우 범위내에서 찾기로 했으므로 (1,1)은 덱에서 제거. 이후에 최솟값을 출력
# (윈도우를 1칸 슬라이딩 하는 거임)

# 정리하자면, 숫자비교, 윈도우 범위 계산이 끝난 덱에서 맨 앞에 있는 노드의 숫자를 출력하면 정답일 듯

# for N만큼 반복:  # now 리스트를 탐색 (now[i를 현재 값으로 세팅)

# 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거  
# 역의 마지막 위치에 현재 값 저장
# 택의 1번째 위치에서부터 L의 범위를 벗어난 값(now index-L = index)을 덱에서 제거 
# 덱의 1번째 데이터 출력

from collections import deque

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    
    mydeque.append((now[i],i))
    
    if mydeque[0][1] <= i - L: # 범위에서 벗어난 값은 덱에서 제거
        mydeque.popleft()
    
    print(mydeque[0][0], end=' ')


# 위 코드에서 새로운 값이 들어올 때마다 정렬 대신
# 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도를 줄였다.

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    
    mydeque.append((now[i],i))
    
    if mydeque[0][1] <= i - L: # 범위에서 벗어난 값은 덱에서 제거
        mydeque.popleft()
    
    print(mydeque[0][0], end=' ')


