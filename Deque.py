'''
Implement a Dque (double-queue) via https://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaDequeinPython.html
'''

class Deque:
    def __init__(self):
        self.deque = []
    
    def isEmpty(self):
        if self.deque:
            return False
        return True
    
    def size(self):
        return len(self.deque)

    def addFront(self, item):
        self.deque.append(item)
    
    def addRear(self, item):
        self.deque.insert(0, item)
    
    def removeFront(self):
        return self.deque.pop()
    
    def removeRear(self):
        return self.deque.pop(0)

if __name__ == "__main__":
    d=Deque()
    print(d.isEmpty())
    d.addRear(4)
    d.addRear('dog')
    d.addFront('cat')
    d.addFront(True)
    print(d.size())
    print(d.isEmpty())
    d.addRear(8.4)
    print(d.removeRear())
    print(d.removeFront())