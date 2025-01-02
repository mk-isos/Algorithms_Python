class QueueWithStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop() if self.out_stack else None

queue = QueueWithStacks()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20