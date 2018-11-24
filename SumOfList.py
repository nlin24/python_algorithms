'''
Sum up a list by recursion per https://interactivepython.org/runestone/static/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html
'''

def sumOfList(numList):
    # The escape clause is that the list contains one element
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + sumOfList(numList[1:])

if __name__ == "__main__":
    l = [1,3,5,7,9]
    print(sumOfList(l))