from collections import deque

import sys

# n = int(sys.stdin.readline())

input = sys.stdin.readline

n = int(input())

deq = deque()

for _ in range(n):
    command = input().split()

    if command[0] == "1":
        deq.appendleft(int(command[1]))
    elif command[0] == "2":
        deq.append(int(command[1]))
    elif command[0] == "3":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif command[0] == "4":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif command[0] == "5":
        print(len(deq))
    elif command[0] == "6":
        print(1 if not deq else 0)
    elif command[0] == "7":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif command[0] == "8":
        if deq:
            print(deq[-1])
        else:
            print(-1)

# 또 시간초과가 나서
# import sys

# n = int(sys.stdin.readline())

input = sys.stdin.readline

n = int(input())

# 이걸로 또 해결함!
