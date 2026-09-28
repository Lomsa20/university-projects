def validate_tags(html):
    stack = []
    i = 0
    while i < len(html):
        if html[i] == '<':
            j = html.find('>', i)
            tag = html[i+1:j]
            if not tag.startswith('/'):
                stack.append(tag)
            else:
                if not stack or stack[-1] != tag[-1]:
                    return False
                stack.pop()
            i = j
        i += 1
    return not stack