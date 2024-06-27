# 회원 수 입력
N = int(input())

# 회원 정보 입력 및 리스트에 저장
members = []
for _ in range(N):
    age, name = map(str, input().split())
    members.append((int(age), name))

# 나이가 증가하는 순으로 정렬, 나이가 같으면 가입한 순으로 정렬
members.sort(key=lambda x: (x[0], members.index(x)))

# 정렬된 회원 정보 출력
for member in members:
    print(member[0], member[1])
    
## 위는 런타임에러 
#  O(N^2)의 시간 복잡도

# 회원 수 입력
N = int(input())

# 회원 정보 입력 및 리스트에 저장
members = []
for i in range(N):
    age, name = input().split()
    members.append((int(age), name, i))

# 나이가 증가하는 순으로 정렬, 나이가 같으면 가입한 순으로 정렬
members.sort(key=lambda x: (x[0], x[2]))

# 정렬된 회원 정보 출력
for member in members:
    print(member[0], member[1])