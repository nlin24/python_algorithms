'''
Implement hash methods per https://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html
'''

def hashFolding(aString, tableSize):
    # Implement the folding hash method
    stringSum = 0
    for i in aString:
        stringSum = stringSum + ord(i)
    
    # Calculate hash value via remainder method
    return stringSum % tableSize

if __name__ == "__main__":
    print(hashFolding('cat', 11))