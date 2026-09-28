class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def remove_dublicate(head):
    current = head
    while current and current.next:
        current = current.next
        if current.next:
            current.next = current.next.next
    return head
def print_list(head):
    cur = head
    while cur:
        print(cur.data, end=" -> ")
        cur = cur.next
    print("None")
head = Node(1)
e1 = Node(2)
e2 = Node(3)
e3 = Node(4)
e4 = Node(5)

head.next = e1
e1.next = e2
e2.next = e3
e3.next = e4
print_list(remove_dublicate(head))
