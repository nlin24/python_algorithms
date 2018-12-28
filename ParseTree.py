import Stack
import BinaryTrees
import operator

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack.Stack()
    eTree = BinaryTrees.BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']: # i is an operand
            currentTree.setRootValue(int(i))
            parentNode = pStack.pop()
            currentTree = parentNode
        elif i in ['+','-','*','/']: # i is an operator
            currentTree.setRootValue(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    """
    """
    oper = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv
    }
    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()
    if leftChild and rightChild:
        func = oper[parseTree.getRootValue()]
        return func(evaluate(leftChild),evaluate(rightChild))
    else:
        return parseTree.getRootValue()

if __name__ == "__main__":
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")
    print(evaluate(pt))
