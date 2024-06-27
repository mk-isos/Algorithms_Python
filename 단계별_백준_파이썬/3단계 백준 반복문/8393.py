n = int(input())

sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)

# 1줄 코드
print(sum(range(1, int(input()) + 1)))
