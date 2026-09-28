class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def RevList(head):
    prv = None
    current = head
    while current:
          nxt = current.next
          current.next = prv
          prv = current
          current = nxt
    return prv

