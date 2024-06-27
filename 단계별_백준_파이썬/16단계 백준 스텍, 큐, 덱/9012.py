T = int(input())

for _ in range(T):
    parentheses_string = input()
    stack = []  # 스택을 사용하여 괄호의 짝을 확인하기 위한 빈 리스트 생성

    # 괄호 문자열을 한 글자씩 확인
    for char in parentheses_string:
        if char == "(":  # 여는 괄호일 경우
            stack.append(char)  # 스택에 추가
        else:  # 닫는 괄호일 경우
            # 스택이 비어있는 경우에는 올바르지 않은 괄호 문자열
            if not stack:
                print("NO")
                break
            stack.pop()  # 스택에서 여는 괄호를 제거

    else:
        # 반복이 끝난 후에도 스택이 비어있으면 "YES" 출력
        if not stack:
            print("YES")
        else:
            # 스택이 비어있지 않으면 "NO" 출력
            print("NO")
