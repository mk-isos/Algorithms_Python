t = int(input())

for i in range(t):
    
    result = input()
    
    score = 0
    
    consecutive_o = 0
    
    for char in result:
        if char == 'O':
            consecutive_o += 1
            score += consecutive_o
        else:
            consecutive_o = 0  # X가 나오면 연속된 O의 개수 초기화

    print(score)