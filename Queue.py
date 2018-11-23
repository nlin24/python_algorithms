'''
Implement queue via Python list per https://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaQueueinPython.html
'''

class Queue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        if not self.queue:
            return True
        return False

    def enqueue(self, item):
        self.queue.insert(0,item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

if __name__ == "__main__":
    tQueue = Queue()
    print(tQueue.size())
    print(tQueue.isEmpty())
    tQueue.enqueue('amy')
    print(tQueue.size())
    print(tQueue.isEmpty())
    print(tQueue.dequeue())
