N = int(input())
line = list(map(int, input().split()))

i = 1  # 대기열에서 기대하는 번호표
stack = []  # 대기열에서 현재까지 올라간 번호표들을 저장하는 스택

for num in line:
    if num == i:  # 현재 기대하는 번호표가 나오면 승환이는 그대로 앞으로 나아감
        i += 1
    else:  # 현재 기대하는 번호표가 아니라면 대기열에 넣어줌
        stack.append(num)

    # 스택에서 현재 기대하는 번호표가 나올 때까지 계속해서 간식을 받음
    while stack and stack[-1] == i:
        stack.pop()
        i += 1

# 대기열을 모두 확인한 후에도 스택이 비어있다면 모두가 순서대로 간식을 받을 수 있음
if not stack:
    print("Nice")
else:
    print("Sad")

