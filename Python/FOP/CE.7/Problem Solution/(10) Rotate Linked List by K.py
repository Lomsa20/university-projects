def rotate(head, k):
    if not head or not head.next:
        return head
    lenght = 1
    tail = head
    while tail.next:
        tail = tail.next
        lenght += 1
    tail.next = head
    k %= lenght
    steps = lenght - k 
    for _ in range(steps - 1):
        new_tail = head
    new_head = head
    new_tail.next = None
    return new_head