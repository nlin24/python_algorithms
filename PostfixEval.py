import Stack
'''
Implement the postfix string evaluation here http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
'''

def postfixEval(postfix_string):
    operandStack = Stack.Stack()
    for token in postfix_string:
        if token == " ":
            continue
        elif token == "+" or token == "-" or token == "*" or token == "/":
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            if token == "+":
                operandStack.push(operand1 + operand2)
            elif token == "-":
                operandStack.push(operand1 - operand2)
            elif token == "*":
                operandStack.push(operand1 * operand2)
            elif token == "/":
                operandStack.push(operand1 / operand2)
        else:
            if token.isdigit():
                operandStack.push(int(token))

    return operandStack.pop()

if __name__ == "__main__":
    #print(postfixEval('7 8 + 3 2 + /'))
    print(postfixEval(" 17 10 + 3 * 9 / "))

