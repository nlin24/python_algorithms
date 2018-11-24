'''
Implementing various searching algorithms per https://interactivepython.org/runestone/static/pythonds/SortSearch/TheSequentialSearch.html
'''

def sequentialSearch(aList, item):
    found = False
    for i in aList:
        if i == item:
            found = True
    
    return found

if __name__ == "__main__":
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))