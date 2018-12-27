class BinaryTree:
    """
    A simple binary tree node
    """
    def __init__(self,nodeName):
        self.key = nodeName
        self.rightChild = None
        self.leftChild = None

    def insertLeft(self,newNode):
        """
        Insert a left child to the current node object
        Append the left child of the current node to the new node's left child
        """
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        """
        Insert a right child to the current node object
        Append the right child of the current node to the new node's right child
        """
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        """
        Return the right child of the root node
        """
        return self.rightChild
    
    def getLeftChild(self):
        """
        Return the left child of the root node
        """
        return self.leftChild
    
    def setRootValue(self,newValue):
        """
        Set the value of the root node
        """
        self.key = newValue
    
    def getRootValue(self):
        """
        Return the key value of the root node
        """
        return self.key

if __name__ == "__main__":
    r = BinaryTree('a')
    print(r.getRootValue()) #a
    print(r.getLeftChild()) #None
    r.insertLeft('b') 
    print(r.getLeftChild()) #binary tree object
    print(r.getLeftChild().getRootValue()) #b
    r.insertRight('c')
    print(r.getRightChild()) #binary tree object
    print(r.getRightChild().getRootValue()) #c
    r.getRightChild().setRootValue('hello') 
    print(r.getRightChild().getRootValue()) #hello
