
n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# 정렬하기
points.sort(key=lambda point: (point[1], point[0]))

for point in points:
    print(point[0], point[1])
