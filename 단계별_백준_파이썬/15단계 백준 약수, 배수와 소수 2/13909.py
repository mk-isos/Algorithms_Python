# N = int(input())

# open_windows = [0] * N  # 초기에 모든 창문은 닫혀있음

# for person in range(1, N + 1):
#     for window in range(person - 1, N, person):
#         # 각 사람의 배수 번째 창문 상태 변경
#         open_windows[window] = 1 - open_windows[window]

# result = sum(open_windows)

# print(result)

# 위 코드 메모리 초과

# 그래서 코드의 메모리를 더 줄이기 위해 리스트를 사용하는 대신
# 변수를 사용하여 현재 열려 있는 창문의 개수를 체크

# open_windows 리스트 대신에 open_windows_count 변수를 사용
# 하다가 실패...


# 다시 문제 접근
# 주어진 숫자 N이 21억이란 숫자이므로, 단순 반복으론 해결 불가

# 생각해보면 각각 제곱 수에서 값이 변함.
# 이건 노가다 해서 작은 수에 대해서 규칙을 찾아봐야함
# 예를 들어 11122222333333344444444...

# 그럼 아예 색다르게 코드를 구현할 수 있다.

import sys

N = int(sys.stdin.readline())
result = 0
x = 1
while x * x <= N:
    x += 1
    result += 1
print(result)

# 다른 사람들의 풀이를 보니 아예 이 풀이를 한줄로

print(int(input()**0.5))

# 이렇게 풀어버림..
# 이게 막상보면 쉬운데 직접 구현할 때 이렇게 한번에 풀기는 쉽지않다.
