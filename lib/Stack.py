class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            self.stack = []
        else:
            self.stack = list(items)
        self.limit = limit

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        if self.limit is None or len(self.stack) < self.limit:
            self.stack.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")

    def size(self):
        return len(self.stack)

    def full(self):
        if self.limit is None:
            return False
        return len(self.stack) == self.limit

    def search(self, target):
        if target in self.stack:
            return len(self.stack) - self.stack.index(target) - 1
        else:
            return -1