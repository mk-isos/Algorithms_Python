def gcd(a, b):  # 최대공약수, 유클리드 호제
    while b:
        a, b = b, a % b
    return a


A, B = map(int, input().split())
C, D = map(int, input().split())

N = gcd(A * D + C * B, B * D)
print((A * D + C * B) // N, B * D // N)
