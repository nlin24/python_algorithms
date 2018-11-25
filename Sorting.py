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

def shellSort(alist):
    # first pick the sublist size. In this example we split the list in two
    sublistCount = len(alist) // 2

    while sublistCount > 0:
        for startPosition in range(sublistCount):
            gapInsertionSort(alist,startPosition, sublistCount)
        
        print("After increment of size", sublistCount, "The list is ", alist)

        sublistCount = sublistCount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentValue = alist[i]
        currentPosition = i
        while currentPosition >= gap and currentValue < alist[currentPosition-gap]:
            alist[currentPosition] = alist[currentPosition-gap]
            currentPosition = currentPosition - gap
        alist[currentPosition] = currentValue

def mergeSort(alist):
    print("[x] Splitting",alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]
        
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0 # index for left half
        j = 0 # index for right half
        k = 0 # index for merging list
        
        # merge the two halves
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] > rightHalf[j]:
                print("alist pick right in right/left compareson:", rightHalf[j])
                alist[k] = rightHalf[j]
                j = j + 1
            else:
                print("alist pick left in right/left compareson:", leftHalf[i])
                alist[k] = leftHalf[i]
                i += 1
            k += 1
        
        while i < len(leftHalf):
            print("alist merges left:", leftHalf[i])
            alist[k] = leftHalf[i]
            i += 1
            k += 1
        
        while j < len(rightHalf):
            print("alist merges right:", rightHalf[j])
            alist[k] = rightHalf[j]
            j += 1
            k += 1
    print("[o] Merging ", alist)

def testMergeSort():
    #alist = [54,26,93,17,77,31,44,55,20]
    alist = [3,2,1,4]
    mergeSort(alist)
    print(alist)

def testShellSort():
    alist = [54,26,93,17,77,31,44,55,20]
    shellSort(alist)
    print(alist)

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
    #testBubbleSort()
    #testSelectionSort()
    #testInsertionSort()
    #testShellSort()
    testMergeSort()