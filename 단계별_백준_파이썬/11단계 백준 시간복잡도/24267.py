# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 2
#         for j <- i + 1 to n - 1
#             for k <- j + 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

# MenOfPassion 알고리즘을 보면 총 반복문이 3번이니 두번째 줄은  3

################### 이거 말고 다른 풀이
# # https://sorryhyeon.tistory.com/65 여기 들어가서 식 캡쳐
# # 설명도 여기 참고

# n = int(input())
# print(((n-2)*(n-1)*(2*n-3)+3*(n-1)*(n-2))//12)
# print(3)
###############

# 6 을 예시로 들어보겠습니다.

# 첫 번째 for문은 1, 2, 3, 4 까지 실행이 되겠네요.

# 첫 번째 for문이 1일 때,
# 두 번째 for문은 2, 3, 4, 5 까지 실행이 됩니다.

# 그렇다면 첫 번짜 for문이 1, 두번 째 for문이 2 일 때는?
# 세 번째 for문이 3, 4, 5, 6 까지 실행이 됩니다.

# 첫 번짜 for문이 1, 두번 째 for문이 3 일 때는?
# 세 번째 for문이 4, 5, 6 까지 실행이 됩니다.

# 즉, 1 부터 n까지의 숫자중 3가지를 뽑아 중복 없이, 크기 순으로 작성하는 경우의 수가 수행 횟수
# 123, 124, 125, 126, 134, 135 ... 456

# nC3
# https://dev-mandos.tistory.com/124    여기서 식 가져오기

n = int(input())
print((n * (n - 1) * (n - 2)) / 6)
print(3)
# 위에 틀림

n = int(input())
print(n * (n - 1) * (n - 2) // 6)
print(3)
