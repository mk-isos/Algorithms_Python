n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# 정렬하기
points.sort(key=lambda point: (point[0], point[1]))

for point in points:
    print(point[0], point[1])

# print(points)

# lambda는 간단한 익명 함수를 만들 때 사용

# lambda point: (point[0], point[1])는 입력으로 좌표를 받아서
# 해당 좌표의 x좌표와 y좌표를 튜플로 반환하는 함수

######## 다른 사람들 풀이