# print(n)
# print(1)

###############
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         sum <- sum + A[i]; # 코드1
#     return sum;
# }

# 코드는 입력값에 따라 함수 내에서 for문이 입력한 값만큼 돌아가니까

# 입력한 값 (수행횟수)
# 1 (다항식으로 수행횟수 n에 비례하므로 최고차항은 1)

import sys

n = sys.stdin.readline().rstrip("\n")
print(n)
print(1)

# .rstrip("\n")은 문자열에서 오른쪽 끝에 있는 개행 문자(\n)를 제거하는 메서드

# 따라서, n = sys.stdin.readline().rstrip("\n")은
# 사용자로부터 입력 받은 문자열에서 오른쪽 끝에 있는 개행 문자를 제거한 후에 변수 n에 저장하는 코드
