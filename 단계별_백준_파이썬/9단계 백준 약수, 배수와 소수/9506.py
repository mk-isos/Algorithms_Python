while 1:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
    else:
        print(n, "is NOT perfect.")


##########

while True:
    n = int(input())

    # 입력값이 -1이면 반복문 종료
    if n == -1:
        break

    # 약수를 저장할 리스트 초기화
    arr = []

    # 1부터 n-1까지의 수에 대해 반복
    for i in range(1, n):
        # 현재 수 i가 n의 약수이면 리스트에 추가
        if n % i == 0:
            arr.append(i)

    # 약수의 합이 입력값과 같으면 완전수 출력
    if sum(arr) == n:
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
    else:
        # 약수의 합이 입력값과 다르면 완전수가 아님을 출력
        print(n, "is NOT perfect.")


# join은 문자열을 결합하는 메서드로,
# 리스트에 있는 각 요소들을
# 지정된 구분자(" + " 여기서는 덧셈 기호와 공백)로 연결하여 하나의 문자열로 만든다.

# print(n, " = ", " + ".join(str(i) for i in arr), sep="")에서
# sep=""를 사용하여 공백 대신 빈 문자열을 구분자로 사용하도록 지정했습니다.
# 따라서 출력 결과에서 n, "=", 그리고 약수들이 모두 붙어서 나타납니다.
