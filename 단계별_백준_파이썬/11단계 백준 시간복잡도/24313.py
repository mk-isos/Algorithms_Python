a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if (a1 * n0 + a0 <= c * n0) and (a1 <= c):
    print(1)
else:
    print(0)


# f(n) = 7n + 7, g(n) = n, c = 8, n0 = 1이다.
# f(1) = 14, c × g(1) = 8이므로 O(n) 정의를 만족하지 못한다.
