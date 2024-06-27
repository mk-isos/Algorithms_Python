N, K = map(int, input().split())
List = []
for i in range(1, N + 1):
    if N % i == 0:
        List.append(i)

if len(List) < K:
    print(0)
else:
    print(List[K - 1])

    # 인덱스 번호에 맞춰서 K-1번째로 해야함
