N = int(input())
M = int(input())

prime = []
for num in range(N, M + 1):
    error = 0
    if num > 1:
        for i in range(2, num):  # 2부터 num-1까지
            if num % i == 0:
                error += 1
                break  # 몫이 0이면 error가 증가하고 for문을 끝냄
        if error == 0:
            prime.append(num)


if len(prime) > 0:
    print(sum(prime))
    print(min(prime))

    # print(prime)

else:
    print(-1)
