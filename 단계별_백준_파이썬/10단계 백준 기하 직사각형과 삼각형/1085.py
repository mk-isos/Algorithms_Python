x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))


################### 이 문제는 아래가 느림
import sys

input = sys.stdin.readline
x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))


# 주된 차이는 대개 sys.stdin.readline이 실행 시간 측면에서 input()보다 빠르다는 것입니다.
# 특히 큰 양의 입력 데이터를 읽어야 하는 상황에서 더욱 빠릅니다.

# 빠르고 간단한 작업의 경우 input()을 사용하는 것이 편리하고 충분합니다.
# 그러나 대량의 입력 데이터가 있는 성능 중요한 응용 프로그램의 경우 속도를 위해 sys.stdin.readline을 선호할 수 있습니다.
