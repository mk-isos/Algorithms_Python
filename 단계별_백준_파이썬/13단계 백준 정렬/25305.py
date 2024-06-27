N, k = map(int, input().split())

# x = []
# for i in range(N):
#     x.append(int(input()))

x = list(map(int, input().split()))

x.sort(reverse=True)

cut_line = x[k - 1]

print(cut_line)