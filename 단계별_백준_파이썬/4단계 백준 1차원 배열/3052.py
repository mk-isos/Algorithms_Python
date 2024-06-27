# 서로 다른 값이 몇 개 있는지 출력하는 프로그램

# 찾아본 다른 풀이 법
#set()함수는 중복된 값을 뺄 수 있으나, 순서가 뒤죽박죽이 된다. 
# 이 문제에서는 순서대로 출력할 필요가 없으므로 사용가능하다.
arr = []
for i in range(10):
    a = int(input())
    arr.append(a % 42)
print(len(set(arr)))

# 내 풀이
arr = []
for i in range(10):
    a = int(input())
    if a%42 not in arr:
        arr.append(a % 42)
print(len(arr))