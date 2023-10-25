class Stack:
    def __init__(self, N):
        self.element = [0] * N
        self.size = 0

    def push(self, x):
        self.element[self.size] = x
        self.size += 1

    # Doesn't actually delete the item. Changing size DOES mean this remaining value will never be returned.
    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.element[self.size]
        else:
            return None
    
    def is_empty(self):
        return self.size == 0