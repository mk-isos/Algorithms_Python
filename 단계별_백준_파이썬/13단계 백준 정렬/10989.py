# 이 문제는 문제시도한 것 까지 캡쳐 # 내제출

import sys

N = int(sys.stdin.readline())

x = []
for _ in range(N):
    x.append(int(sys.stdin.readline()))

x.sort()

for i in range(N):
    print(x[i])

# 위 코드는 메모리 초과

# 변경된 점:

# 리스트 x를 미리 크기 N으로 초기화하였습니다.
# 입력을 받을 때 x 리스트에 직접 값을 할당하였습니다.
# 불필요한 변수를 최소화하고, 반복문에서 변수 i만 사용하도록 하였습니다.

import sys

N = int(sys.stdin.readline())

x = [0] * N

for i in range(N):
    x[i] = int(sys.stdin.readline())

x.sort()

for i in range(N):
    print(x[i])

# 또 메모리 초과라서 더 줄여야함 .. 허

# 변경된 점:

# 입력값을 받을 때 바로 정렬하여 출력하였습니다.
# 리스트를 사용하지 않고, 입력과 출력을 각각 처리하였습니다.
# sys.stdin.readlines()를 사용하여 여러 줄을 한 번에 입력 받았습니다.
# end=''를 사용하여 print 함수에서 자동으로 추가되는 개행 문자(\n)를 없애고, 한 줄에 모든 출력을 출력했습니다.

#################

# 여기서 더 줄이려면
# sort를 쓰지 않고, intput 대신 int(sys.stdin.readline()) 이 함수를 쓰는것

import sys

N = int(sys.stdin.readline())

# 아이디어는 수를 입력받으면서 바로 해당 위치에 출력

x = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    x[num] += 1     # 횟수를 기록

# 해당 수의 등장 횟수만큼 출력
for i in range(10001):
    if x[i] > 0:    
        for _ in range(x[i]):
            print(i)

#입력으로 받은 수의 등장 횟수를 x 리스트에 기록합니다.
# 최종적으로 x 리스트를 순회하면서 해당 수의 등장 횟수만큼 그 수를 출력