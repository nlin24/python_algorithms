import Stack

def parChecker(symbolString):
    s = Stack.Stack()
    balanced = True
    index = 0
    matches = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(" or symbol == "[" or symbol == "{":
            s.push(symbol)
        elif symbol ==  matches[s.peek()]:
            s.pop()
        index += 1
    
    if s.isEmpty():
        return True
    else:
        return False

if __name__ == "__main__":
    print(parChecker('{{([][])}()}'))
    print(parChecker('[{()]'))
    print(parChecker('{({[][])}()}'))
