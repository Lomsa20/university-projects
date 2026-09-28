class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def find_mid(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data