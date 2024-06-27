while True:
    s = input()
    
    # 입력 종료 조건
    if s == '.':
        break

    stack = []
    is_balanced = True

    for char in s:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            # 스택이 비어있는 경우나 괄호의 짝이 맞지 않는 경우
            if not stack or (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '['):
                is_balanced = False
                break
            stack.pop()

    # 스택이 비어있고 균형이 잘 맞았으면 "yes", 아니면 "no" 출력
    if is_balanced and not stack:
        print("yes")
    else:
        print("no")
