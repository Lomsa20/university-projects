def postfix(s):
    stack = []
    for token in s.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.append(int(token))
            if token == '+':
                stack.append(a + b)
            elif token == '*':
                stack.append(a * b)
            elif token == '-':
                stack.append(a - b)
            elif token == '/':
                stack.append(a / b)
    return stack.pop
