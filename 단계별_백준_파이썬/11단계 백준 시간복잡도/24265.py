# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }


n = int(input())

print(int(n * (n - 1) - (n - 1) * n / 2))
print(2)

# ex ) n = 6
# 반복횟수 5,4,3,2,1번
# n-1,n-2,...,n-5 까지 감소
# (n + n + ... + n) - (1 + 2 + ... + 5)
# n을 n-1번 더한 수에서 첫째항이 1이고 마지막항이 n-1인 등차 수열의 합을 뺴주면 되겠다.
