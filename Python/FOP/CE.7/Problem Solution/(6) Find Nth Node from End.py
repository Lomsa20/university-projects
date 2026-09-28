class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def nth_node(head, n):
    first = second = head
    for i in range(n):
        first = first.next
    while first:
        first = first.next
        second = second.next
    return second.data

def listprint(head):
    cur = head
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
    print()

# build a list: 10 → 20 → 30 → 40 → 50
head = Node(10)
e1 = Node(20)
e2 = Node(30)
e3 = Node(40)
head.next = e1
e1.next = e2
e2.next = e3

listprint(head)

print("nth node from end (n=2):", nth_node(head, 2))
