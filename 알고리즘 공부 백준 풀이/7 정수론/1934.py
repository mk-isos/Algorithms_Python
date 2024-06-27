# 유클리드 호제법 링크

# 문제 풀기

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    result = a * b / gcd(a, b)
    print(int(result))
