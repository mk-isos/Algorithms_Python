# 시간제한이 0.25초이다 즉 반복문을 사용하면 안된다는 소리

# A = 올라갈 수 있는 거리 , B = 미끄러지는 거리 , V= 나무막대 높이
# 올라가야할 거리 = V-B
# 하루에 갈 수 있는 거리 = A - B

# 올라가야할 거리 % 하루에 갈 수 있는 거리 ==0


# 생각
# 1.25 는 1일보다 0.25더 걸린다는 것 그래서 올림을 해야해서 방법을 찾다가
# 올림함수가 있을거라 생각해서 찾아보았다.
# ceil 함수
# 즉 ceil 함수를 사용해 올림을 사용해주면 된다.
# floor
# 내림함수

import math

A, B, V = map(int, input().split())

day = (V - B) // (A - B)

print(math.ceil(day))

# 위에꺼 틀림
# 문제의 주어진 조건을 다시 확인해 보면, 달팽이가 정상에 도달한 날에는 미끄러지지 않는다고 명시.
# 따라서, 마지막에 정상에 도달하고 나면 다시 미끄러지지 않기 때문에, (V - B) // (A - B)로 계산하는 것이 아니라,
# (V - B - 1) // (A - B)로 계산.
# 올림 함수인 math.ceil() 대신에 일반적인 나눗셈 연산자 /를 사용하여 계산

A, B, V = map(int, input().split())

day = (V - B - 1) // (A - B) + 1

print(day)
