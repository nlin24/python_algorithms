class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        if not self.items:
            return True
        return False

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    s.push('dog')
    print(s.peek())
    s.push('cat')
    print(s.peek())
    s.pop()
    print(s.peek())
    print(s.size())
    