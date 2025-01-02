class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 원형 연결 리스트 확인 함수
    def is_circular(self):
        if not self.head:
            return False
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next           # 한 칸 이동
            fast = fast.next.next      # 두 칸 이동

            if slow == fast:           # 두 포인터가 만난다면 원형
                return True
        
        return False                   # 빠른 포인터가 None이면 원형 아님

# 원형 연결 리스트 생성 및 확인
ll = LinkedList()
ll.add(3)
ll.add(2)
ll.add(1)

# 원형으로 만들기
ll.head.next.next.next = ll.head

print("원형 연결 리스트인가?", ll.is_circular())  # Output: True