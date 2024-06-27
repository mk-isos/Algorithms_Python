T = int(input())

i = 1
for i in range(1, T + 1):
    a, b = map(int, input().split())
    print(f"Case #{i}: {a+b}")  # f-string 공부
