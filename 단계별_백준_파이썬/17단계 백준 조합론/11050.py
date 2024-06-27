n, k = map(int, input().split())

result = 1

# 이항 계수 계산
for i in range(k):
    result *= n - i
    result //= i + 1

print(result)
