import Stack
'''
Implement devide by 2 algorithm in 3.8 via stack
http://interactivepython.org/runestone/static/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html
'''

def devideByBase(num=0, base=2):
    digits = "0123456789ABCDEF"

    if type(num) != "int":
        try:
            num = int(num)
            base = int(base)
        except ValueError:
            print("Non-numeric data input found")
            return -1
        else:
            pass
            #print("converted to int")
        
    binaryStack = Stack.Stack()

    while num > 0:
        digit = num % base
        num = num // base
        binaryStack.push(digit)

    binString = ""
    while not binaryStack.isEmpty():
        binString = binString + digits[binaryStack.pop()]
    return binString

if __name__ == "__main__": 
    print(devideByBase("36"))
    print(devideByBase(25,2))
    print(devideByBase(25,16))
    print(devideByBase(25,8))
    print(devideByBase(256,16))
    print(devideByBase(26,26))
    print(devideByBase(23,12))
