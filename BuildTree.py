r"""
Build the following tree
   a
   /\
  /  \
  b   c
   \  /\
    d e f
"""
from BinaryTrees import BinaryTree

def buildTree():
    t = BinaryTree('a')
    t.insertLeft('b')
    t.getLeftChild().insertRight('d')
    t.insertRight('c')
    t.getRightChild().insertLeft('e')
    t.getRightChild().insertRight('f')
    return t
