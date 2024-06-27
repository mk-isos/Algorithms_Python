# 스택의 개념을 익히고 실습하는 문제

import sys

stack = []

n = int(sys.stdin.readline())


for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "1":
        stack.append(command[1])
    elif command[0] == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "3":
        print(len(stack))
    elif command[0] == "4":
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == "5":
        if stack:
            print(stack[-1])
        else:
            print(-1)

# list로 스택 구현

# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# -> stack.append
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# -> if stack:
        #     print(stack.pop())
        # else:
        #     print(-1)
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# -> len(stack)
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# -> if stack:
        #     print(0)
        # else:
        #     print(1)
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
# -> if stack:
        #     print(stack[-1])
        # else:
        #     print(-1)