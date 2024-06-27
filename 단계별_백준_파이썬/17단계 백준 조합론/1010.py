import math


T = int(input())


for _ in range(T):
    N, M = map(int, input().split())

    # 조합 계산 및 결과 출력
    result = math.comb(M, N)
    print(result)
