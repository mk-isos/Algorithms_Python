# 슬라이딩 윈도우 알고리즘
# 2개의 포인터로 범위를 지정한 다음, 범위를 유지한 채로 이동하며 문제를 해결.
# 범위 : window , 이동 : sliding

# 문제 분석
# P 와 S 의 길이가 1,000,000으로 매우 크기 때문에 O(n)의 시간복잡도 알고리즘으로 문제를 해결해야함.

# 문제 풀이
# 1. 리스트 s와 비밀번호 체크리스트를 저장한다.
# 2. 슬라이딩 윈도우에 포함된 문자열로 현재 상태리스트를 만든다.
# 3. 현재상태리스트와 비밀번호 체크리스트를 비교하여 유효한지 확인한다.
# 4. 윈도우를 한 칸씩 이동하며 현재 상태 리스트를 업데이트.
# 5. 또 2, 3번 확인
# 6. 5에서 현재 상태 리스트를 새로 만들때는 빠지는 거 하나 빼주고 들어오는 거 하나 넣어서 현재 상태 리스트를 만든다.

# 6번 처럼 기존 검사 결과에 새로 들어온 문자열, 제거되는 문자열만 반영하여 확인하는 것이 핵심.

checkArr = [0] * 4
myArr = [0] * 4
checkSecret = 0

# 함수 정의
def myadd(c): #새로 들어온 문자를 처리하는 함수
    global checkArr,myArr,checkSecret
    if c == 'A':
        myArr[0] += 1
        if myArr[0] == checkArr[0]:
            checkSecret += 1
    elif c == 'C':
        myArr[1] += 1
        if myArr[1] == checkArr[1]:
            checkSecret += 1
    elif c == 'G':
        myArr[2] += 1
        if myArr[2] == checkArr[2]:
            checkSecret += 1
    elif c == 'T':
        myArr[3] += 1
        if myArr[3] == checkArr[3]:
            checkSecret += 1

def myremove(c): #제거되는 문자를 처리하는 함수
    global checkArr, myArr, checkSecret
    if c == 'A':
        if myArr[0] == checkArr[0]:
            checkSecret -= 1
        myArr[0] -= 1
    elif c == 'C':
        if myArr[1] == checkArr[1]:
            checkSecret -= 1
        myArr[1] -= 1
    elif c == 'G':
        if myArr[2] == checkArr[2]:
            checkSecret -= 1
        myArr[2] -= 1
    elif c == 'T':
        if myArr[3] == checkArr[3]:
            checkSecret -= 1
        myArr[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkArr = list(map(int, input().split()))
for i in range(4):
    if checkArr[i] == 0:
        checkSecret += 1
for i in range(P):  #초기 P 부분 문자열 처리 부분
    myadd(A[i])
if checkSecret == 4: #4자릿수와 관련된 크기가 모두 충족될 때 유효한 비밀번호
    Result += 1
for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1
print(Result)



