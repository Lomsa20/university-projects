class Node:
    def __init__(self, name, n_seats):
        self.name = name
        self.n_seats = n_seats
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def add_booking(self, name, n_seats):
        new_node = Node(name, n_seats)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def cancel_booking(self, n_seats):
        if not self.head:
            print("No booking")
            return
        if self.head.n_seats == n_seats:
            print(f"The booking seat: {n_seats} is cancelled")
            self.head = self.head.next
            return
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.n_seats == n_seats:
                prev.next = curr
                curr.next = curr.next
    def reversed_booking(self):
        prev = None
        curr = self.head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    def display(self):
        curr = self.head
        while curr:
            print(curr.name, end = ' <=> ')
            curr = curr.next
        return 'None'
sll = SLL()
sll.add_booking("Alice", 1)
sll.add_booking("Bob", 2)
sll.add_booking("Charlie", 3)
sll.display()
sll.cancel_booking(2)
sll.display()
sll.reversed_booking()
sll.display()