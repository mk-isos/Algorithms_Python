from collections import deque

N = int(input())
queue = deque()

for _ in range(N):
    command = input().split()

    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(0 if queue else 1)
    elif command[0] == "front":
        print(queue[0] if queue else -1)
    elif command[0] == "back":
        print(queue[-1] if queue else -1)

# collections 모듈에서 deque 클래스를 가져와서 사용하고 있습니다.
# deque는 "double-ended queue"의 약자로, 양쪽 끝에서 데이터를 추가하거나 삭제할 수 있는 자료구조입니다.
# 이는 리스트보다 효율적인 큐(queue)나 스택(stack)을 구현할 때 사용됩니다.

# deque를 사용하면 리스트의 pop(0)이나 insert(0, ...) 같은 연산보다 훨씬 효율적으로 작동합니다.
# deque의 시간 복잡도는 O(1)이며, 리스트의 경우 O(n)이기 때문에 큰 데이터셋에서 성능상 이점이 있습니다.

# 위의 코드에서 deque를 사용하여 큐(queue)를 구현하여 입력된 명령을 처리하고 있습니다.

# 아 위에 코드 시간초과임.......
# python 3 라메...........

from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()
result = []

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        result.append(str(queue.popleft()) if queue else "-1")
    elif command[0] == "size":
        result.append(str(len(queue)))
    elif command[0] == "empty":
        result.append("0" if queue else "1")
    elif command[0] == "front":
        result.append(str(queue[0]) if queue else "-1")
    elif command[0] == "back":
        result.append(str(queue[-1]) if queue else "-1")

# 결과 출력
sys.stdout.write("\n".join(result))

# 시간 복잡도를 줄이려고 sys.stdin.readline()을 사용
# print 문장도 매번 호출하지 않고 문자열로 결과를 모아두었다가 한 번에 출력하는 방식
# sys.stdout.write('\n'.join(result))

# 휴 이러니까 맞았다..