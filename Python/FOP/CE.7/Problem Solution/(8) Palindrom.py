def is_palindrom(head):
    vals = []
    current = head
    while current:
        vals.append(current.data)
        current = current.next
    return vals == vals[::-1]