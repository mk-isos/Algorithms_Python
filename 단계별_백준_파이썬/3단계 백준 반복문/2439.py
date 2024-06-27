N = int(input())

for i in range(1, (N + 1)):
    print(" " * (N - 1) + "*" * i)

################## 위아래가 다르다 이유는? (아래가 정답)
# 앞에 공백 차이 -1, -i
N = int(input())

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)
