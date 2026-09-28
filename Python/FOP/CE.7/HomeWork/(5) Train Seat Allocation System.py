class Node:
    def __init__(self, seat_n, status):
        self.seat_n = seat_n
        self.status = status
        self.next = None
class SLL:
    def __init__(self):
        self.head = None

    def add_booking(self,seat_n,status):
        new_node = Node(seat_n,status)
        if not self.head:
            self.head = new_node
            return
        temp =self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def cancel_booking(self,seat_n):
        if not self.head:
            return False
        if self.head.seat_n == seat_n:
            self.head = self.head.next
            return True

        prev = self.head
        curr = self.head.next if self.head else None
        while curr:
            if curr.seat_n == seat_n:
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def display(self):
        current = self.head
        while current:
            print(f"{current.seat_n} {current.status}", end=' <=> ')
            current = current.next
        return 'None'
s = SLL()

s.add_booking(1, "booked")
s.add_booking(2, "booked")
s.add_booking(3, "booked")

s.display()
print()

s.cancel_booking(2)

s.display()

