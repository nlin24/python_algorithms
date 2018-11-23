import Stack
'''
Infix to Postfix conversion per http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
'''

def InfixToPostfix(math_string):
    opstack = Stack.Stack()
    ans = ""
    opPrecedence = {
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
        "(": 0
    }

    for token in math_string:
        
        if token == " ":
            continue
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            check = opstack.peek()
            while check != "(":
                ans = ans + opstack.pop()
                check = opstack.peek()
                if check == "(":
                    opstack.pop()
                    break
        elif  token == "+" or token == "-" or token == "*" or token == "/":
            # Push the operator when it has higher precedance than the operators already in stack
            if opstack.isEmpty() or opPrecedence[token] > opPrecedence[opstack.peek()]:
                opstack.push(token)
            # if an operator with lower precedence is encountered, then pop the ones in stack first before pushing the new one to stack
            else:
                check = opstack.peek()
                while check != "(":
                    if opPrecedence[token] > opPrecedence[check]:
                        break
                    ans = ans + opstack.pop()
                    if opstack.isEmpty():
                        break
                    check = opstack.peek()
                opstack.push(token)
        # Append to ans list if operand found
        else:
            ans = ans + token

    while not opstack.isEmpty():
        ans = ans + opstack.pop()
    return ans

if __name__ == "__main__":
    print(InfixToPostfix("A * B + C * D"))
    print(InfixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(InfixToPostfix("D + ( A * B + C ) "))
    print(InfixToPostfix("A * B * C "))
    print(InfixToPostfix("1 + 3 * 5 / (6 - 4)"))
