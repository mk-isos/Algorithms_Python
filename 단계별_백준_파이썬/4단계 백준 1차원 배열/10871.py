N, X = map(int, input().split())
L = list(map(int, input().split()))

for i in range(N):
    if L[i] < X:
        print(L[i], end=" ")  # end=" " 가 공백으로 구분해 출력
