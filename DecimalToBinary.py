import Stack
'''
Implement devide by 2 algorithm in 3.8 via stack
http://interactivepython.org/runestone/static/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html
'''

def devideBy2(num=0):
    if type(num) != "int":
        try:
            num = int(num)
        except ValueError:
            print("Non-numeric data input found")
            return -1
        else:
            print("converted to int")
        
    binaryStack = Stack.Stack()

    while num > 0:
        digit = num % 2
        num = num // 2
        binaryStack.push(digit)

    binString = ""
    while not binaryStack.isEmpty():
        binString = binString + str(binaryStack.pop())
    return binString

if __name__ == "__main__":
    print(devideBy2("36"))
