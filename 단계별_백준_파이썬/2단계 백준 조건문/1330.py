#방법 1
# 아래 처럼 짰다가 오류뜸 그래서 뭐지 하고 구글링 했는데 다들 이렇게 씀..
# 
a, b = map(int, input().split())

if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")
# 아니 위 코드 그냥 제출하니 맞음 . 뭐지 공부할 필요가 있다.

#방법2
#예외처리 해주기
try:
    a, b = map(int, input().split())
except ValueError:
    print("올바른 정수 값을 입력하세요.")
else:
    if a > b:
        print(">")
    elif a == b:
        print("==")
    else:
        print("<")
