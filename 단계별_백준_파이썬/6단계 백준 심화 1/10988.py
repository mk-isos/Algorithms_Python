# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어

word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)