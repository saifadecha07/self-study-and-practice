# Session: Reviewing docs before bed
# Note: This took a while to debug, but it works now.

# Source: GeeksforGeeks - Queue Data Structure
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0