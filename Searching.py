'''
Implementing various searching algorithms per https://interactivepython.org/runestone/static/pythonds/SortSearch/TheSequentialSearch.html
'''

def sequentialSearch(aList, item):
    # for unsorted list only
    found = False
    for i in aList:
        if i == item:
            found = True
    return found

def binarySearch(aList, item):
    # for ordered list only
    found = False
    half = len(aList)//2
    midValue = aList[len(aList)//2]
    subList = []
    if item == midValue:
        return True
    elif item > midValue:
        subList = aList[half+1:]
    else:
        subList = aList[:half]
    for i in subList:
        if item == i:
            return True
    return found

def binarySearchRecursion(aList, item):
    # Binary search implemented via recursions    
    # Base case is when the item is not in aList, return false
    if len(aList) == 0:
        return False
    else:
        # Reduce the aList size by half until it is length of 1 or 0 when item is not in list
        midpoint = len(aList)//2
        first = 0
        last = len(aList) -1
        if aList[midpoint] == item:
            return True
        else:
            if item > aList[midpoint]:
                return binarySearchRecursion(aList[midpoint+1:last], item)
            else:
                return binarySearchRecursion(aList[first:midpoint], item)

def testLinerSearch():
    print("[x] Test Liner Search:")
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))

def testBinarySearch():
    print("[x] Test Binary Search:")
    testlist2 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binarySearch(testlist2, 3))
    print(binarySearch(testlist2, 13))

def testBinarySearchRecursion():
    print("[x] Test Binary Search via Recursions:")
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binarySearchRecursion(testlist, 3))
    print(binarySearchRecursion(testlist, 13))
    print(binarySearchRecursion(testlist, 44))

def testSubList():
    testlist = [0, 1, 2, 8, 13, 17, 19, 32,]
    half = len(testlist) //2
    print(half)
    print(testlist[half])
    print(testlist[:half])
    print(testlist[half:])

if __name__ == "__main__":
    #testSubList()    
    #testLinerSearch()
    #testBinarySearch()
    testBinarySearchRecursion()
    