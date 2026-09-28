 class Node:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None

    def add_item(self, name, quantity):
        new_node = Node(name, quantity)
        if not self.head or self.head.name > name:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next and temp.next.name < name:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def merge(self, other):
        dummy = Node("dummy", 1)
        tail = dummy
        a, b = self.head, other.head

        while a and b:
            if a.name < b.name:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a or b

        merged = Inventory()
        merged.head = dummy.next
        return merged

    def show(self):
        items = []
        temp = self.head
        while temp:
            items.append(f"{temp.name}, {temp.quantity}")
            temp = temp.next
        return items

inv1 = Inventory()
inv1.add_item('Apple', 10)
inv1.add_item('Orange', 5)

inv2 = Inventory()
inv2.add_item('Banana', 7)
inv2.add_item('Peach', 3)

merged = inv1.merge(inv2)
print(merged.show())
