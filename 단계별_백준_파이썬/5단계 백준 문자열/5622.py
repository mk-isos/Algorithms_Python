## 어케 푸노

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'] # 2초부터 1초씩
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)


# dial 리스트는 각 알파벳이 속한 다이얼을 나타냅니다.
# 사용자로부터 입력된 단어를 각 문자에 대해 반복합니다.
# 현재 문자가 어떤 다이얼에 속하는지를 찾고, 해당 다이얼의 인덱스에 3을 더해 최소 시간으로 누적합니다.
# 최종적으로 누적된 값이 전화를 걸기 위해 필요한 최소 시간이 됩니다.


# 다이얼에 대한 정보를 리스트로 정의합니다.
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']  # 2초부터 1초씩

# 사용자로부터 단어를 입력받습니다.
a = input()

# 필요한 최소 시간을 저장할 변수를 초기화합니다.
ret = 0

# 입력된 단어의 각 문자에 대해서 반복합니다.
for j in range(len(a)):
    # 다이얼 리스트를 순회하면서 현재 문자가 속한 다이얼을 찾습니다.
    for i in dial:
        if a[j] in i:
            # 현재 다이얼의 인덱스에 3을 더한 값을 누적으로 더해줍니다.
            # 이때, 다이얼의 인덱스에 3을 더하는 이유는 다이얼의 첫 숫자가 2이기 때문입니다.
            ret += dial.index(i) + 3

# 최종적으로 구해진 총 시간을 출력합니다.
print(ret)
