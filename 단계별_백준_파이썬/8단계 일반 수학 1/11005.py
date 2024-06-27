N, B = map(int, input().split())
s = ""
num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # 진법의 index를 알기위한

while N:
    s += str(num[N % B])
    N //= B

print(s[::-1])  # s를 뒤집어서 출력
