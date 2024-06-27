N = int(input())

x = []
for i in range(N):
    x.append(int(input()))


x.sort()


for i in range(len(x)):
    print(x[i])

## 위 코드는 시간초과

import sys

N = int(sys.stdin.readline())

x = []
for _ in range(N):
    x.append(int(sys.stdin.readline()))

x.sort()

for i in range(N):
    print(x[i])

# sys.stdin.readline()을 사용하여 더 빠르게 입력을 받을 수 있습니다. 
# 단, 주의할 점은 sys.stdin.readline()을 사용할 때는 문자열의 개행 문자('\n')도 함께 입력으로 들어오기 때문에 
# int()로 변환할 때 이를 처리해주어야 합니다. 위 코드에서는 int(sys.stdin.readline())로 입력을 받고 있습니다.