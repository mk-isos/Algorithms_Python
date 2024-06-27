N = [i for i in range(1, 30 + 1)]

for _ in range(28):
    chk = int(input())
    N.remove(chk)

print(min(N))
print(max(N))
