# 문제 분석
# 그리디를 생각하면 쉽게 풀 수 있을 듯?
# 가장 작은 최솟값 만드려면 가장 큰 값들을 뺴주면 될 듯
# 더하기 빼기로만 구성되어 있으니 더하기 부분에 괄호쳐서 모두 계산하고 빼기를 하자

# 문제 풀이
# 더하기 연산 먼저
# 가장 앞에 있는 값에서 더하기로 묶은 값들 빼주기

answer = 0
A = list(map(str, input().split("-")))

def mySum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)
