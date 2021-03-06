'''
Sum up a list by recursion per https://interactivepython.org/runestone/static/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html
'''

def sumOfList(numList):
    # The escape clause is that the list contains one element
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + sumOfList(numList[1:])

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

# Convert an integer to any base by recursion
def IntToString(num, base):
    convertString = "0123456789ABCDEF"
    if num < base:
        return convertString[num]
    else:
        return IntToString(num // base, base) + convertString[num % base]

# Reverse a string by recursion
def reverse(inputString):
    if inputString == "":
        return ""
    else:
        if len(inputString) == 1:
            return inputString[0]
        else:
            return reverse(inputString[1:]) + inputString[0]

# Check if an input string is a palindrome via recursion and the reverse function
def checkPalindrome(inputString):
    if inputString == reverse(inputString):
        return True
    else:
        return False

# Calculate the number of coins for changes via recursions
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

if __name__ == "__main__":
    print(sumOfList([2,4,6,8,10]))
    print(fact(7))
    print(IntToString(967, 10))
    print(IntToString(1453, 16))
    print(IntToString(10, 2))
    print(reverse("world"))
    print(reverse("l"))
    print(reverse("follow"))
    print(reverse(""))

    print(checkPalindrome("kayak"))
    print(checkPalindrome("aibohphobia"))
    print(checkPalindrome("Livenotonevil".lower()))
    print(checkPalindrome("RevileddidIlivesaidIasevilIdiddeliver".lower()))
    print(checkPalindrome("Kanakanak".lower()))
    print(checkPalindrome("hello".lower()))
    print(recMC([1,5,10,25],50))