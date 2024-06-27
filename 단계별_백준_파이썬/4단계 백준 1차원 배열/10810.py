# 공 넣기

N, M = map(int, input().split())
basket = [0] * (N + 1)  # 바구니 0으로 채우기

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j + 1):
        basket[n] = k

for i in range(1, N + 1):
    print(basket[i], end=" ")  # end = ' ' : 공백으로 구분해 출력
