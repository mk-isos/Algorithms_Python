S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ')
    


# find 함수는 어떤 찾는 문자가 문자열 안에서 첫 번째에 위치한 순서를 숫자로 출력한다.
#만일 찾는 문자가 문자열 안에 없는 경우에는 -1을 출력하는 함수이다.

S = list(input())
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in S:
        print(S.index(i), end =' ')
    else:
        print(-1, end=' ')