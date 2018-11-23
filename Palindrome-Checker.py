import Deque

'''
Implement a palindrome checking algorithm via deque per https://interactivepython.org/runestone/static/pythonds/BasicDS/PalindromeChecker.html
'''

def palindromeChecker(aString):
    stringDeque = Deque.Deque()
    for letter in aString:
        stringDeque.addFront(letter)
    while stringDeque.size() > 1:
        last = stringDeque.removeFront()
        first = stringDeque.removeRear() 
        if first == last:
            continue
        else:
            break
    if stringDeque.size() > 1:
        return False
    else:
        return True

if __name__ == "__main__":
    print(palindromeChecker("lsdkjfskf"))
    print(palindromeChecker("radar"))
    print(palindromeChecker("EvedamnedEdenmadEve".lower()))