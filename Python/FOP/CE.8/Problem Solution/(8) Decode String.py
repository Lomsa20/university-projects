def decode(d):
    stack_n, stack_s = [], ['']
    num = 0
    for char in d:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '[':
            stack_n.append(num)
            stack_s.append('')
            num = 0
        elif char == ']':
            repeat = stack_n.pop()
            segment = stack_s.pop()
            stack_s[-1] += segment * repeat
        else:
            stack_s[-1] += char
    return stack_s[0]
k = decode(input('Enter a number: '))
print(k)