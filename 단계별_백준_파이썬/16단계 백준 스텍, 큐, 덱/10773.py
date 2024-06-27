import sys

stack = []

n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "0":
        stack.pop()
    else:
        stack.append(int(command[0]))

result = sum(stack)
print(result)
