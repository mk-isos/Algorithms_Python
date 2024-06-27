# 입 출력 다 같은데 틀렸다네 ..
#공백 으로 출력안해서 틀렸네 ..

N, M = map(int, input().split())
basket = [i for i in range(1, N + 1)]

for i in range(M):
    i, j = map(int, input().split())

    # list index에 접근하기 위해 i -1, j도 포함되어야 하니까 j-1+을 range로!!
    temp = basket[i - 1 : j - 1 + 1]
    temp.reverse()
    basket[i - 1 : j] = temp

for i in range(N):
    print(basket[i], end=" ")


