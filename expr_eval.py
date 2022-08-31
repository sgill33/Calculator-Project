from stack_arr import *

def postfix_eval(input_str: str) -> float:
    """Evaluates a postfix expression"""

    lst = input_str.split(' ')
    stack = Stack(30)

    for token in lst:
        if isfloat(token) == True:
            stack.push(float(token))
        else:
            if token == '+':
                if stack.size() < 2:
                    raise Exception('Insufficient operands')
                res = stack.pop() + stack.pop()
                stack.push(res)
            elif token == '-':
                if stack.size() < 2:
                    raise Exception('Insufficient operands')
                x = stack.pop()
                y = stack.pop()
                res = y-x
                stack.push(res)
            elif token == '⁒':
                if stack.size() < 2:
                    raise Exception('Insufficient operands')
                x = stack.pop()
                y = stack.pop()
                res = y/x
                stack.push(res)
            elif token == 'x':
                if stack.size() < 2:
                    raise Exception('Insufficient operands')
                res = stack.pop() * stack.pop()
                stack.push(res)
            else:
                raise Exception('Invalid token')

    if stack.size() == 1:
        return stack.pop()
    else:
        raise Exception('Too many operands')


def infix_to_postfix(input_str: str) -> str:
    """Converts an infix expression to an equivalent postfix expression"""
    prec = {}
    prec['x'] = 2
    prec['⁒'] = 2
    prec['-'] = 1
    prec['+'] = 1

    out = ''
    ops = Stack(30)
    lst = input_str.split(' ')

    for token in lst:
        if isfloat(token) == True:
            out = out + token + ' '
        elif token == '+' or '-' or '⁒' or 'x':
            while ops.size() > 0 and prec[ops.peek()] >= prec[token]:
                out = out + ops.pop() + ' '
            ops.push(token)

    while ops.size() > 0:
            out = out + ops.pop() + ' '
    return out[:len(out)-1]


def isfloat(num: Any) -> bool:
    '''tries to convert number to float. If able to, returns True. If not, returns False'''
    try:
        float(num)
        return True
    except ValueError:
        return False