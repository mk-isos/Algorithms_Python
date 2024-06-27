n = int(input())

L = []
for i in range(n):
    L.append(int(input()))

L.sort()
for i in range(len(L)):
    print(L[i])