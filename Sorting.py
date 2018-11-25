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

# Enhanced bubble sort, stopping when no element has been exchagned
def shortBubbleSort(alist):
    exchanged = False
    for passNum in range(len(alist)-1,0,-1):
        exchanged = False
        for i in range(passNum):
            if alist[i] > alist[i+1]:
                tmp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = tmp
                exchanged = True
        if exchanged == False:
            return alist

def selectionSort(alist):
    for i in range(len(alist)-1, 0, -1 ):
        maxIndex = 0
        for j in range(1,i+1):
            if alist[maxIndex] < alist[j]:
                maxIndex = j
        tmp = alist[i]
        alist[i] = alist[maxIndex]
        alist[maxIndex] = tmp

def insertionSort(alist):
    for index in range(1,len(alist)):
        currentValue = alist[index]
        currentPosition = index
        while currentPosition > 0 and currentValue < alist[currentPosition-1]:
            alist[currentPosition] = alist[currentPosition-1]
            currentPosition = currentPosition - 1
        alist[currentPosition] = currentValue

def testInsertionSort():
    alist = [54,26,93,17,77,31,44,55,20]
    insertionSort(alist)
    print(alist)



def testSelectionSort():
    alist = [54,26,93,17,77,31,44,55,20]
    selectionSort(alist)
    print(alist)

def testBubbleSort():
    alist = [54,26,93,17,77,31,44,55,20]
    bubbleSort(alist)
    clist=[1,3,2,4,5]
    shortBubbleSort(clist)
    bubbleSort(clist)
    print(alist)
    print(clist)

if __name__ == "__main__":
    testBubbleSort()
    testSelectionSort()
    testInsertionSort()
