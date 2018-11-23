'''
Implement unordered list via linked list per https://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
    
    def getData(self):
        return self.data

    def getNextNode(self):
        return self.nextNode
    
    def setData(self, newData):
        self.data = newData
    
    def setNextNode(self, nextNode):
        self.nextNode = nextNode

if __name__ == "__main__":
    temp = Node(93)
    print(temp.getData())