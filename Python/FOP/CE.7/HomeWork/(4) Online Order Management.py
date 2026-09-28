class Node:
    def __init__(self, _id, status):
        self.id = _id
        self.status = status
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def add_order(self, _id, status):
        new_node = Node(_id, status)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def update_order(self, _id, new_status):
        temp = self.head
        while temp:
            if temp.id == _id:
                temp.status = new_status
                return
            temp = temp.next
        print("Order not found")

    def remove_completed_orders(self):
        if not self.head:
            return

        # remove from head
        while self.head and self.head.status == "completed":
            self.head = self.head.next

        prev = self.head
        curr = self.head.next if self.head else None

        while curr:
            if curr.status == "completed":
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

    def display(self):
        temp = self.head
        while temp:
            print(f"[ID:{temp.id}, Status:{temp.status}]", end=" -> ")
            temp = temp.next
        print("None")
