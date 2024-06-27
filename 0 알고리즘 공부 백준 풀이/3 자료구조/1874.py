# 스택의 원리를 묻는 문제
# 스택의 pop, push, 후입선출 개념
# 스택에 넣는 값은 오름차순 정렬

# 문제 풀이
# if 현재 수열값 >= 오름차순 자연수:
#     while 현재 수열값>= 오름차순 자연수:
#          append
#          오름차순 자연수 1 증가
#          (+)저장
#     pop()
#     (-)저장
# else 현재 수열값 < 오름차순 자연수:
#     pop()
#     if 스택 pop 결과값 > 수열의 수:
#         NO 출력
#     else:
#         (-)저장

import sys
input = sys.stdin.readline()

N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    
    su = A[i]
    
    if su >= num:   #현재 수열 값 >= 오름차순 자연수: 값이 같아질 때까지 push() 수행
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    
    else:           #현재 수열 값 < 오름차순 자연수: pop()을 수행해 수열 원소를 꺼냄
        n = stack.pop()
        if n > su:  #스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 없음
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)


######### 위 코드가 시간 초과라서

import sys

N = int(sys.stdin.readline())
A = [0] * N

for i in range(N):
    A[i] = int(sys.stdin.readline())

stack = []
num = 1
result = True
answer = []

for i in range(N):
    su = A[i]

    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer.append("+")
        stack.pop()
        answer.append("-")
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break
        else:
            answer.append("-")

if result:
    print("\n".join(answer))



