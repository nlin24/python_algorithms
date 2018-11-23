import Node
'''
Implement ordered list via Node per https://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganOrderedList.html
'''

class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def search(self, item):
        found = False
        currentNode = self.head
        while currentNode != None:
            # If item is found, set found to True and break
            if currentNode.getData() == item:
                found = True
                break
            # If node value is greater than item, stop iteration because the item is not in the list
            elif currentNode.getData() > item:
                break
            else:
                currentNode = currentNode.getNextNode()
        return found

    # add the item in ascending order
    def add(self, item):
        newNode = Node.Node(item)
        previousNode = None
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode != None:
                if currentNode.getData() <= item:
                    if currentNode.getNextNode() == None:
                        currentNode.setNextNode(newNode)
                        break
                    else:
                        previousNode = currentNode
                        currentNode = currentNode.getNextNode()
                elif currentNode.getData() > item:
                    if previousNode == None:
                        newNode.setNextNode(currentNode)
                        self.head = newNode
                    else:
                        newNode.setNextNode(currentNode)
                        previousNode.setNextNode(newNode)
                    break
                    
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNextNode()
        return count

    def index(self):
        return None

    def remove(self, item):
        return None

    def pop(self):
        currentNode = self.head
        self.head = currentNode.getNextNode()
        return currentNode.getData()

if __name__ =="__main__":
    mylist = OrderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))
    
    for i in range(mylist.size()):
        print(mylist.pop())

