class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
    def insertion(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def deletion(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                if temp.prev:
                    temp.prev.next = temp.next
                    if self.head:
                        self.head = self.head.next
                else:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                return
            temp = temp.next
    def reverse(self):
        current = self.head
        temp = None
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <=> ")
            current = current.next
        return "None"
    def traverse_back(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <=> ")
            current = current.prev
        return "None"
    