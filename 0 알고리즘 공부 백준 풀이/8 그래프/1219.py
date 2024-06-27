# 문제분석
# 벨만 포드 원리 이용해서 내부 로직을 조금 바꿔야할 듯
# 기존 벨만 포드는 최단 거리 구하기
# 이번에는 돈의 액수 최대기에 업데이트 방식을 반대로 변경
# 음수 사이클아니고 양수 사이클 찾기 그리고 예외 처리 1개 필요
# 또 신경쓸게 ...

# 문제 풀이
# 에지 리스트 에지 데이터 저장, 거리 리스트 초기화
# 돈 최대 배열에 저장, 시작점 초기화
# 벨만포드 수행
# 도착 도시의 값에 따라 결과 출력

import sys
input = sys.stdin.readline
N, sCity, eCity, M = map(int, input().split())
edges= []
distance = [-sys.maxsize] * N  # 최단거리 배열 초기화

for _ in range(M):
    start, end, price = map(int, input().split())
    edges.append((start, end, price))

cityMoney = list(map(int, input().split()))

# 변형된 벨만포드 수행
distance[sCity] = cityMoney[sCity]  # 출발 초기화
# 양수 사이클이 전파 되도록 충분히 큰 수로 반복
for i in range(N+101):
    for start, end, price in edges:
        if distance[start] == -sys.maxsize:
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + cityMoney[end] - price:
            distance[end] = distance[start] + cityMoney[end] - price
            if i >= N-1:
                distance[end] = sys.maxsize

if distance[eCity] == -sys.maxsize:
    print("gg")
elif distance[eCity] == sys.maxsize:
    print("Gee")
else:
    print(distance[eCity])

