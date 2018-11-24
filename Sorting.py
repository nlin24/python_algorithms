'''
Implement sorting algorithms per https://interactivepython.org/runestone/static/pythonds/SortSearch/sorting.html
'''

def bubbleSort(aList):
    for passNum in range(len(aList) -1, 0, -1):
        for index in range(passNum):
            if aList[index] > aList[index + 1]:
                tmp = aList[index]
                aList[index] = aList[index + 1]
                aList[index + 1] = tmp
    return aList

def testBubbleSort():
    alist = [54,26,93,17,77,31,44,55,20]
    bubbleSort(alist)
    print(alist)

if __name__ == "__main__":
    testBubbleSort()