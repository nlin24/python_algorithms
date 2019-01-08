import Node

'''
Impelement unordered list via Node per https://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
'''

class UnorderedList:
    def __init__(self):
        self.head = None
        self.end = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
    def add(self, item):
        '''
        Add item at the head of the unordered list because it's the easiest. Track the end position. Update the end position only at the first add operation
        '''
        tmp = self.head
        self.head = Node.Node(item)
        self.head.setNextNode(tmp)
        if self.head.getNextNode() == None:
            self.end = self.head
    
    def size(self):
        '''
        Count number of nodes in the unsorted list by traversing through the list
        '''
        count = 0
        current = self.head
        while current != None:
            current = current.getNextNode()
            count += 1 
        return count

    def search(self, item): 
        '''
        Return True/False if the item is in the unsorted list. Search by traversing through the list
        '''
        found = False
        current = self.head
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNextNode()
        
        return found

    def remove(self, item):
        '''
        Implement remove by search(item) and then disconnecting the node, reconnecting to the previous node.getNextNode()
        '''
        found = False
        # Handle special case where item is found at the head. If not traverse the list
        if self.head.getData() == item:
            found = True
            self.head = None
            return found
        else:
            currentNode = self.head
        while currentNode != None:
            nextNode = currentNode.getNextNode()    
            if nextNode != None:
                if nextNode.getData() == item:
                    found = True
                    currentNode.setNextNode(nextNode.getNextNode())
                    break
                else:
                    tmp = nextNode
                    currentNode = nextNode
                    nextNode = tmp.getNextNode()
            else:
                currentNode = currentNode.getNextNode()

        return found
    
    def append(self, item): 
        '''
        Append to the end of the list. Update the end position to the new item
        '''
        newNode = Node.Node(item)
        self.end.setNextNode(newNode)
        self.end = self.end.getNextNode()
        
    def insertAt(self, index=None, value=0):
        '''
        Insert value in the list at the index position
        '''
        currentNode = self.head
        newNode = Node.Node(value)
        i = 0
        if index > self.size() or index == None:
            raise IndexError('index greater than list size')
        while i < index-1:
            currentNode = currentNode.getNextNode()
            i += 1
        newNode.setNextNode(currentNode.getNextNode())
        currentNode.setNextNode(newNode)
        return None
    
    def deleteAt(self, index=None):
        '''
        Delete node at the indexed position
        '''
        i = 0
        currentNode = self.head
        if index > self.size() or index == None:
            raise IndexError('index greater than list size')
        while i < index-1:
            currentNode = currentNode.getNextNode()
            i += 1
        currentNode.setNextNode((currentNode.getNextNode()).getNextNode())
        return None

    def pop(self): 
        '''
        Pop the head of the list
        '''
        if self.head != None:
            result = self.head.getData()
            self.head = self.head.getNextNode()
        else: 
            result = "Empty"
        return result

if __name__ == "__main__":
    mylist = UnorderedList()
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.append(0)
    mylist.append(4)
    mylist.insertAt(3,10)
    mylist.deleteAt(3)
    print("unordered list data:")
    while mylist.head != None:
        print(mylist.pop())
