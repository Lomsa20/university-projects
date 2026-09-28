def simplify_path(path):
    stack = []
    for part in path.split('/'): #for this one /a/./..
        if part == ""or part == ".": 
    # it doesnot matter if . or '' is there because nothing changes
            continue
        elif part =='..':
    #here it matter because it pops /a/./b/../c/ c here
            if stack:
                stack.pop()
            else:
                stack.append(part) 
        #if it is not part of stack then append
        return '/' + '/'.join(stack) 
        