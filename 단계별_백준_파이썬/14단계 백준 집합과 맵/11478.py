s = input().strip()
n = len(s)
substrings = set()  # 서로 다른 부분 문자열을 저장할 set 초기화

for i in range(n):
    for j in range(i + 1, n + 1):
        substrings.add(s[i:j])  # 모든 가능한 부분 문자열

result = len(substrings)
print(result)

# s = input().strip()
# strip() 메서드를 사용하여 양쪽의 공백을 제거