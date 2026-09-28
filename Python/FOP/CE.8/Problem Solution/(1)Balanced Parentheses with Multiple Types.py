def is_balanced(s):
    stack = []
    mapping = {')':'(','}':'{', ']':'['}
    for char in s:
        if char in mapping.values(): #opening brackets
            stack.append(char)
        elif char in mapping.keys(): #closing brackets
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack
k = input('Enter a string to check if it is balanced: ')
print(is_balanced(k))
