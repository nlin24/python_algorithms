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
        subList = aList[half:]
    else:
        subList = aList[:half]
    for i in subList:
        if item == i:
            return True
    return found

if __name__ == "__main__":
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))

    testlist2 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binarySearch(testlist2, 2))
    print(binarySearch(testlist2, 33))