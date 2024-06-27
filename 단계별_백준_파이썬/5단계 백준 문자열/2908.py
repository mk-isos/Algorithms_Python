# 일의 자리만 비교?

# [::-1] : 역순

A, B = input().split()
A = int(A[::-1])  
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)
