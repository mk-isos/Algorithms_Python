from collections import deque

n = int(input())

cards = list(range(1, n+1))

cards = deque(cards)

while len(cards) > 1:
    # 제일 위에 있는 카드를 버림
    discarded_card = cards.popleft()
    # 제일 위에 있는 카드를 제일 아래로 옮김
    cards.append(cards.popleft())

print(cards[0])
