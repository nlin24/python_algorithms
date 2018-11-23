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
    
    # Add item at the head of the unordered list because it's the easiest
    # Track the end position. Update the end position only at the first add operation
    def add(self, item):
        tmp = self.head
        self.head = Node.Node(item)
        self.head.setNextNode(tmp)
        if self.head.getNextNode() == None:
            self.end = self.head
    
    # Count number of nodes in the unsorted list by traversing through the list
    def size(self):
        count = 0
        current = self.head
        while current != None:
            current = current.getNextNode()
            count += 1 
        return count

    # Return True/False if the item is in the unsorted list. Search by traversing through the list
    def search(self, item): 
        found = False
        current = self.head
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNextNode()
        
        return found
    
    # Implement remove by search(item) and then disconnecting the node, reconnecting to the previous node.getNextNode()
    def remove(self, item):
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
    
    # Append to the end of the list. Update the end position to the new item
    def append(self, item): 
        newNode = Node.Node(item)
        self.end.setNextNode(newNode)
        self.end = self.end.getNextNode()
        
    def insert(self, position, item): 
        return None
    
    # Pop the head of the list
    def pop(self): 
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
    print("unordered list data:")
    while mylist.head != None:
        print(mylist.pop())
